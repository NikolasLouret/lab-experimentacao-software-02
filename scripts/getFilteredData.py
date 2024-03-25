import pandas as pd
import os

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

def main():
    javaRepositories = pd.read_csv(f'{ROOT_PATH}/scripts/dataset/csv/data.csv')
    
    calculate_repositories_age(javaRepositories)
    calculate_releases(javaRepositories)
    
    input_file = f'{ROOT_PATH}/scripts/dataset/ck_results/combined_results.csv'
    loc = calculate_mean(input_file, 'loc')
    cbo = calculate_mean(input_file, 'cbo')
    dit = calculate_mean(input_file, 'dit')
    lcom = calculate_mean(input_file, 'lcom')
    print(f'A média do campo "LOC" é: {loc}')
    print(f'A média do campo "CBO" é: {cbo}')
    print(f'A max do campo "CBO" é: {cbo}')
    print(f'A média do campo "DIT" é: {dit}')
    print(f'A média do campo "LCOM" é: {lcom}')

if __name__ == "__main__":
    main()