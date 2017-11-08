var express = require('express');
var app = express();
var ROOMS = {};
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.use('/socket-io', express.static('node_modules/socket.io-client/dist'));

app.set('view engine', 'hbs');
app.use('/static', express.static('public'));

app.get('/', function (request, response) {
  response.render('home.hbs');
});


io.on('connection', function(client){
  console.log('USER CONNECTED');

  client.on('join-room', function(room){
    client.join(room, function() {

      if (ROOMS[room]) {
        ROOMS[room].push(client.id);
      }
      else {
        ROOMS[room] = [client.id];
      }
      // console.log("Global", ROOMS);
      ROOMS[room].forEach(function (id) {
        if (id != client.id) {
          io.to(id).emit('chat message', '**A NEW USER HAS JOINED**');
        }
      });
        io.to(client.id).emit('chat message', '**THANKS FOR JOINING**');
    });
  });

  client.on('incoming', function(msg){
    io.to(msg.room).emit('chat message', msg.msg);
  });

  client.on('disconnect', function(id){
    console.log('USER DISCONNECTED');
    io.emit('chat message', '**USER HAS LEFT**');
  });

});


http.listen(3000, function() {
  console.log('listening on *:3000');
});
