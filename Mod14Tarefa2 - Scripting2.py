#!/usr/bin/env python
# coding: utf-8

# ## Modulo 14 - Tarefa 02 - Scripting
# • Crie um script que receba uma lista de abreviaturas de meses (MAR, ABR, MAI, JUN, etc) como argumento e gera as pastas e graficos necessarios para os meses de referência.

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

def plota_pt(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15,5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15,5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15,5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
  
raiz = '/Users/tsumano/Documents/Cursos/EBAC/Cientista de Dados/Modulo_14'
output_dir = f'{raiz}/output/figs'

meses = sys.argv[1:]

for mes in meses:
    sinasc = pd.read_csv(f'{raiz}/input/SINASC_RO_2019_{mes}.csv')
       
    max_data = sinasc.DTNASC.max()[:7]
    os.makedirs(f'{output_dir}/{max_data}', exist_ok=True)
    
    plota_pt(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')
    plt.savefig(f'{output_dir}/{max_data}/media_idade_mae_por_data.png')
    
    plota_pt(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
    plt.savefig(f'{output_dir}/{max_data}/media idade mae por sexo.png')

    plota_pt(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
    plt.savefig(f'{output_dir}/{max_data}/media peso bebe por sexo.png')

    plota_pt(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano','escolaridade mae','sort')
    plt.savefig(f'{output_dir}/{max_data}/PESO mediano por escolaridade mae.png')

    plota_pt(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
    plt.savefig(f'{output_dir}/{max_data}/media apgar1 por gestacao.png')


# In[ ]:




