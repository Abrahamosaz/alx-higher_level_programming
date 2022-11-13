-- LEFT JOIN on tv_show and tv_show_genres table of the database
SELECT tv_s.title, tv_gen.genre_id FROM tv_shows as tv_s
LEFT JOIN tv_show_genres as tv_gen
ON tv_s.id = tv_gen.show_id
ORDER BY tv_s.title, tv_gen.genre_id;
