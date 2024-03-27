import pandas as pd
import os
import matplotlib.pyplot as plt

ROOT_PATH = os.getcwd().split('lab-experimentacao-software-02/scripts')[0].replace('\\', '/')

def calculate_mean(input_file, column):
    df = pd.read_csv(input_file, low_memory=False)
    mean = df[column].mean()
    return mean

def calculate_repositories_age(df):
    df['createdAt'] = pd.to_datetime(df['node.createdAt']).dt.tz_localize(None)
    df['repository_age'] = (pd.to_datetime('today').tz_localize(None) - df['createdAt']).dt.days / 365
    
def calculate_releases(df):
    df['node.releases.totalCount']

def get_cbo_and_stargazers(input_file, javaRepositories):
    cbo_values = pd.read_csv(input_file, low_memory=False)['cbo']
    dit_values = pd.read_csv(input_file, low_memory=False)['dit']
    lcom_values = pd.read_csv(input_file, low_memory=False)['lcom']
    stargazers_count = javaRepositories['node.stargazers.totalCount']

    min_len = min(len(cbo_values), len(dit_values), len(lcom_values), len(stargazers_count))
    cbo_values = cbo_values[:min_len]
    dit_values = dit_values[:min_len]
    lcom_values = dit_values[:min_len]
    stargazers_count = stargazers_count[:min_len]

    return cbo_values, dit_values, lcom_values, stargazers_count

def plot_scatter(x_values, y_values, x_label='', y_label='', title=''):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

def main():
    javaRepositories = pd.read_csv(f'{ROOT_PATH}/scripts/dataset/csv/data.csv')
    calculate_repositories_age(javaRepositories)
    calculate_releases(javaRepositories)
    
    input_file = f'{ROOT_PATH}/scripts/dataset/ck_results/combined_results.csv'
    cbo_values, dit_values, lcom_values, stargazers_count = get_cbo_and_stargazers(input_file, javaRepositories)
    plot_scatter(cbo_values, stargazers_count, 'CBO', 'Número de Estrelas', 'Relação entre CBO e o número de estrelas')
    plot_scatter(dit_values, stargazers_count, 'DIT', 'Número de Estrelas', 'Relação entre DIT e o número de estrelas')
    plot_scatter(lcom_values, stargazers_count, 'LCOM', 'Número de Estrelas', 'Relação entre LCOM e o número de estrelas')
    
if __name__ == "__main__":
    main()
