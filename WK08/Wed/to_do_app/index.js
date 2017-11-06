var express = require('express');
var app = express();
var body_parser = require('body-parser');

var pgp = require('pg-promise')({});
var db = pgp({database: 'todo'});

app.set('view engine', 'hbs');
app.use('/static', express.static('public'));
app.use(body_parser.urlencoded({extended: false}));


app.get('/', function (request, response) {
  response.render('home.hbs');
});

app.get('/todos', function (request, response, next) {
  let query = "SELECT * FROM task ORDER BY id";
  db.any(query)
    .then(function(todolist) {
      response.render('todos.hbs', {todolist: todolist});
    })
    .catch(next);
});

app.post('/add', function (request, response, next) {
  var description = request.body.new_todo;
  let update = "INSERT INTO task VALUES(default, $1, null)";
  db.any(update, description)
    .then(function() {
      response.redirect('/todos');
    })
    .catch(next);
});

app.post('/update/:id', function (request, response, next) {
  var id = request.params.id;
  let query = "SELECT * FROM task WHERE id = $1";
  db.one(query, id)
    .then(function(task) {
      if (task.done) {
        var update = "UPDATE task SET done = FALSE WHERE id = $1";
      }
      else {
        var update = "UPDATE task SET done = TRUE WHERE id = $1";
      };
      return db.any(update, id);
    })
    .then(function(){
      response.redirect('/todos');
    })
    .catch(next);
});

app.listen(8000, function () {
  console.log('Listening on port 8000');
});