# Arquitetura da Solução

## Visão geral
A solução foi organizada considerando as camadas do data lake:
- Raw
- Standardized
- Aggregated

## Airflow
O Airflow será responsável pela ingestão diária das transações da loja de Nova York:
1. Ler no MySQL apenas os dados do dia anterior
2. Gravar os dados na camada Raw
3. Padronizar os dados na camada Standardized

## NiFi
O NiFi será responsável por consultar a API REST de câmbio USD/EUR e disponibilizar esse dado no data lake.

## Python Extraction
A extração horária via ODBC será feita em paralelo por lotes de sensores, gerando arquivos Parquet por janela de uma hora.

## SQL e Spark
As análises pedidas no desafio serão entregues tanto em SQL quanto em Spark.