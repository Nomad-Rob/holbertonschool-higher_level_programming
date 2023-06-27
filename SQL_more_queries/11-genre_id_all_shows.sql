-- Show TV shows in alphabetical order with genre data!
SELECT tv_shows.title, tv_show_genres.genre_id FROM (tv_show_genres RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id or NULL) ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
