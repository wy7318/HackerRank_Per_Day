/*
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
*/

SELECT distinct(CITY) FROM STATION
WHERE lower(SUBSTR(CITY, 1, 1)) NOT IN ('a', 'i', 'e', 'o', 'u')
AND lower(SUBSTR(CITY, -1, 1)) NOT IN ('a', 'i', 'e', 'o', 'u');
