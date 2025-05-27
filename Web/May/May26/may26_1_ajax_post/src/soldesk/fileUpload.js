import React, { useRef, useState } from "react";
import axios from "axios";

const FileUpload = () => {
  const [photo, setPhoto] = useState({ title: "", photo: "" });
  const [result, setResult] = useState({ title: "" });
  const photoInput = useRef(); // fila타입 input은

  const changePhoto = (e) => {
    // 파일의 유효성 검사라면 : e.target.value
    // 파일의 경우 여러개 선택도 되고, 객체 형태로 받기 위해 : e.target.files[0]
    if (e.target.name === "photo") {
      setPhoto({ ...photo, [e.target.name]: e.target.files[0] });
    } else {
      setPhoto({ ...photo, [e.target.name]: e.target.value });
    }
  };

  const photoFD = new FormData();
  photoFD.append("title", photo.title);
  photoFD.append("photo", photo.photo);

  const uploadPhoto = () => {
    // 기존 방식으로는 파일 인코딩이 불가하니, 인코딩 방식을 바꿔야 함.
    axios
      .post("http://localhost:1123/photo.upload", photoFD, {
        headers: { "Content-type": "multipart/form-data" },
        withCredentials: true,
      })
      .then((res) => {
        setResult(res.data);
        setPhoto({ title: "", photo: "" });
        photoInput.current.value = "";
      });
  };

  return (
    <div>
      <h1>파일 업로드</h1>
      제목 : <input value={photo.title} name="title" onChange={changePhoto} />
      <p />
      사진 :{" "}
      <input ref={photoInput} type="file" name="photo" onChange={changePhoto} />
      <p />
      <button onClick={uploadPhoto}>업로드</button>
      <h2>업로드한거 제목 : {result.title}</h2>
    </div>
  );
};

export default FileUpload;
