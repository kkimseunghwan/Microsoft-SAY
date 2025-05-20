import React, { useEffect, useState } from "react";

const HwanResizeEvent2 = () => {
  // 메뉴 호출 함수
  const summonMenu = () => {};

  // 메뉴 호출 이벤트 연결
  // 메뉴 호출 이벤트 제거
  // 설명 : 브라우저 크기가 변경될 때마다 메뉴를 호출하는 이벤트를 연결하고, 컴포넌트가 사라질 때 이벤트를 제거합니다.
  useEffect(() => {
    window.addEventListener("resize", summonMenu);
    return () => {
      window.removeEventListener("resize", summonMenu);
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
