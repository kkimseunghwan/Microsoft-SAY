import React, { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5555");

const HwanEchoClient2 = () => {
  // React 측에서 함수호출 (시간이 걸리는) 같은거는 비추
  // -> UseEffect에서 처리 권장.
  //const [socket, setSocket] = useState(io("http://localhost:5555"));

  const [msg, setMsg] = useState("");

  useEffect(() => {
    socket.on("svrMsg", (msg) => {
      alert(msg);
    });

    return () => {
      socket.close();
    };
  }, []);

  const sendMsg = () => {
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

export default HwanEchoClient2;
