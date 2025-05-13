var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


const http = require('http').createServer();
const io = require('socket.io')(http, {
  cors: {
    origin: "*"
  }
});

io.listen(8888); // 소켓 통신

io.on("connection", function(socket){
  
  console.log(`[접속] ${socket.id}`);
  
  // 실시간 채팅 소켓 통신
  socket.on('clnMsg', function(msg) {
    console.log(`[메시지] ${JSON.stringify(msg)}`);
    // 메세지가 너무 길면 줄바꿈
    if (msg.msg.length > 55) {
      msg.msg = msg.msg.replace(/(\w{55})(\w)/, '$1\n$2');
    }

    io.sockets.emit('srvMsg', msg);
    
    
  });
  //


  // 그림 그리기 소켓 통신
  socket.on('drawMove', function(data) {
    console.log(`[그림] ${JSON.stringify(data)}`);
    io.sockets.emit('draw', data);

  });


  //

});
















app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

