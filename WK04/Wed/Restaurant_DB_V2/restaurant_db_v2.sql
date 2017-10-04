--  Creating Tables

--  restaurant table
CREATE TABLE restaurant (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	address VARCHAR,
	category VARCHAR
);

--  reviewer TABLE
CREATE TABLE reviewer (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	email VARCHAR,
	karma INTEGER CHECK (0 <= karma AND karma <= 7)
);

--  review table
CREATE TABLE review (
	id SERIAL PRIMARY KEY,
  reviewer_id INTEGER REFERENCES reviewer (id),
  stars INTEGER CHECK (1 <= stars AND stars <= 5),
  title VARCHAR,
	review_text VARCHAR,
	restaurant_id INTEGER REFERENCES restaurant (id)
);


--	Create these table schemas by loading this file. For example,
--	psql restaurant -f restaurant.sql
--	This command assumes database is called restaurant
--	and file is called restaurant.sql
