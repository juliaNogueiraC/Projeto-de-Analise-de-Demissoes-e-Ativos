import pandas as pd
import matplotlib.pyplot as plt

# Carregar a planilha
caminho_planilha = 'Entrevistas de desligamento.xlsx'  # Ajuste para o caminho correto do arquivo
df = pd.read_excel(caminho_planilha, sheet_name='Sheet2', engine='openpyxl')

# Verificar se a coluna "MOTIVO DO DESLIGAMENTO" existe na planilha
if 'MOTIVO DO DESLIGAMENTO' not in df.columns:
    raise KeyError("'MOTIVO DO DESLIGAMENTO' não encontrado na aba 'Sheet2'")

# Remover espaços em branco antes e depois dos valores na coluna "MOTIVO DO DESLIGAMENTO"
df['MOTIVO DO DESLIGAMENTO'] = df['MOTIVO DO DESLIGAMENTO'].str.strip()

# Contar a quantidade de desligamentos por motivo
contagem_motivos = df['MOTIVO DO DESLIGAMENTO'].value_counts()

# Calcular porcentagens
porcentagens = (contagem_motivos / contagem_motivos.sum()) * 100

# Ordenar porcentagens em ordem decrescente
porcentagens = porcentagens.sort_values(ascending=True)

# Criar gráfico de barras horizontais
plt.figure(figsize=(10, 8))
bars = plt.barh(porcentagens.index, porcentagens.values, color=plt.cm.Paired.colors)

# Adicionar porcentagens ao lado das barras
for bar in bars:
    xval = bar.get_width()
    plt.text(xval, bar.get_y() + bar.get_height()/2, f'{xval:.2f}%', va='center', ha='left', fontsize=10, color='black')

plt.title('Ranking de Motivos de Desligamento', fontsize=16)
plt.xlabel('Porcentagem (%)', fontsize=14)
plt.ylabel('Motivo do Desligamento', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Mostrar gráfico
plt.show()
