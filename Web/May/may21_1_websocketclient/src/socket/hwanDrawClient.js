import React, { useEffect, useState, useRef } from "react";
import io from "socket.io-client";
import "./drawingCss.css";

const socket = io("http://localhost:5555");

const HwanDrawClient = () => {
  const [isDrawing, setIsDrawing] = useState(false);

  const [drawOptions, setDrawOptions] = useState({
    color: "black",
    lineWidth: 2, // 선 굵기
  });
  const lastPositionRef = useRef({ x: 0, y: 0 }); // 이전 좌표를 ref로 관리

  const paperRef = useRef(null);
  const [drawTool, setDrawTool] = useState({
    paper: null,
    pen: null,
  });

  // 캔버스 초기화
  useEffect(() => {
    if (paperRef.current) {
      const canvas = paperRef.current;
      const pen = canvas.getContext("2d");
      setDrawTool({ paper: canvas, pen });

      pen.lineCap = "round";
      pen.strokeStyle = drawOptions.color;
      pen.lineWidth = drawOptions.lineWidth;
    }
  }, []); // (초기 1회 실행)

  // 서버로부터 드로잉 데이터 수신
  useEffect(() => {
    if (!drawTool.pen) return;

    const handleDraw = (data) => {
      // 수신한 데이터로 그림
      draw(drawTool.pen, data);
    };

    socket.on("draw", handleDraw);

    return () => {
      socket.off("draw", handleDraw); // 이벤트 리스너 정리
      // socket.close()는 컴포넌트 언마운트 시에만 하는 것이 일반적
      // 만약 drawTool.pen이 변경될 때마다 소켓 연결을 끊고 싶다면 유지
    };
  }, [drawTool.pen]); // drawTool.pen이 설정된 후에 리스너 등록

  // 그림 그리기 함수
  const draw = (pen, data) => {
    if (!pen) return;
    pen.strokeStyle = data.color;
    pen.lineWidth = data.lineWidth || 2; // 서버에서 lineWidth도 받을 수 있도록
    pen.beginPath();
    pen.moveTo(data.lastX, data.lastY);
    pen.lineTo(data.currentX, data.currentY);
    pen.stroke();
  };

  const handleMouseDown = (e) => {
    setIsDrawing(true);
    const { offsetX, offsetY } = e.nativeEvent;
    lastPositionRef.current = { x: offsetX, y: offsetY };
    // 필요하다면 mousedown 시점의 점을 찍는 로직 추가 가능 (예: 작은 원)
    // 현재는 mouseMove가 발생해야 선이 그려짐
  };

  const handleMouseUp = () => {
    setIsDrawing(false);
  };

  const handleMouseMove = (e) => {
    if (!isDrawing || !drawTool.pen) return;

    const { offsetX, offsetY } = e.nativeEvent;
    const currentPosition = { x: offsetX, y: offsetY };

    const drawingData = {
      color: drawOptions.color,
      lineWidth: drawOptions.lineWidth,
      lastX: lastPositionRef.current.x,
      lastY: lastPositionRef.current.y,
      currentX: currentPosition.x,
      currentY: currentPosition.y,
    };

    // 1. 로컬에서 먼저 그리기 (즉각적인 반응)
    draw(drawTool.pen, drawingData);

    // 2. 서버로 드로잉 데이터 전송
    socket.emit("drawMove", drawingData);

    // 3. 다음 선 그리기를 위해 현재 위치를 이전 위치로 업데이트
    lastPositionRef.current = currentPosition;
  };

  const handleMouseLeave = () => {
    // 캔버스 밖으로 나가도 그리기가 멈추도록
    setIsDrawing(false);
  };

  const handleColorChange = (e) => {
    setDrawOptions((prevOptions) => ({
      ...prevOptions,
      color: e.target.value,
    }));
    // 펜의 색상도 즉시 변경 (만약 draw 함수에서 매번 설정하지 않는다면)
    if (drawTool.pen) {
      drawTool.pen.strokeStyle = e.target.value;
    }
  };

  return (
    <>
      <canvas
        ref={paperRef}
        width="800px"
        height="600px"
        style={{ border: "black solid 3px", touchAction: "none" }} // 모바일 터치 이벤트 기본 동작 방지
        onMouseDown={handleMouseDown}
        onMouseUp={handleMouseUp}
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
        // 모바일 터치 이벤트 핸들러 (필요시 추가)
        // onTouchStart={handleMouseDown} // 이벤트 객체 구조가 다를 수 있으므로 별도 처리 권장
        // onTouchMove={handleMouseMove}
        // onTouchEnd={handleMouseUp}
      ></canvas>
      <br />
      <input
        type="color"
        id="colorPicker"
        value={drawOptions.color} // value를 state와 바인딩
        style={{ width: "100px", height: "100px" }}
        onChange={handleColorChange}
      />
      {/* 선 굵기 조절 예시 */}
      {/*
      <input
        type="range"
        min="1"
        max="20"
        value={drawOptions.lineWidth}
        onChange={(e) => {
          setDrawOptions((prevOptions) => ({
            ...prevOptions,
            lineWidth: parseInt(e.target.value, 10),
          }));
          if (drawTool.pen) {
            drawTool.pen.lineWidth = parseInt(e.target.value, 10);
          }
        }}
      />
      */}
    </>
  );
};

export default HwanDrawClient;
