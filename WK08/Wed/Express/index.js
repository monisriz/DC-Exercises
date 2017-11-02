var express = require('express');
var app = express();

app.set('view engine', 'hbs');
app.use('/static', express.static('public'));

// Hello World
//
// Make an express program that will display "Hello, world!" at the root URL: /
app.get('/', function (request, response) {
  response.send('Hello, World!');
});

// Routes
//
// Add to your program the following pages:
//
// "Meow" at the URL /cats
// "Woof" at the URL /dogs
// "Living together" at the URL /cats_and_dogs
        // app.get('/cats', function (request, response) {
        //   response.send('Meow');
        // });
        // app.get('/dogs', function (request, response) {
        //   response.send('Woof');
        // });
        // app.get('/cats_and_dogs', function (request, response) {
        //   response.send('Living together');
        // });

// Route Parameters
//
// Adding to the same program, say a greeting to the user, given that the user's name is encoded inside the URL. For example, if you go to the URL
//
// /greet/Kennedy it should say "Hello, Kennedy!"
// /greet/Jamison it should say "Hello, Jamison!"
// /greet/Manny it should say "Hello, Manny!"
      // app.get('/greet/:username', function (request, response) {
      //   var username = request.params.username;
      //   response.send(`Hello, ${username}!`);
      // });

// Query Parameters: Tell the year you were born
//
// Adding to the same program, display the year you were born when you report
// your age in a query parameter. For example, when you go to the URL:
//
// /year?age=32 it will display You were born in 1985.
app.get('/year', function (request, response) {
  var userage = request.query.userage || '1950';
  response.send(`You were born in ${2017 - userage}.`);
});

// Templates
//
// Make the greet page say hello to visitor and tell the year they were born. This time you will use a .hbs file in the views folder to render the message using HTML.
//
// For example, if you go to the URL:
//
// /greet/Manoush?age=32
//
// The server should render the html:
//
// <h1>Hello, Manoush!</h1>
// <p>You were born in 1985.</p>

app.get('/greet/:username', function (request, response) {
  var username = request.params.username;
  var userage = request.query.userage;
  var year = 2017 - userage;
  var context = {title: 'Hello', username: username, userage: userage, year: year};
  response.render('greet.hbs', context);
});

// Templates 2
//
// Create this array in your server program:
//
// var animals = [
//   { name: 'cats', favorite: true },
//   { name: 'dogs', favorite: true },
//   { name: 'tree frogs', favorite: true },
//   { name: 'earth worms', favorite: false },
//   { name: 'guinea pigs', favorite: true },
// ];
// Feel free to change to match your current state of mind.
//
// Create a page at the URL /fav_animals that will render an ordered list of those animals which are your favorite.
app.get('/fav_animals', function (request, response) {
  var animals = [
    { name: 'cats', favorite: true },
    { name: 'dogs', favorite: true },
    { name: 'elephant', favorite: true },
    { name: 'pigs', favorite: false },
    { name: 'lion', favorite: true },
    { name: 'honeybadger', favorite: true }
  ];

  var context = {title: 'Favorite Animals', animals: animals};
    response.render('fav_animals.hbs', context);
});

// Templates 3
//
// Go back through each page you have created previous and make an .hbs for
// each one, use resp.render to render them.

app.get('/cats', function (request, response) {
  response.render('cats.hbs');
});
app.get('/dogs', function (request, response) {
  response.render('dogs.hbs');
});
app.get('/cats_and_dogs', function (request, response) {
  response.render('cats_and_dogs.hbs');
});



app.listen(8000, function () {
  console.log('Listening on port 8000');
});
