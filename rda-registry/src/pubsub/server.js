var fs = require('fs');
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

if (fs.existsSync('.env')) {
    require('dotenv').config();
}

const mode = process.env.MODE ? process.env.MODE : 'HTTP'
const port = process.env.PORT ? process.env.PORT : 3000;

const options = {
    url: process.env.REDIS_URL ? process.env.REDIS_URL : 'redis://127.0.0.1:6379'
}

var redis = require("redis")
    , subscriber = redis.createClient(options)
    , publisher  = redis.createClient(options);

subscriber.psubscribe('*');

subscriber.on("pmessage", function(pchannel, channel, message) {
    // console.log("Message '" + message + "' on channel '" + channel + "' arrived!")
    io.emit(channel, message);
});

io.on('connection', function(socket){
    // console.log('New connection from ' + socket.request.connection.remoteAddress);
    socket.on('disconnect', function(socket) {
        // console.log( 'a user disconnected' );
    });
});

if (mode == "HTTP") {
    http.listen(port, function(){
      console.log('listening http on '+port);
    });
} else if (mode == "HTTPS") {
    
    const credential = {
        key: fs.readFileSync(process.env.SSL_KEY),
        cert: fs.readFileSync(process.env.SSL_CERT)
    }
    var https = require('https').Server(credential, app);
    var io = require('socket.io')(https);
    
    https.listen(port, function() {
        console.log( 'listening https on '+port );
    });
}

