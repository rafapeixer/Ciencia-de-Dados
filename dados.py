import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo Excel
df_nvda = pd.read_excel('NVDA.xlsx')

# Visualizar as primeiras linhas do dataframe
print(df_nvda.head())

# Resumo estatístico
resumo_estatistico_nvda = df_nvda.describe()
print(resumo_estatistico_nvda)

# Configurações do Seaborn
sns.set(style="whitegrid")

# Gráfico de linhas do preço de fechamento da NVDA ao longo do tempo
plt.figure(figsize=(14, 7))
sns.lineplot(x='Date', y='Close', data=df_nvda)
plt.title('Preço de Fechamento da NVDA ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento (USD)')
plt.xticks(rotation=45)
plt.show()

# Distribuição dos preços de fechamento
plt.figure(figsize=(10, 6))
sns.histplot(df_nvda['Close'], kde=True)
plt.title('Distribuição dos Preços de Fechamento da NVDA')
plt.xlabel('Preço de Fechamento (USD)')
plt.ylabel('Frequência')
plt.show()

# Boxplot dos preços de fechamento
plt.figure(figsize=(10, 6))
sns.boxplot(y='Close', data=df_nvda)
plt.title('Boxplot dos Preços de Fechamento da NVDA')
plt.ylabel('Preço de Fechamento (USD)')
plt.show()

# Matriz de correlação
plt.figure(figsize=(10, 6))
correlation_matrix = df_nvda.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Converter a coluna 'Date' para o tipo datetime
df_nvda['Date'] = pd.to_datetime(df_nvda['Date'])

# Adicionar uma coluna para o número de dias desde o início dos dados
df_nvda['Days'] = (df_nvda['Date'] - df_nvda['Date'].min()).dt.days

# Calcular a correlação entre 'Days' e 'Close'
correlacao_nvda = df_nvda['Days'].corr(df_nvda['Close'])
print(f"Correlação entre número de dias e preço de fechamento: {correlacao_nvda}")

# Calcular o desvio padrão dos preços de fechamento
desvio_padrao_nvda = df_nvda['Close'].std()
print(f"Desvio padrão dos preços de fechamento: {desvio_padrao_nvda}")

# Interpretar a AED
interpretacao_aed = """
Interpretação da AED:
- O gráfico de linhas mostra as flutuações dos preços de fechamento da NVDA ao longo do tempo.
- O histograma mostra a distribuição dos preços de fechamento, indicando a frequência de diferentes intervalos de preços.
- O boxplot mostra a dispersão dos preços de fechamento e possíveis outliers.
- A matriz de correlação revela a relação entre diferentes variáveis no conjunto de dados.
- A correlação positiva sugere uma tendência de aumento dos preços ao longo do tempo.
- O alto desvio padrão indica que os preços da NVDA são altamente variáveis, confirmando a hipótese de alta volatilidade.
"""

print(interpretacao_aed)

# Levantamento e Interpretação de Duas Hipóteses
hipoteses = """
Hipótese 1: Existe uma tendência de aumento no preço da NVDA ao longo do tempo.
- A correlação positiva entre o número de dias e o preço de fechamento suporta esta hipótese.

Hipótese 2: A variabilidade do preço da NVDA é alta, indicando um mercado volátil.
- O alto desvio padrão dos preços de fechamento suporta esta hipótese.
"""

print(hipoteses)

# Salvar as estatísticas e interpretações em um arquivo de texto
with open('analise_nvda.txt', 'w') as f:
    f.write(resumo_estatistico_nvda.to_string())
    f.write('\n\n')
    f.write(interpretacao_aed)
    f.write('\n\n')
    f.write(hipoteses)

# Para converter o notebook para PDF, use o comando:
# jupyter nbconvert --to pdf nome_do_arquivo_notebook.ipynb
