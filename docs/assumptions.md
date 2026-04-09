# Premissas

1. Não foi disponibilizado acesso ao ambiente real, então conexões, caminhos e nomes foram tratados como exemplos.
2. O nome da tabela de sensores foi assumido como `sensor_readings`.
3. Sempre que aplicável, o formato adotado para saída é Parquet.
4. A extração horária utiliza intervalo semiaberto: `[start_timestamp, end_timestamp)`.
5. Como a query horária completa demora mais de uma hora, a solução em Python foi desenhada com paralelismo por lotes de sensores.
6. O ambiente Airflow em Docker foi tratado como demonstração para o desafio.