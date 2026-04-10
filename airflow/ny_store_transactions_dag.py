import os
from datetime import datetime, timedelta

import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    "owner": "data-eng",
    "depends_on_past": False,
    "start_date": datetime(2026, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def extract_previous_day_transactions(**context):
    execution_date = context["execution_date"]

    end_dt = execution_date.replace(hour=0, minute=0, second=0, microsecond=0)
    start_dt = end_dt - timedelta(days=1)

    print(f"Start window: {start_dt}")
    print(f"End window: {end_dt}")

    query = f"""
    SELECT
        timestamp,
        product_id,
        product_name,
        product_price,
        cliente_id
    FROM transactions
    WHERE timestamp >= '{start_dt}'
      AND timestamp < '{end_dt}'
    """

    output_dir = (
        f"./data/raw/store_transactions/store=ny/"
        f"year={start_dt.year}/month={start_dt.month:02d}/day={start_dt.day:02d}"
    )
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "transactions.parquet")

    # apenas representação saída do pipeline
    df = pd.DataFrame(
        columns=["timestamp", "product_id", "product_name", "product_price", "cliente_id"]
    )
    df.to_parquet(output_file, index=False)

    print(f"Output file generated at: {output_file}")


dag = DAG(
    dag_id="ny_store_transactions_ingestion",
    default_args=default_args,
    schedule_interval="0 1 * * *",
    catchup=True,
    max_active_runs=1,
)


extract_task = PythonOperator(
    task_id="extract_previous_day_transactions",
    python_callable=extract_previous_day_transactions,
    provide_context=True,
    dag=dag,
)