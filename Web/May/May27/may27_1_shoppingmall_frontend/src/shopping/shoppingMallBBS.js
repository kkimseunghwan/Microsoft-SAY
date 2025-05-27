import React, { useState } from "react";
import axios from "axios";
import styles from "./shoppingMallBBS.module.css";

const ShoppingMallBBS = () => {
  const [product, setProduct] = useState({
    name: "",
    price: "",
    description: "",
    image: null,
  });

  const productFD = new FormData();
  productFD.append("name", product.name);
  productFD.append("price", product.price);
  productFD.append("desc", product.description);

  const changeProduct = (e) => {
    setProduct({ ...product, [e.target.name]: e.target.value });
  };

  const regProduct = () => {
    axios
      .post("http://195.168.9.143:1125/weather.reg", productFD, {
        withCredentials: true,
      })
      .then((res) => {
        alert(JSON.stringify(res.data));
      });
  };

  const handleFileChange = (e) => {
    setProduct((prev) => ({
      ...prev,
      image: e.target.files[0],
    }));
  };

  return (
    <div className={styles.container}>
      <h2 className={styles.title}>상품 등록</h2>
      <table className={styles.formTable}>
        <tbody>
          <tr>
            <td>
              <input
                className={styles.input}
                name="name"
                value={product.name}
                onChange={changeProduct}
                placeholder="상품명"
                autoComplete="off"
                maxLength={20}
              />
            </td>
          </tr>
          <tr>
            <td>
              <input
                className={styles.input}
                name="price"
                value={product.price}
                onChange={changeProduct}
                placeholder="가격"
                type="number"
              />
            </td>
          </tr>
          <tr>
            <td>
              <textarea
                className={styles.textarea}
                name="description"
                value={product.description}
                onChange={changeProduct}
                placeholder="상품 설명"
              />
            </td>
          </tr>
          <tr>
            <td>
              <div className={styles.fileUpload}>
                <label htmlFor="image">이미지 선택</label>
                <input
                  id="image"
                  type="file"
                  accept="image/*"
                  onChange={handleFileChange}
                />
                {product.image && (
                  <span className={styles.fileName}>{product.image.name}</span>
                )}
              </div>
            </td>
          </tr>
          <tr>
            <td>
              <button className={styles.button} onClick={regProduct}>
                상품 등록
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default ShoppingMallBBS;
