import React, { useState } from 'react';

const HwanRSFourth = () => {

    const [snack, setSnack] = useState([
        {name: '치즈볼', price: 1500},
        {name: '치즈퐁듀', price: 2000},
        {name: '쿠크다스', price: 2500},
        {name: '오징어땅콩', price: 1700},
        {name: '콘치즈', price: 1800}
    ]);

    // const sortedSnack = snack.sort((a, b)) // 기본형급. 오름차순
    const sortedSnack = snack.sort((a, b) => {
        if (a.price > b.price) {
            return -1;
    }
        return -1;
    }); // 객체급 or 기본형급   이지만, 다른 순서

    const snackTrs = sortedSnack.map((s, i) => (
        <tr>
            <td>{s.name}</td>
            <td>{s.price}</td>
        </tr>
    ));

    return (
        <div>
            <h1>HwanRSFourth</h1>       
        </div>
    )
}

export default HwanRSFourth;