-- From albums,
-- filter where id is '2',
-- and select only values for the columns id, title and release_year.
SELECT id, title, release_year
  FROM albums
  WHERE id = 2;

-- From albums,
-- filter where title is 'Doolittle',
-- and select only values for the columns id, title and release_year.

-- Make sure to always use single quotes ('')
-- to delimitate strings in conditions.
SELECT id, title, release_year
  FROM albums
  WHERE title = 'Doolittle';

-- We can use =, <, <=, >, >=
-- to compare values.

-- From albums,
-- filter where release_year is greater than 1990,
-- and select only values for the columns id, title and release_year.
SELECT id, title, release_year
  FROM albums
  WHERE release_year > 1990;

-- We can use the keywords AND and OR
-- to combine conditions.

-- From albums,
-- filter where release_year is greater than 1989 AND artist_id is '1',
-- and select only values for the columns id, title, release_year and artist_id.
SELECT id, title, release_year, artist_id
  FROM albums
  WHERE release_year > 1989 AND artist_id = 1;



-- Challenge : Insert a new artist of your choice, and a new album related to that artist (here's an idea, if you can't pick one).

INSERT INTO artists
  (name , genre)
  VALUES('Sia', 'Pop');

INSERT INTO albums
  (title, release_year, artist_id)
  VALUES ('This is Acting', '2016' , '6');
