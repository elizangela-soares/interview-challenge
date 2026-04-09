# Desafio Técnico

## Escopo
O desafio contempla:
- desenho de uma pipeline em Airflow para ingestão diária de transações
- consultas SQL sobre dados de sensores de refinaria
- implementação em Spark para as mesmas questões SQL
- script Bash para housekeeping
- explicação sobre dbt
- extração horária em Python a partir de uma base proprietária via ODBC

## Organização do repositório
Este projeto será organizado em pastas separadas para cada tema do desafio:
- airflow/
- sql/
- spark/
- bash/
- dbt/
- python_extraction/
- docs/

## Premissas
- Como não foi disponibilizado acesso à infraestrutura ou à base de dados real, as configurações de conexão e os caminhos de armazenamento foram parametrizados ou representados apenas como exemplo.
- O data lake foi considerado com as seguintes camadas lógicas:
  - Raw
  - Standardized
  - Aggregated
- As janelas de extração utilizam intervalo semiaberto: (start_timestamp, end_timestamp).

## Observações
- A solução de Airflow foi estruturada para execução com Docker, conforme solicitado no enunciado.
- O repositório foi organizado para versionamento e entrega via Git