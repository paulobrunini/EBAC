{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e5cfd51",
   "metadata": {},
   "source": [
    "## Modulo 14 - Tarefa 02 - Scripting\n",
    "• Crie um script que receba uma lista de abreviaturas de meses (MAR, ABR, MAI, JUN, etc) como argumento e gera as pastas e graficos necessarios para os meses de referência."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "86eae13b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import os\n",
    "import sys\n",
    "\n",
    "def plota_pt(df, value, index, func, ylabel, xlabel, opcao='nada'):\n",
    "    if opcao == 'nada':\n",
    "        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15,5])\n",
    "    elif opcao == 'unstack':\n",
    "        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15,5])\n",
    "    elif opcao == 'sort':\n",
    "        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15,5])\n",
    "    plt.ylabel(ylabel)\n",
    "    plt.xlabel(xlabel)\n",
    "  \n",
    "raiz = '/Users/tsumano/Documents/Cursos/EBAC/Cientista de Dados/Modulo_14'\n",
    "output_dir = f'{raiz}/output/figs'\n",
    "\n",
    "meses = sys.argv[1:]\n",
    "\n",
    "for mes in meses:\n",
    "    sinasc = pd.read_csv(f'{raiz}/input/SINASC_RO_2019_{mes}.csv')\n",
    "       \n",
    "    max_data = sinasc.DTNASC.max()[:7]\n",
    "    os.makedirs(f'{output_dir}/{max_data}', exist_ok=True)\n",
    "    \n",
    "    plota_pt(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')\n",
    "    plt.savefig(f'{output_dir}/{max_data}/media_idade_mae_por_data.png')\n",
    "    \n",
    "    plota_pt(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')\n",
    "    plt.savefig(f'{output_dir}/{max_data}/media idade mae por sexo.png')\n",
    "\n",
    "    plota_pt(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')\n",
    "    plt.savefig(f'{output_dir}/{max_data}/media peso bebe por sexo.png')\n",
    "\n",
    "    plota_pt(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano','escolaridade mae','sort')\n",
    "    plt.savefig(f'{output_dir}/{max_data}/PESO mediano por escolaridade mae.png')\n",
    "\n",
    "    plota_pt(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')\n",
    "    plt.savefig(f'{output_dir}/{max_data}/media apgar1 por gestacao.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "a96f4f22",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
