.read data.sql

CREATE TABLE bluedog AS
SELECT
  color AS color, pet AS pet
FROM
  students
WHERE
  color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
SELECT
  color AS color, pet AS pet, song AS song
FROM
  students
WHERE
  color = 'blue' AND pet = 'dog';

CREATE TABLE matchmaker AS
SELECT
  first.pet AS pet, first.song AS song,
  first.color AS first_color, second.color AS second_color
FROM
  students AS first, students AS second
WHERE
  first.pet = second.pet AND
  first.song = second.song AND
  first.time < second.time;

CREATE TABLE sevens AS
SELECT
  students.seven AS seven
FROM
  students, numbers
WHERE
  students.number = 7 AND
  numbers.time = students.time AND
  numbers.'7' = 'True';

CREATE TABLE favpets AS
SELECT
  pet AS pet, COUNT(*) AS count
FROM
  students
GROUP BY
  pet
ORDER BY
  count DESC 
LIMIT
  10;

CREATE TABLE dog AS
SELECT
  pet AS pet, COUNT(*) AS count
FROM
  students
WHERE
  pet = 'dog'
GROUP BY
  pet;

CREATE TABLE bluedog_agg AS
SELECT
  song as song, COUNT(*) as count
FROM
  bluedog_songs
GROUP BY
  song
ORDER BY
  count DESC;

CREATE TABLE instructor_obedience AS
SELECT
  seven AS seven, instructor AS instructor, COUNT(*) AS count
FROM
  students
WHERE
  seven = '7'
GROUP BY
  instructor
ORDER BY
  instructor;