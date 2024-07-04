# Projeto de Analise de Demissoes e Ativos com Python 
Este projeto contém dois scripts que realizam a análise de dados de demissões e funcionários ativos utilizando a biblioteca `pandas`. 

## Script 1: Análise de Funcionários Ativos e Demitidos por Mês

Este script carrega dados de duas abas de uma planilha do Excel para analisar o número de funcionários ativos e demitidos por mês no ano de 2024.

### Funcionalidades

1. **Carregamento de Dados:**
   - Carrega as abas "Ativos" e "Desligados" da planilha `planilha.xlsx`.
   - Converte as colunas de datas para o formato correto (dia/mês/ano).

2. **Definição do Período de Análise:**
   - Define os meses de janeiro a junho para análise.

3. **Filtragem de Demissões por Mês:**
   - Filtra e conta o número de demissões por mês no ano de 2024.

4. **Filtragem de Ativos por Mês:**
   - Conta o número de funcionários ativos no início de cada mês considerando as admissões e demissões.

5. **Exibição dos Resultados:**
   - Exibe o número de demissões por mês.
   - Exibe o número de funcionários ativos por mês.

## Script 2: Análise de Tipos de Desligamento em uma Aba Específica
Este script carrega dados de uma aba específica de uma planilha do Excel e analisa os tipos de desligamento (involuntário e voluntário) ocorridos em junho.

### Funcionalidades

1. **Carregamento de Dados:**
   - Carrega a aba "DESLIGUES JUNHO" da planilha `DESLIGAMENTOS 06.24.xlsx`.

2. **Verificação de Coluna:**
   - Verifica se a coluna 'TIPO DE DESLIGAMENTO' está presente na aba.

3. **Definição dos Tipos de Desligamento:**
   - Define os tipos de desligamento involuntários e voluntários.

4. **Contagem de Desligamentos:**
   - Conta o número de desligamentos involuntários e voluntários.

5. **Exibição dos Resultados:**
   - Exibe o número de demissões involuntárias e voluntárias.

## Requisitos

- Python 3.x
- Pandas

## Como Executar

1. Certifique-se de ter o Python e a biblioteca `pandas` instalados:
   ```bash
   pip install pandas

2. Execute os scripts em seu ambiente Python preferido, ajustando os caminhos dos arquivos conforme necessário.


Este projeto oferece uma análise detalhada de dados de funcionários, proporcionando uma visão clara dos movimentos de pessoal ao longo do tempo.
