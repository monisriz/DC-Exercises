var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);



app.set('view engine', 'hbs');
app.use('/static', express.static('public'));

app.get('/', function (request, response) {
  response.render('home.hbs');
});


io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    console.log('message: ' + msg);
  });
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});


http.listen(3000, function() {
  console.log('listening on *:3000');
});
