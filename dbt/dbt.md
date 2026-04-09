# dbt

## O que é
o dbt é uma ferramenta de transformação analítica que combina SQL, Jinja, testes, documentação e lineage para tornar pipelines de dados mais organizadas, rastreáveis e fáceis de manter

## Como funciona
O dbt não extrai dados da origem. Ele atua sobre dados que já foram carregados no data lake, data warehouse ou lakehouse.

A lógica é construída a partir de modelos, normalmente escritos em SQL, que podem representar tabelas ou views. Esses modelos se relacionam entre si, formando uma DAG de dependências. O dbt compila os arquivos SQL com Jinja, resolve referências entre modelos e executa as transformações no engine de destino.

## Principais recursos
- criação de modelos SQL reutilizáveis
- uso de Jinja para parametrização, macros e reaproveitamento de lógica
- materializações como view, table, incremental e ephemeral
- testes de qualidade de dados
- documentação automática
- geração de lineage entre modelos
- integração com versionamento em Git
- separação por camadas, como staging, intermediate e marts

## Papel na arquitetura
Dentro da arquitetura proposta neste desafio, o dbt se encaixa principalmente nas camadas **Standardized** e **Aggregated**.

Na prática, ele pode ser usado para:
- padronizar dados vindos da camada Raw
- aplicar regras de negócio
- consolidar entidades analíticas
- construir tabelas finais para consumo por BI, reporting ou outras aplicações
