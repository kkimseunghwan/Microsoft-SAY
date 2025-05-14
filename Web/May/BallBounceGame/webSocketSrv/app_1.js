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

// Node.js : 웹 소캣 서버 구현에 특화.
//    1) js 파일 제공 -> 웹 환경에서 사용이 편리함.
//    2) 문법이 간단함.
//    3) 서버 특성상. 멀티 쓰레드 관련 구현이 필요
//        JavaScript언어는 non-blocking I/O형태에 특화된 언어
//        -> 멀티쓰레드 신경 안써도 동시에 여러 개의 요청을 처리할 수 있음.


// app.listen(1111); // HTTP 통신

// 통신 종류
// 1. 요청-응답 : HTTP, HTTPS
// 2. 실시간 통신 : socket 통신 
//    -> 라이브러리 설치 필요 
//    -> socket.io
//    npm install socket.io@2

const http = require('http').createServer();
const io = require('socket.io')(http, {
  cors: {
    origin: "*"
  }
});

io.listen(9999); // 소켓 통신
// => 웹소켓 서비스 시작
// http://주소:포트/socket.io/socket.io.js
// http://localhost:9999/socket.io/socket.io.js

// 객체(주어)
//    io.sockets : 연결된 모든 소켓 관리
//    socket : 개별 소켓 관리

// 메서드(동사)
//    emit("제목", 내용) : 이벤트 발생 -> 보낼 때 사용
//    on("제목", 콜백함수) : 이벤트 처리 -> 받을 때 사용




const MAX_USERS = 2;
let users = []; // socket.id 목록
let hostId = null; // 중심 사용자
let userName = {}; // 사용자 이름

io.on("connection", function(socket){
  console.log(`[접속] ${socket.id}`);

  // // 정원 초과 체크
  // if (users.length >= MAX_USERS) {
  //   socket.emit('error', '정원 초과입니다.');
  //   socket.disconnect(true);
  //   return;
  // }

  // 사용자 등록
  users.push(socket.id);

  // 중심 지정
  if (!hostId) {
    hostId = socket.id;
    socket.emit('you-are-host');
    console.log(`[호스트 지정] ${socket.id}`);
  } else {
    socket.emit('you-are-guest', { hostId, userName });
  }

  io.emit('user-list', users); // 전체 접속자에게 접속자 목록 전파
  
  //나갔을 때
  socket.on('disconnect', () => {
    console.log(`[퇴장] ${socket.id}`);
    users = users.filter(id => id !== socket.id);

    // 중심이 나가면 권한 이양
    if (socket.id === hostId) {
      hostId = users[0] || null;
      if (hostId) {
        io.to(hostId).emit('you-are-host');
        console.log(`[호스트 변경] ${hostId}`);
      } else {
        console.log(`[호스트 없음]`);
      }
    }
    // 전체 접속자에게 접속자 목록 새로고침
    io.emit('user-list', users); 
  });

  socket.on("message", function(message){
    console.log("메세지 받음");  
    console.log(message);

    io.sockets.emit("messageReturn", message);
  });

  socket.on("setname", function(name){
    console.log(socket.id + " 이름 설정");
    console.log(name);
    console.log(userName);
    userName[socket.id] = name;
    io.emit("user-list", users);
  });

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

