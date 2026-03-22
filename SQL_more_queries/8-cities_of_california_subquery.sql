-- Lists cities of California using a subquery (No JOIN)
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;

