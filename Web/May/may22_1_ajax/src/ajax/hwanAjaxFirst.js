import React, { useState } from "react";
import axios from "axios";

// React에는 따로 Ajax관련 기능이 없음 -> VanillaJS의 AJAX 기능을 사용해야 함
// -> AJAX 라이브러리를 사용
// -> 대표적인 AJAX 라이브러리 : axios
// yarn add axios
// https://api.openweathermap.org/data/2.5/weather?lat=37.5693582&lon=126.9858652&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr
const HwanAjaxFirst = () => {
  const [weather, setWeather] = useState({
    desc: "",
    temp: "",
    humi: "",
  });

  const getWeather = () => {
    //GET 요청
    // axios.get(요청주소).then(콜백함수)
    axios
      .get(
        "https://api.openweathermap.org/data/2.5/weather?lat=37.5693582&lon=126.9858652&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr"
      )
      .then((res) => {
        console.log(res);
        setWeather({
          desc: res.data.weather[0].description,
          temp: res.data.main.temp,
          humi: res.data.main.humidity,
        });
      });
  };

  return (
    <>
      <h2>날씨 : {weather.desc}</h2>
      <h2>기온 : {weather.temp}</h2>
      <h2>습도 : {weather.humi}</h2>
      <button onClick={getWeather}>날씨 가져오기</button>
    </>
  );
};

export default HwanAjaxFirst;
