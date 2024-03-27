import requests
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_url = 'https://api.github.com/graphql'
ROOT_PATH = os.getcwd().split('lab-experimentacao-software-02/scripts')[0].replace('\\', '/')
headers = {'Authorization': 'Bearer %s' % API_KEY}
allResults = list()


def fetch_repository_data(numRepos):
    endCursor = None

    for i in range(int(numRepos / 2)):
        variables = {"endCursor": endCursor}
        query_result = make_graphql_request(variables)
        allResults.append(query_result)
        endCursor = query_result['data']['search']['pageInfo']['endCursor']

    return allResults


def make_graphql_request(variables):
    query = """
    query ($endCursor: String) {
    search(query: "language:Java stars:>1 fork:false sort:stars-desc", type: REPOSITORY, first:2, after: $endCursor) {
        edges {
            node {
                ... on Repository {
                    url
                    nameWithOwner
                    name
                    owner {
                        login
                    }
                    createdAt
                    updatedAt
                    primaryLanguage {
                        name
                    }
                    stargazers {
                        totalCount
                    }
                    releases {
                        totalCount
                    }
                }
            }
        }
        pageInfo {
            endCursor
            hasNextPage
        }
    }
}
    """
    request = requests.post(url=api_url, json={'query': query, 'variables': variables}, headers=headers)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))


def save_to_csv(result):
    data_to_csv=[]

    for i in range(len(result)):
        edges = result[i]['data']['search']['edges']
        for edge in edges:
            repository = edge['node']
            repo_name = repository['name']
            owner_login = repository['owner']['login']
            repo_url = repository['url']
            stars = repository['stargazers']['totalCount']
            releases = repository['releases']['totalCount']

            created_at = pd.to_datetime(repository['createdAt'])
            updated_at = pd.to_datetime(repository['updatedAt'])
            years_diff = round((updated_at - created_at).days / 365, 2)

            metrics = get_metrics(repo_name)
            
            avg_cbo = round(np.mean(metrics['cbo']) if metrics['cbo'] else np.nan, 2)
            median_cbo = round(np.median(metrics['cbo']) if metrics['cbo'] else np.nan, 2)
            std_cbo = round(np.std(metrics['cbo']) if metrics['cbo'] else np.nan, 2)
            avg_lcom = round(np.mean(metrics['lcom']) if metrics['lcom'] else np.nan, 2)
            median_lcom = round(np.median(metrics['lcom']) if metrics['lcom'] else np.nan, 2) 
            std_lcom = round(np.std(metrics['lcom']) if metrics['lcom'] else np.nan, 2)
            dit_max = np.max(metrics['dit']) if metrics['dit'] else np.nan
            dit_max = np.max(metrics['dit']) if metrics['dit'] else np.nan
            loc = np.sum(metrics['loc']) if 'loc' in metrics else np.nan

            data_to_csv.append([f'{owner_login}/{repo_name}', repo_name, stars, years_diff, releases, loc, avg_cbo, median_cbo, std_cbo, avg_lcom, median_lcom, std_lcom, dit_max])

    header = ['Repositório', 'Nome', 'Estrelas', 'Anos', 'Nº Releases', 'LOC', 'Média CBO', 'Mediana CBO', 'Desvio Padrão CBO', 'Média LCOM', 'Mediana LCOM', 'Desvio Padrão LCOM', 'DIT Max']
    df = pd.DataFrame(data_to_csv)
    
    csv_dir = f'{ROOT_PATH}/scripts/dataset/csv'
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)
        
    df.to_csv(f'{csv_dir}/data.csv', index=False, header=header)

    return df

def clone_repository(url):
     repo_url = url+".git"
     os.chdir(f'{ROOT_PATH}/scripts/repos/')
     os.system(f'git clone {repo_url}')
     
def delete_repositories(repository: str):
    repo_path = f'{ROOT_PATH}/scripts/repos/{repository}'
    if os.path.exists(repo_path):
        os.system(f'rmdir /S /Q {repository}')

def run_ck_calculator(repository: str):
    base_path = f'{ROOT_PATH}/scripts'
    ck_jar_path = f'{base_path}/ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar'
    repo_path = f'{base_path}/repos/{repository}'
    ck_results = f'{ROOT_PATH}/scripts/dataset/ck_results/{repository}/'
    
    if not os.path.exists(ck_results):
        os.makedirs(ck_results)
        
    ck_command = f'java -jar {ck_jar_path} {repo_path} true 0 false {ck_results}'
    os.system(ck_command)


def get_metrics(repository: str):
    df = pd.read_csv(f'{ROOT_PATH}/scripts/dataset/ck_results/{repository}/class.csv')
    
    metrics = {
        'cbo': df['cbo'].tolist(),
        'lcom': df['lcom'].tolist(),
        'dit': df['dit'].tolist(),
        'loc': df['loc'].tolist()
    }

    return metrics

def main():
    result = fetch_repository_data(10)
    for search_result in result:
        edges = search_result['data']['search']['edges']
        for edge in edges:
            repo_url = edge['node']['url']
            repo_name = edge['node']['name']
            clone_repository(repo_url)
            try:
                run_ck_calculator(repo_name)
            except Exception as e:
                print(f"Erro ao calcular métricas para o repositório {repo_name}: {e}")
            delete_repositories(repo_name)
            
    save_to_csv(result)


if __name__ == "__main__":
    main()
