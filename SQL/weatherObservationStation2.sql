/*
Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of 2 decimal places.
The sum of all values in LONG_W rounded to a scale of 2 decimal places.
*/

SELECT CAST(SUM(LAT_N) as decimal(10, 2)), CAST(SUM(LONG_W) as decimal(10, 2)) FROM STATION

--- CAST(column AS format) : Convert column's data type
