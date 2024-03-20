import requests
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_url = 'https://api.github.com/graphql'
ROOT_PATH = os.getcwd().split('lab-experimentacao-software-02/scripts')[0].replace('\\', '/')
headers = {'Authorization': 'Bearer %s' % API_KEY}
allResults = list()


def fetch_repository_data(numRepos):
    endCursor = None

    for i in range(int(numRepos/20)):
        variables = {"endCursor": endCursor}
        query_result = make_graphql_request(variables)
        allResults.append(query_result)
        endCursor = query_result['data']['search']['pageInfo']['endCursor']

    return allResults


def make_graphql_request(variables):
    query = """
    query ($endCursor: String) {
    search(query: "language:Java stars:>1 fork:false sort:stars-desc", type: REPOSITORY, first:20, after: $endCursor) {
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
                    stargazers{
                        totalCount
                    }
                    totalIssues: issues {
                        totalCount
                    }
                    closedIssues: issues(states: CLOSED) {
                        totalCount
                    }
                    pullRequests(states: MERGED) {
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
    df = pd.DataFrame()
    dfs = []

    for i in range(len(result)):
        normalized_data = pd.json_normalize(result[i]['data']['search']['edges'])
        dfs.append(normalized_data)

    df = pd.concat(dfs, ignore_index=True)

    # Save the dataframe directly to a CSV file
    df.to_csv('scripts/dataset/csv/data.csv', index=False)

    return df
    
def run_ck_calculator(repository: str):
    base_path = f'{ROOT_PATH}/scripts'
    ck_jar_path = f'{base_path}/ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar'
    repo_path = f'{base_path}/repos/{repository}'
    ck_results = f'{ROOT_PATH}/scripts/dataset/ck_results/{repository}/'
    
    if not os.path.exists(ck_results):
        os.makedirs(ck_results)
        
    ck_command = f'java -jar {ck_jar_path} {repo_path} true 0 false {ck_results}'
    os.system(ck_command)

    
def clone_repository(url):
     repo_url = url+".git"
     os.chdir('./scripts/repos/')
     os.system(f'git clone {repo_url}')
     
def delete_repositories(repository: str):
    repo_path = f'{ROOT_PATH}/scripts/repos/{repository}'
    if os.path.exists(repo_path):
        os.system(f'rmdir /S /Q {repository}')
    

def main():
    result = fetch_repository_data(1000)
    df = save_to_csv(result)
    clone_repository(result[0]['data']['search']['edges'][10]['node']['url'])
    run_ck_calculator(result[0]['data']['search']['edges'][10]['node']['name'])
    delete_repositories(result[0]['data']['search']['edges'][10]['node']['name'])

main()
