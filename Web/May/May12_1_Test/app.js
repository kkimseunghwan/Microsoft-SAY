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

app.listen(5643); // Node.js Express WAS 포트번호

app.get("/te.st", function(req, res) { //첫번째인자 요청, 두번째 인자 응답
  res.send("abcd");
});

// 195.168.9.139
// http://195.168.9.139:5643/param.test?a=10&b=20
app.get("/param.test", function(req, res) {
  var aa = req.query.a; // req.query.파라미터변수명
  var bb = req.query.b;
  var cc = aa + bb;
  res.send(cc + ""); // 숫자 -> 글자 + "" 해줘야 함
});

// http://IP주소:5643/json.res.test?a=10&b=20
app.get("/json.res.test", function(req, res) {
  var aa = req.params.a * 1;
  var bb = req.params.b * 1;
  var cc = aa + bb;
  var dd = {"result": cc};
  res.send(dd);
});
// app.use('/', indexRouter); // get post 공용?
// app.use('/users', usersRouter); 이거 두줄 필요없다?

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

