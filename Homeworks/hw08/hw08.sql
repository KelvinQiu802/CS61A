CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
SELECT
  name AS name, size AS size
FROM
  dogs, sizes
WHERE
  height <= max AND min < height;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
SELECT
  d1.name
FROM
  dogs AS d1, dogs AS d2, parents
WHERE
  d1.name = child AND d2.name = parent
ORDER BY
  d2.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
SELECT
  d1.name AS ch1, d2.name AS ch2
FROM
  dogs AS d1, dogs AS d2, parents AS p1, parents AS p2
WHERE
  d1.name = p1.child AND d2.name = p2.child AND
  p1.parent = p2.parent AND d1.name != d2.name AND
  d1.name < d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
SELECT
  s1.name || ' and ' || s2.name || ' are ' || s1.size || ' siblings' 
FROM
  siblings, size_of_dogs AS s1, size_of_dogs AS s2
WHERE
  s1.name = ch1 AND s2.name = ch2 AND s1.size = s2.size;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);


CREATE TABLE stacks AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

