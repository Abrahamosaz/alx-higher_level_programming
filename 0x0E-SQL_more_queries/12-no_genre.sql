-- list all shows contained in the database linked with genres
SELECT tv_s.title, tv_gen.genre_id
FROM tv_shows as tv_s
LEFT JOIN tv_show_genres as tv_gen
ON tv_s.id = tv_gen.show_id
WHERE tv_gen.genre_id IS NULL
ORDER BY tv_s.title, tv_gen.genre_id;
