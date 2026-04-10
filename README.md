# Desafio Técnico

## Escopo
Esta entrega contempla:
- proposta de pipeline em Airflow para ingestão diária de transações
- consultas SQL sobre dados de sensores de refinaria
- implementação em Spark para as mesmas questões analíticas
- observação sobre o item de Bash
- explicação sobre dbt
- proposta de extração horária em Python a partir de uma base proprietária via ODBC

## Organização do repositório
O projeto foi organizado em pastas separadas por tema:
- airflow/
- sql/
- spark/
- bash/
- dbt/
- python_extraction/
- docs/

## Premissas
- Como não foi disponibilizado acesso à infraestrutura ou à base de dados real, as configurações de conexão e os caminhos de armazenamento foram representados como exemplo.
- O data lake foi considerado com as seguintes camadas lógicas:
  - Raw
  - Standardized
  - Aggregated
- As janelas de extração utilizam intervalo semiaberto: start_timestamp, end_timestamp.

## Observações
- A parte de Airflow foi apresentada como proposta de solução, em linha com o que é solicitado no desafio.
- O item de NiFi foi tratado em nível arquitetural, uma vez que o enunciado apenas indica seu uso para obtenção da taxa de câmbio via API REST.
- O repositório foi organizado para versionamento e entrega via Git.