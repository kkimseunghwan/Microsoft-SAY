// 객체(Component)를 만들려면 -> 클래스 
// -> React측에서 클래스보다는 함수형 Component를 권장하는 쪽으로 바뀜

// rafce 단축키 하면 밑에 함수 만들어짐
import React from 'react'

// JSX(JavaScript Xml)
//      html아님, html비슷하게 생긴 xml
//      무조건 하나가 리턴되어야함 -> 여러개 쓰려면 <></> 이렇게 해주면 어러개 가능
//      DOM객체 풀 세트 형태여야함
//          -> 원래 풀 세트 아닌 것들은 -> </태그명> 이렇게 닫아줘야함
//      속성 값 자리에 문자열 넣으려면 -> "문자열" 이렇게 넣어야함
//      {JS문법 }

    // <MyH1></MyH1>
    // <MyH1></MyH1>
    // <MyH1></MyH1>
    // <MyH1></MyH1>
// 이런거 안됨 -> 그래서 <div> 로 감싸줘도되고 -> 아니면 <></> 이렇게 해주면 어러개 가능

const MyH1 = () => {
    return (
    <h1>ㅋㅋㅋ</h1>
    )
}


export default MyH1;