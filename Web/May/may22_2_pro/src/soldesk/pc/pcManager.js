import React, { useEffect, useState } from "react";
import pmmc from "./pcManager.module.css";
import axios from "axios";

const PCManager = () => {
  const [pages, setPages] = useState([]);
  const pageSpans = pages.map((p, i) => (
    <span
      className={pmmc.pageSpan}
      onClick={() => {
        getComputer(p);
      }}
    >
      {p}
    </span>
  ));

  const [pc, setPc] = useState({ name: "", what: "", ip: "", condition: "" });
  const [pcs, setPcs] = useState([]);
  const pcTrs = pcs.map((p, i) => {
    return (
      <tr className={pmmc.dataTr}>
        <td align="center">{p.no}</td>
        <td align="center">{p.name}</td>
        <td align="center">{p.what}</td>
        <td align="center">{p.ip}</td>
        <td align="center">{p.condition}</td>
      </tr>
    );
  });

  const getComputer = (page) => {
    axios
      .get(`http://195.168.9.59:1111/computer.get?page=${page}`)
      .then((res) => {
        setPcs(res.data.computers);
        const ar = [];
        for (let i = 1; i <= res.data.pageCount; i++) {
          ar.push(i);
        }
        setPages(ar);
      });
  };

  useEffect(() => {
    getComputer(1);

    return () => {};
  }, []);

  const changePcInfo = (e) => {
    setPc({ ...pc, [e.target.name]: e.target.value });
  };
  const reg = () => {
    if (
      pc.name === "" ||
      pc.what === "" ||
      pc.ip === "" ||
      pc.condition === "" ||
      pc.condition.length !== 2
    ) {
      alert("?");
    } else {
      axios
        .get(
          `http://195.168.9.143:1111/computer.reg?name=${pc.name}&what=${pc.what}&ip=${pc.ip}&condition=${pc.condition}`
        )
        .then((res) => {
          alert(res.data.result);
          setPc({ name: "", what: "", ip: "", condition: "" });
        });
    }
  };
  return (
    <>
      <table id="pcManagerRegTbl">
        <tr>
          <td align="center">
            <input
              name="name"
              value={pc.name}
              onChange={changePcInfo}
              placeholder="이름"
              autoComplete="off"
              maxLength={10}
            />
          </td>
        </tr>
        <tr>
          <td align="center">
            <input
              name="what"
              value={pc.what}
              onChange={changePcInfo}
              placeholder="용도"
              autoComplete="off"
              maxLength={10}
            />
          </td>
        </tr>
        <tr>
          <td align="center">
            <input
              name="ip"
              value={pc.ip}
              onChange={changePcInfo}
              placeholder="IP주소"
              autoComplete="off"
              maxLength={15}
            />
          </td>
        </tr>
        <tr>
          <td align="center">
            <input
              name="condition"
              value={pc.condition}
              onChange={changePcInfo}
              placeholder="상태"
              autoComplete="off"
              maxLength={2}
            />
          </td>
        </tr>
        <tr>
          <td align="center">
            <button onClick={reg}>등록</button>
          </td>
        </tr>
      </table>
      <hr />
      <table id="pcManagerPCTbl">
        <tr>
          <th style={{ width: "10%" }}>번호</th>
          <th style={{ width: "25%" }}>이름</th>
          <th style={{ width: "25%" }}>용도</th>
          <th style={{ width: "25%" }}>IP주소</th>
          <th style={{ width: "15%" }}>상태</th>
        </tr>
        {pcTrs}
        <tr>
          <td align="center" colSpan={5} style={{ height: 30 }}>
            {pageSpans}
          </td>
        </tr>
      </table>
    </>
  );
};

export default PCManager;
