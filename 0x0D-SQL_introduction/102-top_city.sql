-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (july,  August) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
