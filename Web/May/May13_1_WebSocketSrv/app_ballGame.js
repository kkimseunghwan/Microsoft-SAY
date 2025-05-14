// app_ballGame.js

var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

// (기존 indexRouter, usersRouter, app 설정 등은 동일)
var indexRouter = require('./routes/index'); // 예시 경로, 실제 프로젝트에 맞게 수정
var usersRouter = require('./routes/users'); // 예시 경로, 실제 프로젝트에 맞게 수정

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


const http = require('http').createServer(app); // Express 앱을 http 서버에 바인딩
const io = require('socket.io')(http, {
  cors: {
    origin: "*"
  }
});

// 포트 변경 시 주의: 클라이언트에서도 동일한 포트로 접속해야 함
const PORT = 7776;
http.listen(PORT, () => { // Express 앱과 Socket.IO가 같은 포트를 사용하도록 수정
    console.log(`Server running on port ${PORT}`);
});


const MAX_PLAYERS = 2;
const winScore = 5;

const rooms = {}; // roomID : { players: [socket.id, socket.id], playerInfos: { socket.id: {nickname, color, order} } }
const players = {}; // socket.id : { nickname, color, score, x, roomID, order }
const gameStarted = {}; // roomID : true/false

const canvasWidth = 380;
const canvasHeight = 600;
const ballSize = 25;
const paddleWidth = 120; // 클라이언트와 동일하게
const paddleHeight = 20;
const paddleOffset = 30; // 패들이 벽에서 얼마나 떨어져 있는지

const gameStates = {};

function normalizeVector(x, y) {
  if (x === 0 && y === 0) return { x: 0, y: 0 }; // 0벡터 방지
  const norm = Math.sqrt(x * x + y * y);
  return { x: x / norm, y: y / norm };
}

function startGame(roomID) {
  console.log(`[게임 시작] ${roomID}`);
  gameStarted[roomID] = true;

  const xDir = Math.random() < 0.5 ? 1 : -1;
  const yDir = Math.random() < 0.5 ? 1 : -1;
  const norm = normalizeVector(xDir, yDir);

  gameStates[roomID] = {
    ballX: canvasWidth / 2 - ballSize / 2, // 공 중앙 정렬
    ballY: canvasHeight / 2 - ballSize / 2,
    xMove: norm.x,
    yMove: norm.y,
    speed: 9,
    lastHitBy: null, // 마지막으로 공을 친 플레이어 (패들겹침 버그 방지용)
    score: { p1: 0, p2: 0} // 플레이어 ID 대신 순서(0, 1)로 점수 관리
  };

  // 게임 루프 시작
  if (gameStates[roomID].gameInterval) clearInterval(gameStates[roomID].gameInterval); // 기존 인터벌 정리
  gameStates[roomID].gameInterval = setInterval(() => updateGame(roomID), 1000 / 60);

  // 점수 초기화 및 클라이언트에 전송
  io.to(roomID).emit("scoreUpdate", gameStates[roomID].score);
}

function resetBall(roomID, loserOrder) {
    const state = gameStates[roomID];
    state.ballX = canvasWidth / 2 - ballSize / 2;
    state.ballY = canvasHeight / 2 - ballSize / 2;
    state.speed = 9;
    state.lastHitBy = null;

    // 진 사람 쪽으로 공이 가도록 방향 설정 (선택적)
    const xDir = Math.random() < 0.5 ? 1 : -1;
    // loserOrder가 0이면 (아래쪽 플레이어, P1) 위로, 1이면 (위쪽 플레이어, P2) 아래로
    const yDir = loserOrder === 0 ? -1 : 1;
    const norm = normalizeVector(xDir, yDir);
    state.xMove = norm.x;
    state.yMove = norm.y;
}


