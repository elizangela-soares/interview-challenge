-- 1. Total number of rows
SELECT COUNT(*) AS total_rows
FROM sensor_readings;

-- 2. Number of distinct sensors present on the database
SELECT COUNT(DISTINCT name) AS distinct_sensors
FROM sensor_readings;

-- 3. Number of rows for the sensor PPL340
SELECT COUNT(*) AS ppl340_rows
FROM sensor_readings
WHERE name = 'PPL340';

-- 4. Number of rows by year for the sensor PPL340
SELECT
    year,
    COUNT(*) AS rows_per_year
FROM sensor_readings
WHERE name = 'PPL340'
GROUP BY year
ORDER BY year;

-- 5. Average number of readings by year for the sensor PPL340
WITH yearly_counts AS (
    SELECT
        year,
        COUNT(*) AS yearly_count
    FROM sensor_readings
    WHERE name = 'PPL340'
    GROUP BY year
)
SELECT AVG(yearly_count) AS avg_readings_per_year
FROM yearly_counts;

-- 6. Years in which the number of readings is less than the average
WITH yearly_counts AS (
    SELECT
        year,
        COUNT(*) AS yearly_count
    FROM sensor_readings
    WHERE name = 'PPL340'
    GROUP BY year
),
average_counts AS (
    SELECT AVG(yearly_count) AS avg_yearly_count
    FROM yearly_counts
)
SELECT
    y.year,
    y.yearly_count
FROM yearly_counts y
CROSS JOIN average_counts a
WHERE y.yearly_count < a.avg_yearly_count
ORDER BY y.year;