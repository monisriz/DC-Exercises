-- PostgreSQL Exercises

-- Creating table in Restaurant database
CREATE TABLE restaurant (
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR NOT NULL,
	dist NUMERIC NOT NULL,
	stars INTEGER DEFAULT 0 CHECK (0 <= stars AND stars <= 5),
	favdish VARCHAR,
	category VARCHAR,
	takeout BOOLEAN DEFAULT FALSE,
	lastvisit DATE
	);


-- Inserting data into the table

INSERT INTO restaurant (name, dist, stars, favdish, category, takeout, lastvisit) VALUES ('Champ Burger', 0.1, 4, 'Champ Burger w/ mushrooms', 'Fast food', True, '2017-09-27');
--
INSERT INTO restaurant (name, dist, stars, favdish, category, takeout, lastvisit) VALUES ('Moon Tower', 0.1, 3, NULL, 'Fast food', FALSE, '2017-09-20');
--
INSERT INTO restaurant (name, dist, stars, favdish, category, takeout, lastvisit) VALUES ('Chick-fil-A', 3.2, 5, 'Spicy Sandwich w Pepperjack cheese', 'Fast food', True, '2017-10-02');
--
INSERT INTO restaurant (name, dist, stars, favdish, category, takeout, lastvisit) VALUES ('Pappadeaux', 6.7, 5, 'Pappadeaux Seafood Platter', 'Seafood', True, '2017-07-20');
--
INSERT INTO restaurant (name, dist, stars, favdish, category, takeout, lastvisit) VALUES ('Pappasitos', 4.6, 4, NULL, 'Mexican', True, '2017-07-20');
--
INSERT INTO restaurant (name, dist, stars, favdish, category, takeout, lastvisit) VALUES ('Bundu Khan', 15, 4, 'Chicken Tikka', 'BBQ', True, '2017-09-12');
--


-- Writing Queries

-- 	1.	The names of the restaurants that you gave a 5 stars to

SELECT name FROM restaurant WHERE stars=5;

-- 	2.	The favorite dishes of all 5-star restaurants

SELECT name, favdish FROM restaurant WHERE stars=5;

--  3.	The the id of a restaurant by a specific restaurant name, say 'Moon Tower'

SELECT id FROM restaurant WHERE name='Moon Tower';

--  4.	Restaurants in the category of 'BBQ'

SELECT name FROM restaurant WHERE category='BBQ';

--  5.	Restaurants that do take out

SELECT name FROM restaurant WHERE takeout=TRUE;

--  6.	Restaurants that do take out and is in the category of 'BBQ'

SELECT name FROM restaurant WHERE takeout=TRUE AND category='BBQ';

--  7.	Restaurants within 2 miles

SELECT name FROM restaurant WHERE dist < 2;

--  8.	Restaurants you haven't ate at in the last week

SELECT name FROM restaurant WHERE lastvisit < '2017-09-26';

--  9.	Restaurants you haven't ate at in the last week and has 5 stars

SELECT name FROM restaurant WHERE lastvisit < '2017-09-26' AND stars=5;


-- Aggregation and Sorting Queries

--  1.	List restaurants by the closest distance

SELECT name FROM restaurant ORDER BY dist;

--  2.	List the top 2 restaurants by distance

SELECT name FROM restaurant ORDER BY dist LIMIT 2;

--  3.	List the top 2 restaurants by stars

SELECT name FROM restaurant ORDER by stars desc LIMIT 2;

--  4.	List the top 2 restaurants by stars where the distance is less than 2 miles

SELECT name FROM restaurant WHERE dist < 2 ORDER BY stars DESC;

--  5.	Count the number of restaurants in the db

SELECT COUNT(*) FROM restaurant;

--  6.	Count the number of restaurants by category

SELECT category, COUNT(*) FROM restaurant GROUP BY category;

--  7.	Get the average stars per restaurant by category

SELECT category, AVG(stars) FROM restaurant GROUP BY category;

--  8.	Get the max stars of a restaurant by category

SELECT category, MAX(stars) FROM restaurant GROUP BY category;
