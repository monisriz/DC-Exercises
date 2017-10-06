-- IMPLICIT JOINS

--  1.  List all the reviews for a given restaurant given a specific
--      restaurant ID.

SELECT restaurant.name, review.stars, review.title, review.review_text FROM review, restaurant WHERE review.restaurant_id = restaurant.id AND restaurant_id = 3;

--  2.  List all the reviews for a given restaurant, given a specific
--      restaurant name.

SELECT restaurant.name AS restaurant_name, review.stars, review.title AS review_title, review.review_text FROM review JOIN restaurant ON review.restaurant_id = restaurant.id WHERE restaurant.name = 'Pappadeaux';

--  3.  List all the reviews for a given reviewer, given a specific author name.

SELECT reviewer.name AS author_name, restaurant.name AS restaurant_name, review.stars, review.title AS review_title, review_text FROM review, restaurant, reviewer WHERE review.reviewer_id = reviewer.id AND review.restaurant_id = restaurant.id AND reviewer.name = 'Mike';

--  4.  List all the reviews along with the restaurant they were written for.
--      In the query result, select the restaurant name and the review text.

SELECT restaurant.name AS restaurant_name, review_text FROM review, restaurant, reviewer WHERE review.reviewer_id = reviewer.id AND review.restaurant_id = restaurant.id;

--  5.  Get the average stars by restaurant. The result should have the
--      restaurant name and its average star rating.

SELECT restaurant.name AS restaurant_name, AVG(review.stars) AS avg_stars FROM review, restaurant WHERE review.restaurant_id = restaurant.id GROUP BY restaurant.name ORDER BY avg_stars DESC;

--  6.  Get the number of reviews written for each restaurant. The result
--      should have the restaurant name and its review count.

SELECT restaurant.name AS restaurant_name, COUNT(review.restaurant_id) AS review_count FROM restaurant, review WHERE restaurant.id = review.restaurant_id GROUP BY restaurant.name ORDER BY review_count DESC;

--  7.  List all the reviews along with the restaurant, and the reviewer's
--      name. The result should have the restaurant name, the review text,
--      and the reviewer name.
--      Hint: you will need to do a three-way join - i.e. joining all three
--      tables together.

SELECT reviewer.name AS author_name, restaurant.name AS restaurant_name, review.review_text FROM review, restaurant, reviewer WHERE review.reviewer_id = reviewer.id AND review.restaurant_id = restaurant.id ORDER BY restaurant_name;

--  8.  Get the average stars given by each reviewer.
--      (reviewer name, average star rating)

SELECT reviewer.name AS author_name, AVG(review.stars) AS avg_stars FROM review, reviewer WHERE review.reviewer_id = reviewer.id GROUP BY reviewer.name ORDER BY reviewer.name;

--  9.  Get the lowest star rating given by each reviewer.
--      (reviewer name, lowest star rating)

SELECT reviewer.name AS author_name, MIN(review.stars) AS lowest_stars FROM review, reviewer WHERE review.reviewer_id = reviewer.id GROUP BY reviewer.name ORDER BY reviewer.name;

--  10. Get the number of restaurants in each category.
--      (category name, restaurant count)

SELECT restaurant.category, COUNT(restaurant.id) AS rest_count FROM restaurant GROUP BY restaurant.category;

--  11. Get number of 5 star reviews given by restaurant.
--      (restaurant name, 5-star count)

SELECT restaurant.name, count(review.stars) AS five_stars_count FROM restaurant, review WHERE restaurant.id = review.restaurant_id AND review.stars = 5 GROUP BY restaurant.name;

--  12. Get the average star rating for a food category.
--      (category name, average star rating)

SELECT restaurant.category, CAST(AVG(review.stars) AS DECIMAL(10,2)) AS avg_stars FROM restaurant, review WHERE restaurant.id = review.restaurant_id GROUP BY restaurant.category;
