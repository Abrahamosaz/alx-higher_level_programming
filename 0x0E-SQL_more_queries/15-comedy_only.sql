-- list all the comedy show in the database
SELECT title FROM tv_genres as tv_gen
INNER JOIN tv_show_genres as tv_show_gen
ON tv_gen.id = tv_show_gen.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_gen.show_id 
WHERE name="Comedy"
ORDER BY title;
