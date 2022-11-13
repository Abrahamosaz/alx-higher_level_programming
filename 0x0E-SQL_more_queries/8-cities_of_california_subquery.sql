-- subquery for states and cities tables in database
SELECT id, name FROM cities WHERE state_id =
(
	SELECT id from states WHERE name = "California"
)
ORDER BY cities.id ASC;
