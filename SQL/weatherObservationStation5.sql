/*
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/

SELECT CITY, length(CITY) FROM STATION ORDER BY length(CITY) asc, CITY limit 1;
SELECT CITY, length(CITY) FROM STATION ORDER BY length(CITY) desc, CITY limit 1;
