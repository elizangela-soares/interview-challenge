from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = (
        SparkSession.builder
        .appName("sensor_analysis")
        .getOrCreate()
    )

    df = spark.table("sensor_readings")

    print("\n1. Total number of rows")
    total_rows = df.count()
    print(total_rows)

    print("\n2. Number of distinct sensors present on the database")
    distinct_sensors = df.select("name").distinct().count()
    print(distinct_sensors)

    ppl340_df = df.filter(F.col("name") == "PPL340")

    print("\n3. Number of rows for the sensor PPL340")
    ppl340_rows = ppl340_df.count()
    print(ppl340_rows)

    print("\n4. Number of rows by year for the sensor PPL340")
    rows_per_year = (
        ppl340_df
        .groupBy("year")
        .count()
        .withColumnRenamed("count", "rows_per_year")
        .orderBy("year")
    )
    rows_per_year.show()

    print("\n5. Average number of readings by year for the sensor PPL340")
    yearly_counts = (
        ppl340_df
        .groupBy("year")
        .count()
        .withColumnRenamed("count", "yearly_count")
    )

    avg_readings = yearly_counts.agg(
        F.avg("yearly_count").alias("avg_readings_per_year")
    )
    avg_readings.show()

    avg_value = avg_readings.collect()[0]["avg_readings_per_year"]

    print("\n6. Years in which the number of readings is less than the average")
    below_average = (
        yearly_counts
        .filter(F.col("yearly_count") < avg_value)
        .orderBy("year")
    )
    below_average.show()

    spark.stop()


if __name__ == "__main__":
    main()