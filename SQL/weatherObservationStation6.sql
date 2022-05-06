/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/

SELECT distinct CITY FROM STATION 
WHERE CITY LIKE 'A%' 
or CITY LIKE 'E%'
or CITY LIKE 'I%'
or CITY LIKE 'O%'
or CITY LIKE 'U%';
