import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import pandas as pd
import pyodbc
import yaml

from utils import build_output_dir, chunk_list


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_connection(connection_string):
    return pyodbc.connect(connection_string)


def get_all_sensors(connection_string, source_table):
    query = f"SELECT DISTINCT sensor_name FROM {source_table}"

    with get_connection(connection_string) as conn:
        df = pd.read_sql(query, conn)

    return df["sensor_name"].dropna().astype(str).tolist()


def extract_sensor_batch(
    connection_string,
    source_table,
    sensor_batch,
    start_ts,
    end_ts,
    part_number,
    output_dir,
):
    placeholders = ",".join(["?"] * len(sensor_batch))

    query = f"""
        SELECT timestamp, sensor_name, value
        FROM {source_table}
        WHERE sensor_name IN ({placeholders})
          AND timestamp >= ?
          AND timestamp < ?
    """

    params = sensor_batch + [start_ts, end_ts]

    with get_connection(connection_string) as conn:
        df = pd.read_sql(query, conn, params=params)

    output_file = output_dir / f"part_{part_number:04d}.parquet"
    df.to_parquet(output_file, index=False)

    return str(output_file), len(df)


def write_success_file(output_dir, total_rows):
    success_file = output_dir / "_SUCCESS"
    content = f"completed_at={datetime.utcnow().isoformat()}\ntotal_rows={total_rows}\n"
    success_file.write_text(content, encoding="utf-8")


def run_hourly_extraction(config_path, start_ts, end_ts):
    config = load_config(config_path)

    connection_string = os.getenv("ODBC_CONNECTION_STRING")
    if not connection_string:
        raise ValueError("Environment variable ODBC_CONNECTION_STRING was not set.")

    source_table = config["source_table"]
    output_base_path = config["output_base_path"]
    batch_size = int(config["batch_size"])
    max_workers = int(config["max_workers"])

    window_start = datetime.strptime(start_ts, "%Y-%m-%d %H:%M:%S")
    output_dir = build_output_dir(
        output_base_path,
        window_start.year,
        window_start.month,
        window_start.day,
        window_start.hour,
    )

    sensors = get_all_sensors(connection_string, source_table)

    futures = []
    total_rows = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for part_number, sensor_batch in enumerate(chunk_list(sensors, batch_size), start=1):
            future = executor.submit(
                extract_sensor_batch,
                connection_string,
                source_table,
                sensor_batch,
                start_ts,
                end_ts,
                part_number,
                output_dir,
            )
            futures.append(future)

        for future in as_completed(futures):
            output_file, row_count = future.result()
            total_rows += row_count
            print(f"Generated file: {output_file} | rows: {row_count}")

    write_success_file(output_dir, total_rows)
    print(f"Extraction finished successfully. Total rows: {total_rows}")


def main():
    config_path = "python_extraction/config_example.yaml"
    start_ts = "2020-01-01 00:00:00"
    end_ts = "2020-01-01 01:00:00"

    run_hourly_extraction(config_path, start_ts, end_ts)


if __name__ == "__main__":
    main()