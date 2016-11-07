var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

http.listen(3000, function(){
  console.log('listening on *:3000');
});

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});


io.on('connection', function(socket){
  console.log('client connected');
  
  socket.on('disconnect', function(){
    console.log('client disconnected');
  });
  
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});

var spawn = require('child_process').spawn; 
Capture();
function Capture(){
	var pycapture    = spawn('python', ['../api/capture.py']);
	
	pycapture.stdout.on('data', function(data){
			console.log(data.toString());
		});
	pycapture.stdout.on('end', function(){
			Recognise();
			console.log('Capture Ends');
		});
} 

function Recognise() {	
for (var i = 0; i < 9; i++) {
    (function(i){
		   var pyrecognize    = spawn('python',[
												'../api/recognise.py',
												'../photo/trainingset', 
												'./tmp/'+i+'.jpg', 
												'1000000.0'
												]
									  );
		   pyrecognize.stdout.on('data', function(data){
				console.log(data.toString());
				io.emit('chat message', 'from server');
		   });
		   })(i)
		}
}


