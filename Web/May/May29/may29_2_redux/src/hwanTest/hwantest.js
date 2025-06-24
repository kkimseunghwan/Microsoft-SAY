import React, { useState } from "react";

const HwanTest = () => {
  const [fontSize, setFontSize] = useState(16); // 기본 폰트 크기 16px

  const increaseFontSize = () => {
    setFontSize((prevSize) => prevSize + 2);
  };

  const decreaseFontSize = () => {
    setFontSize((prevSize) => Math.max(prevSize - 2, 8)); // 최소 8px
  };

  return (
    <>
      <h2 style={{ fontSize: `${fontSize}px` }}>asd</h2>
      <button onClick={increaseFontSize}>크게</button>
      <button onClick={decreaseFontSize}>작게</button>
    </>
  );
};

export default HwanTest;
