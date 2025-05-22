import React, { useState } from "react";
import axios from "axios";
import "./HwanAjaxSecond.css";

// 카카오 API - 책책 데이터 검색하기
// URL : "https://dapi.kakao.com/v3/search/book",
// 요청 헤더 : Authorization : KakaoAK {REST API 키}
// 요청 파라미터 : query={검색어}
// data: { query: searchTxt },
// req.setRequestHeader("Authorization", "KakaoAK f34fe373bf79e015187495714d850629");
const HwanAjaxSecond = () => {
  const [searchTxt, setSearchTxt] = useState("");
  const [books, setBooks] = useState([]);

  const getBooks = () => {
    setBooks([]); // 새로운 검색 시 이전 결과 초기화
    axios
      .get("https://dapi.kakao.com/v3/search/book", {
        headers: { Authorization: "KakaoAK f34fe373bf79e015187495714d850629" },
        params: { query: searchTxt },
      })
      .then((res) => {
        setBooks(res.data.documents);
      });
  };

  const bookList = books.map((b, index) => (
    <tr key={index}>
      <td className="td">
        <span className="bookTitle">{b.title}</span>
      </td>
      <td className="td">
        <span className="bookPrice">{b.price.toLocaleString()}원</span>
      </td>
      <td className="td">
        <img src={b.thumbnail} alt={b.title} className="bookImage" />
      </td>
    </tr>
  ));

  return (
    <div className="container">
      <div className="searchBox">
        <input
          type="text"
          value={searchTxt}
          onChange={(e) => setSearchTxt(e.target.value)}
          placeholder="검색어를 입력하세요"
          className="input"
          onKeyPress={(e) => e.key === "Enter" && getBooks()}
        />
        <button onClick={getBooks} className="button">
          검색
        </button>
      </div>

      <div className="tableContainer">
        <table className="table">
          <thead>
            <tr>
              <th className="th">제목</th>
              <th className="th">가격</th>
              <th className="th">책 표지</th>
            </tr>
          </thead>
          <tbody>{bookList}</tbody>
        </table>
      </div>
    </div>
  );
};

export default HwanAjaxSecond;
