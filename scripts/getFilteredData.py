import pandas as pd
import os
import matplotlib.pyplot as plt

ROOT_PATH = os.getcwd().split('lab-experimentacao-software-02/scripts')[0].replace('\\', '/')

def get_data(javaRepositories):
        
    avg_cbo = javaRepositories['Média CBO']
    dit_max = javaRepositories['DIT Max']
    avg_lcom = javaRepositories['Média LCOM']
    stargazers_count = javaRepositories['Estrelas']
    years = javaRepositories['Anos']
    num_releases = javaRepositories['Nº Releases']
    loc = javaRepositories['LOC']

    return avg_cbo, dit_max, avg_lcom, stargazers_count, years, num_releases, loc

def plot_scatter(x_values, y_values, x_label='', y_label='', title='', x_limit=None, y_limit=None):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values)
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.title(title)
    
    if x_limit is not None:
        plt.xlim(x_limit)
    
    if y_limit is not None:
        plt.ylim(y_limit)
    
    plt.grid(True)
    
    plt.show()

def main():
    javaRepositories = pd.read_csv(f'{ROOT_PATH}/scripts/dataset/csv/data.csv')
        
    avg_cbo, dit_max, avg_lcom, stargazers_count, years, num_releases, loc = get_data(javaRepositories)
    
    # Popularidade
    plot_scatter(avg_cbo, stargazers_count, 'Média CBO', 'Número de Estrelas', 'Relação entre CBO e o número de estrelas', x_limit=(0,14))
    plot_scatter(dit_max, stargazers_count, 'DIT Máx', 'Número de Estrelas', 'Relação entre DIT e o número de estrelas', x_limit=(0,100))
    plot_scatter(avg_lcom, stargazers_count, 'Média LCOM', 'Número de Estrelas', 'Relação entre LCOM e o número de estrelas', x_limit=(0,200))
    
    # Maturidade
    plot_scatter(avg_cbo, years, 'Média CBO', 'Anos', 'Relação entre CBO e Maturidade', x_limit=(0,14))
    plot_scatter(dit_max, years, 'DIT Máx', 'Anos', 'Relação entre DIT e Maturidade', x_limit=(0,100))
    plot_scatter(avg_lcom, years, 'Média LCOM', 'Anos', 'Relação entre LCOM e Maturidade', x_limit=(0,100))
    
    # Atividade
    plot_scatter(avg_cbo, num_releases, 'Média CBO', 'Número de Releases', 'Relação entre CBO e o número de Releases', x_limit=(0,14))
    plot_scatter(dit_max, num_releases, 'DIT Máx', 'Número de Releases', 'Relação entre DIT e o número de Releases', x_limit=(0,100))
    plot_scatter(avg_lcom, num_releases, 'Média LCOM', 'Número de Releases', 'Relação entre LCOM e o número de Releases', x_limit=(0,100))
    
    # Tamanho
    plot_scatter(avg_cbo, loc, 'Média CBO', 'LOC', 'Relação entre CBO e LOC', x_limit=(0,14))
    plot_scatter(dit_max, loc, 'DIT Máx', 'LOC', 'Relação entre DIT e LOC', x_limit=(0,100), y_limit=(0,1000000))
    plot_scatter(avg_lcom, loc, 'Média LCOM', 'LOC', 'Relação entre LCOM e LOC', x_limit=(0,200), y_limit=(0,2500000))
    
if __name__ == "__main__":
    main()
