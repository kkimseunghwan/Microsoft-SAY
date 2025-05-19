import React, { useState } from 'react';

const HwanRSThird = () => {
    const [nnn, setNnn] = useState([56, 11, 22, 567, 678]);

    // 배열 필터링 : filter
    //      배열 차례대로 탐색, 뭐 하나 만날때마다 콜백함수 호출
    //      콜백 함수 속에서 조건문을 써서 true/false 리턴
    //      조건문이 true인 경우만 해당 요소를 배열에 포함시킴
    const filtered = nnn.filter((n) => (n%2 === 0));
    
    const marquees = filtered.map((n, i) => (
        <marquee behavior="alternate">{n}</marquee>
    ));

    return <div>{marquees}</div>
}

export default HwanRSThird;