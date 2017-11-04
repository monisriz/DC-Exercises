var express = require('express');
var app = express();
const body_parser = require('body-parser');
app.use(body_parser.urlencoded({extended: false}));
app.use('/static', express.static('public'));

var pgp = require('pg-promise')({});
var db = pgp({database: 'restaurant_db_v2'});

app.set('view engine', 'hbs');


app.get('/', function (request, response) {
  response.render('home.hbs');
});

app.get('/search', function (request, response, next) {
  let searchTerm = request.query.searchTerm;
  let query = "SELECT * FROM restaurant WHERE name ILIKE '%$1#%'";
  db.any(query, searchTerm)
    .then(function(searchResults) {
      var context = {searchResults: searchResults};
      response.render('search_results.hbs', context);
    })
    .catch(next);
});

app.get('/restaurant/:id', function (request, response, next) {
  var id = request.params.id;
  let query = "SELECT * FROM restaurant WHERE id = $1";
  let restaurant;

  db.one(query, id)
    .then(function(result) {
      restaurant = result;
      return db.query("SELECT * FROM review WHERE restaurant_id = $1", restaurant.id);
    })
    .then(function (reviews) {
      var context = {restaurant: restaurant, reviews: reviews};
      response.render('restaurant.hbs', context);
    })
    .catch(next)
});

app.post('/submit/:id', function (request, response, next) {
  var id = request.params.id;
  var query = "INSERT INTO review VALUES(default, null, $1, $2, $3, $4)"
  db.any(query, [request.body.inputStars, request.body.inputTitle, request.body.inputText, id])
    .then(function(result) {
      response.redirect(`/restaurant/${id}`);
    })
    .catch(next);
});

app.listen(8000, function () {
  console.log('Listening on port 8000');
});
