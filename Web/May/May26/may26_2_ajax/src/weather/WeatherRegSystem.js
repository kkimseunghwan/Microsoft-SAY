import React, { useRef, useState } from "react";
import axios from "axios";

const WeatherRegSystem = () => {
  const iconInput = useRef();
  const [regResult, setRegResult] = useState({
    result: "",
    desc: "",
    temp: "",
    icon: "",
  });
  const [weather, setWeather] = useState({ desc: "", temp: "", icon: "" });

  const changeWeather = (e) => {
    if (e.target.name === "icon") {
      setWeather({ ...weather, [e.target.name]: e.target.files[0] });
    } else {
      setWeather({ ...weather, [e.target.name]: e.target.value });
    }
  };

  const weatherFD = new FormData();
  weatherFD.append("desc", weather.desc);
  weatherFD.append("temp", weather.temp);
  weatherFD.append("icon", weather.icon);

  const regWeather = () => {
    axios
      .post("http://195.168.9.143:1125/weather.reg", weatherFD, {
        // 이미지 파일 인코딩 처리 : headers: { "Content-Type": "multipart/form-data" },
        headers: { "Content-Type": "multipart/form-data" },
        withCredentials: true,
      })
      .then((res) => {
        alert(JSON.stringify(res.data));
        setRegResult(res.data);
        setWeather({ desc: "", temp: "", icon: "" });
        // 이미지 초기화
        iconInput.current.value = "";
      });
  };

  return (
    <>
      <table>
        <tr>
          <td>날씨 : </td>
          <td>
            <input value={weather.desc} name="desc" onChange={changeWeather} />
          </td>
        </tr>
        <tr>
          <td>기온 : </td>
          <td>
            <input value={weather.temp} name="temp" onChange={changeWeather} />
          </td>
        </tr>

        <tr>
          <td>이미지 : </td>
          <td>
            <input
              ref={iconInput}
              type="file"
              name="icon"
              onChange={changeWeather}
            />
          </td>
        </tr>
        <tr>
          <td>
            <button onClick={regWeather}>등록</button>
          </td>
        </tr>
      </table>
      <hr />
      <h2>등록 성공 여부 : {regResult.result}</h2>
      <h2>등록한 날씨 : {regResult.desc}</h2>
      <h2>등록한 온도 : {regResult.temp}</h2>
      <h2>등록한 사진 파일 명 : {regResult.icon}</h2>
      <h2>등록한 사진 : </h2>
      <a
        href={`http://195.168.9.143:1125/weather.icon.get?icon=${regResult.icon}`}
      >
        다운 받기
      </a>{" "}
      <br />
      <img
        src={`http://195.168.9.143:1125/weather.icon.get?icon=${regResult.icon}`}
        alt=""
      />
    </>
  );
};

export default WeatherRegSystem;
