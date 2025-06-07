import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_excel("base de dados pas.xlsx", sheet_name="anatel_bandalarga_capitais")

# Filtrar para a Região Sudeste
sudeste_df = df[df['nome_regiao'] == 'Sudeste'].copy()
sudeste_df = sudeste_df.dropna(subset=['acessos'])

# Configurar estilo de gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Gráfico 1: Distribuição de acessos por estado
plt.figure()
acessos_estado = sudeste_df.groupby('sigla_uf')['acessos'].sum().sort_values(ascending=False)
sns.barplot(x=acessos_estado.index, y=acessos_estado.values, palette="Blues_d")
plt.title("Distribuição de Acessos por Estado (Sudeste)")
plt.xlabel("Estado")
plt.ylabel("Total de Acessos")
plt.tight_layout()
plt.savefig("grafico_1_acessos_estado.png")
plt.show()

# Gráfico 2: Evolução de acessos ao longo dos anos
plt.figure()
acessos_ano = sudeste_df.groupby('ano')['acessos'].sum()
sns.lineplot(x=acessos_ano.index, y=acessos_ano.values, marker='o')
plt.title("Evolução dos Acessos por Ano (Sudeste)")
plt.xlabel("Ano")
plt.ylabel("Total de Acessos")
plt.tight_layout()
plt.savefig("grafico_2_evolucao_ano.png")
plt.show()

# Gráfico 3: Empresas com maior número de acessos por porte
plt.figure()
empresa_porte = sudeste_df.groupby(['nome_empresa', 'porte_empresa'])['acessos'].sum().reset_index()
top_empresas = empresa_porte.sort_values(by='acessos', ascending=False).head(10)
sns.barplot(x='acessos', y='nome_empresa', hue='porte_empresa', data=top_empresas)
plt.title("Top 10 Empresas por Acessos e Porte")
plt.xlabel("Total de Acessos")
plt.ylabel("Empresa")
plt.tight_layout()
plt.savefig("grafico_3_empresas_porte.png")
plt.show()

# Gráfico 4: Evolução do porte das empresas ao longo dos anos
plt.figure()
porte_ano = sudeste_df.groupby(['ano', 'porte_empresa'])['acessos'].sum().reset_index()
sns.lineplot(data=porte_ano, x='ano', y='acessos', hue='porte_empresa', marker='o')
plt.title("Evolução dos Acessos por Porte de Empresa")
plt.xlabel("Ano")
plt.ylabel("Total de Acessos")
plt.tight_layout()
plt.savefig("grafico_4_porte_ano.png")
plt.show()

# Gráfico 5: Perfil atual (ano mais recente)
ano_max = sudeste_df['ano'].max()
atual_df = sudeste_df[sudeste_df['ano'] == ano_max]

plt.figure()
atual_por_porte = atual_df.groupby('porte_empresa')['acessos'].sum().reset_index()
sns.barplot(data=atual_por_porte, x='porte_empresa', y='acessos', palette='muted')
plt.title(f"Distribuição de Acessos por Porte – Ano {ano_max}")
plt.xlabel("Porte da Empresa")
plt.ylabel("Total de Acessos")
plt.tight_layout()
plt.savefig("grafico_5_perfil_atual.png")
plt.show()