function updateGame(roomID) {
  if (!gameStarted[roomID] || !rooms[roomID] || rooms[roomID].players.length < MAX_PLAYERS) {
      if (gameStates[roomID] && gameStates[roomID].gameInterval) {
          clearInterval(gameStates[roomID].gameInterval);
      }
      return;
  }

  const state = gameStates[roomID];
  const roomData = rooms[roomID];
  const playerSocketIDs = roomData.players;


  if (!state) return;

  state.ballX += state.xMove * state.speed;
  state.ballY += state.yMove * state.speed;

  // 벽 충돌 (좌우)
  if (state.ballX <= 0) {
    state.ballX = 0;
    state.xMove *= -1;
  } else if (state.ballX + ballSize >= canvasWidth) {
    state.ballX = canvasWidth - ballSize;
    state.xMove *= -1;
  }

  // 패들 충돌 처리
  playerSocketIDs.forEach(socketID => {
      const player = players[socketID];
      if (!player) return;

      const playerPaddleX = player.x;
      // player.order 가 0이면 아래쪽(P1), 1이면 위쪽(P2)
      const playerPaddleY = player.order === 0 ? canvasHeight - paddleOffset - paddleHeight : paddleOffset;

      // player.order 가 0이면 아래쪽(P1), 1이면 위쪽(P2)
      // player.order 가 1(p2)이면, 공이 튕겨지는 위치 좌표 기준이 반전되어 계산되어야 함.
      // 즉, 공이 튕겨지는 패들의 위치 좌표가 반전되어 계산되어야 함.
      // 패들 충돌 계산을 위한 공의 위치 좌표
      let ballCollisionX = state.ballX;
      let ballCollisionY = state.ballY;

      // P2(order 1)의 경우 공의 x좌표를 반전시켜 계산
      if (player.order === 1) {
          ballCollisionX = canvasWidth - state.ballX - ballSize;
      }


      // 공과 패들의 충돌 조건 개선
      if (
        ballCollisionX + ballSize > playerPaddleX && // 공의 오른쪽이 패들 왼쪽보다 크고
        ballCollisionX < playerPaddleX + paddleWidth && // 공의 왼쪽이 패들 오른쪽보다 작고
        ballCollisionY + ballSize > playerPaddleY && // 공의 아래쪽이 패들 위쪽보다 크고
        ballCollisionY < playerPaddleY + paddleHeight // 공의 위쪽이 패들 아래쪽보다 작다
      ) {
          // state.lastHitBy !== player.order : 같은 플레이어가 연속으로 치는 것 방지 (공이 패들 안에 끼는 현상 완화)
          if (state.lastHitBy !== player.order) {
              // y방향 반전
              state.yMove *= -1;

              // 공이 패들 경계에 정확히 위치하도록 조정
              if (player.order === 0) { // 아래쪽 패들 (P1)
                  state.ballY = playerPaddleY - ballSize;
              } else { // 위쪽 패들 (P2)
                  state.ballY = playerPaddleY + paddleHeight;
              }

              state.speed = Math.min(state.speed + 0.3, 15); // 속도 점진적 증가 (최대 15)
              state.lastHitBy = player.order; // 마지막으로 친 플레이어 기록
          }
      }
  });


  // 점수 획득 (천장 또는 바닥 충돌)
  let scored = false;
  if (state.ballY <= 0) { // P1 (아래쪽 player, order 0)이 점수 획득
    state.score.p1++;
    console.log(`Room ${roomID}: P1 scores! ${state.score.p1}:${state.score.p2}`);
    resetBall(roomID, 1); // 공은 P2쪽으로
    scored = true;
  } else if (state.ballY + ballSize >= canvasHeight) { // P2 (위쪽 player, order 1)가 점수 획득
    state.score.p2++;
    console.log(`Room ${roomID}: P2 scores! ${state.score.p1}:${state.score.p2}`);
    resetBall(roomID, 0); // 공은 P1쪽으로
    scored = true;
  }

  if (scored) {
      io.to(roomID).emit("scoreUpdate", state.score);
      // 승리 조건 (예: 5점 먼저 내는 쪽이 승리)
      if (state.score.p1 >= winScore || state.score.p2 >= winScore) {
          const winner = state.score.p1 >= 5 ? playerSocketIDs.find(id => players[id].order === 0) : playerSocketIDs.find(id => players[id].order === 1);
          const winnerNick = players[winner] ? players[winner].nickname : "Player";
          io.to(roomID).emit("gameOver", { winner: winnerNick, score: state.score });
          console.log(`Room ${roomID} Game Over. Winner: ${winnerNick}`);
          gameStarted[roomID] = false; // 게임 종료 상태로 변경
          if(gameStates[roomID].gameInterval) clearInterval(gameStates[roomID].gameInterval); // 루프 중지

      }
  }


  // 각 플레이어에게 공 위치 전송 (상대방은 X축 반전)
  playerSocketIDs.forEach(socketID => {
      const player = players[socketID];
      if (!player) return;

      let ballDataForPlayer;
      if (player.order === 0) { // P1 (아래쪽, 기준 플레이어)
          ballDataForPlayer = {
              x: state.ballX,
              y: state.ballY
          };
      } else { // P2 (위쪽, 상대 플레이어) - 화면 전체가 반전된다고 가정
          ballDataForPlayer = {
              x: canvasWidth - state.ballX - ballSize, // X축 반전
              y: canvasHeight - state.ballY - ballSize // Y축도 반전 (위아래가 바뀌므로)
          };
      }
      io.to(socketID).emit("ballMoved", ballDataForPlayer);
  });
}


