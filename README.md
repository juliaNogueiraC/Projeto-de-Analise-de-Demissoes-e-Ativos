# Projeto de Análise de Demissões e Ativos com Python
Este projeto contém scripts que realizam a análise de dados de demissões e funcionários ativos utilizando a biblioteca pandas e a visualização com matplotlib.

## Funcionalidades Gerais
- Carregamento de dados de planilhas do Excel
- Conversão e manipulação de datas
- Filtragem de dados por períodos específicos
- Contagem e categorização de dados
- Exibição dos resultados de forma tabular
- Geração de gráficos para visualização de dados

## Script 1: Análise de Funcionários Ativos e Demitidos por Mês
Este script carrega dados de duas abas de uma planilha do Excel para analisar o número de funcionários ativos e demitidos por mês no ano de 2024.

### Funcionalidades
1. Carregamento de Dados:

- Carrega as abas "Ativos" e "Desligados" da planilha planilha.xlsx.
- Converte as colunas de datas para o formato correto (dia/mês/ano).
  
2. Definição do Período de Análise:

- Define os meses de janeiro a junho para análise.

3. Filtragem de Demissões por Mês:

- Filtra e conta o número de demissões por mês no ano de 2024.

4. Filtragem de Ativos por Mês:

- Conta o número de funcionários ativos no início de cada mês considerando as admissões e demissões.
  
#### Exibição dos Resultados:

- Exibe o número de demissões por mês.
- Exibe o número de funcionários ativos por mês.

## Script 2: Análise de Tipos de Desligamento
Este script carrega dados de uma aba específica de uma planilha do Excel e analisa os tipos de desligamento (involuntário e voluntário) ocorridos por mês.

### Funcionalidades
1. Carregamento de Dados:

- Carrega a aba "DESLIGUES" da planilha DESLIGAMENTOS.xlsx.
2. Verificação de Coluna:

- Verifica se a coluna 'TIPO DE DESLIGAMENTO' está presente na aba.
3. Definição dos Tipos de Desligamento:

- Define os tipos de desligamento involuntários e voluntários.
4. Contagem de Desligamentos:

- Conta o número de desligamentos involuntários e voluntários.
#### Exibição dos Resultados:

- Exibe o número de demissões involuntárias e voluntárias.

## Script 3: Análise de Dados por Gênero, Função e Centro de Custo
Este script carrega dados de uma planilha do Excel e analisa as demissões por gênero, função e centro de custo no ano de 2024. Também gera gráficos para melhor visualização dos resultados.

### Funcionalidades
1. Carregamento de Dados:

- Carrega a aba "DESLIGADOS" da planilha Cópia de lista de colaboradores ativos - julia (003).xlsx.
2. Conversão de Datas:

- Converte a coluna 'Dt. Demissao' para o tipo datetime.
3. Filtragem de Dados:

- Filtra os dados para considerar apenas as demissões ocorridas em 2024.
4. Contagem de Demissões por Gênero:

- Conta as demissões por gênero (masculino e feminino) em 2024.
5. Contagem de Demissões por Função/Cargo:

- Conta as demissões por função/cargo em 2024.
6. Contagem de Demissões por Centro de Custo:

- Conta as demissões por centro de custo em 2024.
#### Exibição dos Resultados:

- Exibe os resultados em formato tabular.
- Gera gráficos para visualizar as demissões por gênero, função/cargo e centro de custo.

## Requisitos
- Python 3.x
- Pandas
## Como Executar
Certifique-se de ter o Python e a biblioteca pandas instalados:
````
pip install pandas
````

- Execute os scripts em seu ambiente Python preferido, ajustando os caminhos dos arquivos conforme necessário.

Este projeto oferece uma análise detalhada de dados de funcionários, proporcionando uma visão clara dos movimentos de pessoal ao longo do tempo.
