import React, { useEffect, useState } from "react";

const HwanResizeEvent = () => {
  const [w_h, setW_h] = useState({
    // vanillaJS에서 브라우저 사이즈
    w: 0,
    h: 0,
  });

  const updateWH = () => {
    setW_h({
      w: window.innerWidth,
      h: window.innerHeight,
    });
  };

  useEffect(() => {
    window.addEventListener("resize", updateWH); // VanillaJS에서 스스로 이벤트 연결

    return () => {
      // 컴포넌트가 사라질때 이벤트 제거
      window.removeEventListener("resize", updateWH);
    };
  }, []);

  return (
    <>
      <h2>가로 : {w_h.w}</h2>
      <h2>세로 : {w_h.h}</h2>

      <button
        onClick={() => {
          alert("크기조절");
        }}
      >
        크기 조절
      </button>
    </>
  );
};

export default HwanResizeEvent;
