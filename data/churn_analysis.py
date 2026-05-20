# Impotando bibliotecas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Iniciando leitura do Dataset


df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Explorando visualmente

print(df.head(10))

# Conferindo estrutura

print(df.info(20))

# Estatísticas gerais

print(df.describe())

# Calcular taxa de churn

print(df['Churn'].value_counts(normalize=True))

# Inserindo gráfico

sns.countplot(x='Churn', data=df)

plt.title('Distribuição de Churn')

plt.show()

# Comparando por contrato ainda com gráficos

sns.countplot(x='Contract', hue='Churn', data=df)

plt.xticks(rotation=15)

plt.show()

# Comprarando por valor mensal, ainda com gráficos.

sns.boxplot(x='Churn', y='MonthlyCharges', data=df)

plt.show()

# Checando tempo de permanência

sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack')

plt.show()

# Preparar ambiente para exportar para o POWER BI (a fazer)
