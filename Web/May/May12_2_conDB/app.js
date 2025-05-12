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

app.use('/', indexRouter);
app.use('/users', usersRouter);

app.listen(7655);

// http://localhost:7655/snack.reg?name=빼빼로&price=1000
app.get('/snack.reg',function(req, res) {
  // Node.js : JavaScript로 backend 작성
  // mongoDB : JavaScript로 제어
  // mongojs : Node.js에서 mongoDB 명령어를 그대로 사용하게 + 콜백 함수

  // mongjs
  var mjs = require('mongojs');
  //var db =  mjs("서버주소/DB명", ["테이블명", "테이블명", ...])
  var db = mjs("127.0.0.1/test", ["May_snack"]);

  var name = req.query.name;
  var price = parseInt(req.query.price);

  // err : 에러객체
  // doc : 결과 값
  db.May_snack.insert({name: name, price: price}, function(err, doc) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.send(doc);
  });

});


// http://localhost:7655/snack.get
app.get('/snack.get',function(req, res) {
  var db = require('mongojs')("127.0.0.1/test", ["May_snack"]);
  
  db.May_snack.find(function(err, doc) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.send(doc);
  });

});





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
