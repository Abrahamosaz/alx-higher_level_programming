-- display the number of score and row record in desc order
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
