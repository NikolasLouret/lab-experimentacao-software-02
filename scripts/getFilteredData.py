import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

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

def plot_correlation_matrix(data, title):
    plt.figure(figsize=(10, 6))
    plt.matshow(data.corr(), cmap='coolwarm', fignum=1)
    plt.colorbar()
    plt.xticks(range(data.shape[1]), data.columns, rotation=45)
    plt.yticks(range(data.shape[1]), data.columns)
    plt.title(title)
    plt.show()

def calculate_pearson_correlation(x_values, y_values):
    valid_indices = np.isfinite(x_values) & np.isfinite(y_values)
    x_values_filtered = x_values[valid_indices]
    y_values_filtered = y_values[valid_indices]
    
    correlation_coefficient, _ = pearsonr(x_values_filtered, y_values_filtered)
    
    correlation_coefficient = round(correlation_coefficient, 3)

    return correlation_coefficient

def main():
    javaRepositories = pd.read_csv(f'{ROOT_PATH}/scripts/dataset/csv/data.csv')
        
    avg_cbo, dit_max, avg_lcom, stargazers_count, years, num_releases, loc = get_data(javaRepositories)

    print("\nSe o valor for próximo de 1, indica uma correlação positiva forte (à medida que uma variável aumenta, a outra também aumenta na mesma proporção)")
    print("Se o valor for próximo de -1, indica uma correlação negativa forte (à medida que uma variável aumenta, a outra diminui na mesma proporção)")
    print("Se o valor for próximo de 0, indica que não há correlação entre as variáveis")
    
    # Popularidade
    plot_scatter(avg_cbo, stargazers_count, 'Média CBO', 'Número de Estrelas', 'Relação entre CBO e o número de estrelas', x_limit=(0,14))
    plot_scatter(dit_max, stargazers_count, 'DIT Máx', 'Número de Estrelas', 'Relação entre DIT e o número de estrelas', x_limit=(0,100))
    plot_scatter(avg_lcom, stargazers_count, 'Média LCOM', 'Número de Estrelas', 'Relação entre LCOM e o número de estrelas', x_limit=(0,200))
    data_rq1 = javaRepositories[['Média CBO', 'DIT Max', 'Média LCOM', 'Estrelas']]
    plot_correlation_matrix(data_rq1, 'Matriz de Correlação Popularidade')
    
    # Pearson 
    pearson_corr_cbo_stargazers = calculate_pearson_correlation(avg_cbo, stargazers_count)
    pearson_corr_dit_stargazers = calculate_pearson_correlation(dit_max, stargazers_count)
    pearson_corr_lcom_stargazers = calculate_pearson_correlation(avg_lcom, stargazers_count)
    
    print("\nCorrelação de Pearson entre Média CBO e Número de Estrelas:", pearson_corr_cbo_stargazers)
    print("Correlação de Pearson entre DIT Máx e Número de Estrelas:", pearson_corr_dit_stargazers)
    print("Correlação de Pearson entre Média LCOM e Número de Estrelas:", pearson_corr_lcom_stargazers)

    # Maturidade
    plot_scatter(avg_cbo, years, 'Média CBO', 'Anos', 'Relação entre CBO e Maturidade', x_limit=(0,14))
    plot_scatter(dit_max, years, 'DIT Máx', 'Anos', 'Relação entre DIT e Maturidade', x_limit=(0,100))
    plot_scatter(avg_lcom, years, 'Média LCOM', 'Anos', 'Relação entre LCOM e Maturidade', x_limit=(0,100))
    data_rq2 = javaRepositories[['Média CBO', 'DIT Max', 'Média LCOM', 'Anos']]
    plot_correlation_matrix(data_rq2, 'Matriz de Correlação Maturidade')
    
    # Pearson 
    pearson_corr_cbo_years = calculate_pearson_correlation(avg_cbo, years)
    pearson_corr_dit_years = calculate_pearson_correlation(dit_max, years)
    pearson_corr_lcom_years = calculate_pearson_correlation(avg_lcom, years)
    
    print("\nCorrelação de Pearson entre Média CBO e Anos:", pearson_corr_cbo_years)
    print("Correlação de Pearson entre DIT Máx e Anos:", pearson_corr_dit_years)
    print("Correlação de Pearson entre Média LCOM e Anos:", pearson_corr_lcom_years)

    # Atividade
    plot_scatter(avg_cbo, num_releases, 'Média CBO', 'Número de Releases', 'Relação entre CBO e o número de Releases', x_limit=(0,14))
    plot_scatter(dit_max, num_releases, 'DIT Máx', 'Número de Releases', 'Relação entre DIT e o número de Releases', x_limit=(0,100))
    plot_scatter(avg_lcom, num_releases, 'Média LCOM', 'Número de Releases', 'Relação entre LCOM e o número de Releases', x_limit=(0,100))
    data_rq3 = javaRepositories[['Média CBO', 'DIT Max', 'Média LCOM', 'Nº Releases']]
    plot_correlation_matrix(data_rq3, 'Matriz de Correlação Atividade')
    
    # Pearson 
    pearson_corr_cbo_releases = calculate_pearson_correlation(avg_cbo, num_releases)
    pearson_corr_dit_releases = calculate_pearson_correlation(dit_max, num_releases)
    pearson_corr_lcom_releases = calculate_pearson_correlation(avg_lcom, num_releases)
    
    print("\nCorrelação de Pearson entre Média CBO e Número de Releases:", pearson_corr_cbo_releases)
    print("Correlação de Pearson entre DIT Máx e Número de Releases:", pearson_corr_dit_releases)
    print("Correlação de Pearson entre Média LCOM e Número de Releases:", pearson_corr_lcom_releases)

    # Tamanho
    plot_scatter(avg_cbo, loc, 'Média CBO', 'LOC', 'Relação entre CBO e LOC', x_limit=(0,14))
    plot_scatter(dit_max, loc, 'DIT Máx', 'LOC', 'Relação entre DIT e LOC', x_limit=(0,100), y_limit=(0,1000000))
    plot_scatter(avg_lcom, loc, 'Média LCOM', 'LOC', 'Relação entre LCOM e LOC', x_limit=(0,200), y_limit=(0,2500000))
    data_rq4 = javaRepositories[['Média CBO', 'DIT Max', 'Média LCOM', 'LOC']]
    plot_correlation_matrix(data_rq4, 'Matriz de Correlação Tamanho')
    
    # Pearson 
    pearson_corr_cbo_loc = calculate_pearson_correlation(avg_cbo, loc)
    pearson_corr_dit_loc = calculate_pearson_correlation(dit_max, loc)
    pearson_corr_lcom_loc = calculate_pearson_correlation(avg_lcom, loc)
    
    print("\nCorrelação de Pearson entre Média CBO e LOC:", pearson_corr_cbo_loc)
    print("Correlação de Pearson entre DIT Máx e LOC:", pearson_corr_dit_loc)
    print("Correlação de Pearson entre Média LCOM e LOC:", pearson_corr_lcom_loc)
    
if __name__ == "__main__":
    main()
