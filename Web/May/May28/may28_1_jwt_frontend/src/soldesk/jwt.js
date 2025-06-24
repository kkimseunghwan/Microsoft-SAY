import React, { useState } from "react";
import axios from "axios";

const JWT = () => {
  const [data, setdata] = useState({
    name: "",
    price: 0,
  });

  const changeData = (e) => {
    setdata({ ...data, [e.target.name]: e.target.value });
  };

  const productFD = new FormData();
  productFD.append("name", data.name);
  productFD.append("price", data.price);

  const getData = () => {
    axios.post(`http://195.168.9.143:1125/data.post`, productFD).then((res) => {
      sessionStorage.setItem("KeyDesu", res.data.menuJWT);
      alert(JSON.stringify(res));
    });
  };

  return (
    <>
      <h2>Json Web Token</h2>
      이름 :{" "}
      <input
        name="name"
        value={data.name}
        onChange={changeData}
        autoComplete="off"
      />
      <br />
      가격 :{" "}
      <input
        name="price"
        value={data.price}
        onChange={changeData}
        autoComplete="off"
      />{" "}
      <br />
      <button onClick={getData}>등록</button>
      <button onClick={getData}>확인</button>
    </>
  );
};

export default JWT;
