/*
Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
*/

SELECT distinct(CITY) FROM STATION WHERE lower(SUBSTR(CITY, -1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
