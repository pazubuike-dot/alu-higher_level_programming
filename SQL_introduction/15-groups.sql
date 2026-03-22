-- Lists number of records with same score, sorted by count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

