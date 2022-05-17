/*
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
*/

SELECT distinct(CITY) FROM STATION 
WHERE lower(SUBSTR(CITY,1,1)) in ('a','e','i','o','u')
AND lower(SUBSTR(CITY,-1,1)) in ('a','e','i','o','u');

# lower() : lower-case
# SUBSTR(Col, start at position x, y number of character) : Select 'y' number of character from position 'x' at 'col' 
