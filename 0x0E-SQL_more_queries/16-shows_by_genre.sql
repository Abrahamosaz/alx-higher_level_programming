SELECT title, name FROM tv_show_genres as tv_gen
RIGHT JOIN tv_shows ON tv_gen.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_genres.id = tv_gen.genre_id
ORDER BY title, name;