io.on("connection", function(socket){
  console.log(`[접속] ${socket.id}`);
  let assignedRoomID = null;

  for(const [roomID, roomData] of Object.entries(rooms)){
    if (roomData.players.length < MAX_PLAYERS){
      assignedRoomID = roomID;
      break;
    }
  }

  if (!assignedRoomID){
    assignedRoomID = 'room_' + Date.now();
    rooms[assignedRoomID] = { players: [], playerInfos: {} };
  }

  const playerOrder = rooms[assignedRoomID].players.length; // 0이면 P1, 1이면 P2
  rooms[assignedRoomID].players.push(socket.id);
  rooms[assignedRoomID].playerInfos[socket.id] = { order: playerOrder };

  socket.join(assignedRoomID);
  players[socket.id] = { roomID: assignedRoomID, order: playerOrder, x: canvasWidth / 2 - paddleWidth / 2 }; // 기본 x 위치 중앙

  console.log(`Player ${socket.id} joined ${assignedRoomID} as player order ${playerOrder}`);
  console.log(rooms);

  socket.emit("roomAssigned", { "roomID": assignedRoomID, "playerID": socket.id, "playerOrder": playerOrder });

  socket.on("playerData", function (data) {
    if (players[socket.id]) {
        players[socket.id].nickname = data.nickname;
        players[socket.id].color = data.color;
        rooms[assignedRoomID].playerInfos[socket.id].nickname = data.nickname; // 방 정보에도 닉네임 업데이트
        rooms[assignedRoomID].playerInfos[socket.id].color = data.color;

        // 모든 플레이어 정보 업데이트하여 방 전체에 브로드캐스트
        io.to(assignedRoomID).emit("playersInfoUpdate", rooms[assignedRoomID].playerInfos);
    }
  });

  socket.on("paddleMove", function (data) {
    const player = players[socket.id]; // 현재 플레이어 정보 가져오기
    if (player && player.roomID && gameStarted[player.roomID]) { // player.roomID 사용 및 gameStarted 확인
      player.x = data.x; // 플레이어 x좌표 업데이트

      // 현재 소켓이 속한 방(player.roomID)의 다른 모든 클라이언트에게 emit
      socket.broadcast.to(player.roomID).emit("enemyPaddleMoved", {
         x: data.x // 상대방에게는 나의 실제 x 좌표를 그대로 전달 (클라이언트에서 필요시 반전)
      });
    }
  });

  // 서버 app_ballGame.js의 기존 disconnect 핸들러 (이 부분은 잘 되어 있음)
  socket.on("disconnect", function () {
    console.log("[퇴장]" + socket.id);
    const playerInfo = players[socket.id];
    if (!playerInfo || !playerInfo.roomID || !rooms[playerInfo.roomID]) {
        // 플레이어가 방에 제대로 할당되기 전에 연결이 끊어졌을 수 있음
        if(players[socket.id]) delete players[socket.id]; // players 객체에서만이라도 제거
        return;
    }

    const roomID = playerInfo.roomID;
    const roomData = rooms[roomID];

    // 플레이어 목록에서 제거
    const playerIndex = roomData.players.indexOf(socket.id);
    if (playerIndex > -1) {
      roomData.players.splice(playerIndex, 1);
    }
    // playerInfos 에서도 제거
    if (roomData.playerInfos && roomData.playerInfos[socket.id]) {
        delete roomData.playerInfos[socket.id];
    }
    // players 전역 객체에서 제거
    delete players[socket.id];


    if (roomData.players.length === 0) {
      console.log(`[방 삭제] ${roomID}`);
      if (gameStates[roomID] && gameStates[roomID].gameInterval) {
          clearInterval(gameStates[roomID].gameInterval);
      }
      delete rooms[roomID];
      delete gameStates[roomID];
      delete gameStarted[roomID];
    } else {
      // 남은 플레이어에게 상대방 퇴장 알림
      io.to(roomID).emit("playerLeft", { remainingPlayers: roomData.playerInfos });
      gameStarted[roomID] = false; // 게임 중단
      if (gameStates[roomID] && gameStates[roomID].gameInterval) {
          clearInterval(gameStates[roomID].gameInterval);
      }
      // TODO: 게임 재시작 로직 또는 대기 화면 전환 로직 필요 (현재는 클라에서 새 매칭 유도)
    }
    console.log("현재 방 목록:", rooms);
    console.log("현재 플레이어 목록:", players);
  });

  if (rooms[assignedRoomID].players.length === MAX_PLAYERS){
    io.to(assignedRoomID).emit("gameStartSignal", { message: "Game is starting!", players: rooms[assignedRoomID].playerInfos });
    startGame(assignedRoomID);
  }
});



//




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

