import io from "socket.io-client";
import React, { useEffect, useState } from "react";

const HwanSocketClient = () => {
  useEffect(() => {
    const socket = io("http://localhost:1111");
    socket.on("connect", () => {
      console.log("connected");
    });
  }, []);

  return <div>HwanSocketClient</div>;
};

export default HwanSocketClient;
