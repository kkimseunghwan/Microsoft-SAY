import React from "react";
import axios from "axios";
import { useState } from "react";

const Calculate = () => {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [result, setResult] = useState({ hab: 0, cha: 0, gob: 0, mok: 0 });

  const numFD = new FormData();
  numFD.append("x", num1);
  numFD.append("y", num2);

  const calculate = () => {
    // GET방식
    // axios.get(요청주소, {headers:{이름:값, 이름:값, ...}}).then(res)=>{콜백함수})
    // 요청 파라미터가 주소에 표시됨

    // POST방식
    // axios.post(요청주소, {이름:값, 이름:값, ...}).then(res)=>{콜백함수})
    // 요청 파라미터가 주소에 표시되지 않음 (내부적으로 전송) => GET 방식보다 보안성 높음
    // 파라메터가 주소에 실을 수 없는 요소 : 체크박스, 버튼, 파일 등
    // POST가 사용되는 경우. 로그인 때, 채크박스, 파일, 기타 보안을 좀 더 중요하게 여기는 경우
    axios
      .post("http://localhost:1123/calculate", numFD, { withCredentials: true })
      .then((res) => {
        setResult(res.data);
      })
      .catch((error) => {
        console.error("Error:", error);
        alert(
          "서버 연결에 실패했습니다. 백엔드 서버가 실행 중인지 확인해주세요."
        );
      });
  };

  const changeNum1 = (e) => {
    setNum1(e.target.value);
  };

  const changeNum2 = (e) => {
    setNum2(e.target.value);
  };

  return (
    <div>
      <h1>Calculate</h1>
      X :<input
        type="text"
        name="num1"
        onChange={changeNum1}
        value={num1}
      />{" "}
      <br />
      Y :<input
        type="text"
        name="num2"
        onChange={changeNum2}
        value={num2}
      />{" "}
      <br />
      <button onClick={calculate}>계산하기</button> <br />
      <hr />
      <h2>결과</h2>
      <div id="result">
        hab: {result.hab} <br />
        cha: {result.cha} <br />
        gob: {result.gob} <br />
        mok: {result.mok} <br />
      </div>
    </div>
  );
};

export default Calculate;
