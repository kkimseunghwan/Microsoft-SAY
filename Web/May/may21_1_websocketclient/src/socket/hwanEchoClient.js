import React, { useEffect, useState } from "react";
import io from "socket.io-client";

//io.connect("http://localhost:1111"); -> let socket = io(주소)
// React : 화면 전환 잦은 사이트 개발에 유리 + JS + VDOM : 비동기식 추구
//          -> state 변경한거 바로 반영 안되고 다음 렌더링 때 반영
const HwanEchoClient = () => {
  // React 측에서 함수호출 (시간이 걸리는) 같은거는 비추
  // -> UseEffect에서 처리 권장.
  //const [socket, setSocket] = useState(io("http://localhost:5555"));

  const [socket, setSocket] = useState();
  const [msg, setMsg] = useState("");

  useEffect(() => {
    const socket = io("http://localhost:5555");
    setSocket(socket);

    // if (socket) {
    //   socket.on("svrMsg", (msg) => {
    //     alert(msg);
    //   });
    // }

    return () => {};
  }, []);

  const sendMsg = () => {
    //alert(msg);
    socket.emit("clntMsg", msg);
  };

  return (
    <>
      <h2>HwanSocketClient</h2>
      <input type="text" value={msg} onChange={(e) => setMsg(e.target.value)} />
      <button onClick={sendMsg}>전송</button>
    </>
  );
};

export default HwanEchoClient;
