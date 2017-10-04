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
