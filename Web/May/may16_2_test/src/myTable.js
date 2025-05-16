import React, { useState } from 'react';

// vanillaJS / jQuery = 버튼을 눌렀을 때, 그 시점의 input에 적혀있는 내용을 출력
// react = state(상태)를 상시 업데이트
// 버튼을 눌렀을 때, 그 시점의 state를 출력

// OOP란
// 속성 : 멤버변수
// 기능 : 메서드

// class를 만들려고 했으나, react에서는 함수 형태를 권장해서 함수를 만들어서 사용
//      -> 단순 함수에서 멤버변수/메서드 표현은 불가
//      -> react에서 hook이라는 것을 제공해서 클래스 처럼 쓸 수 있게 해줌
//      -> 클래스 처럼 쓰려면 함수 안에서 멤버변수/메서드 표현 가능

// 함수
const MyTable = () => {
    // 멤버변수 느낌 - useState
    // const [맴버변수, setter(멤버 변수에 값 넣을 때 쓰는 함수)] = useState(초기값)
    // useState import 필요
    // useStae로 자동 완성 -> import
    // -> useStateSnippet 자동 완성 진행

    const [inputValue, setInputValue] = useState('초기값'); 
    
    // 메서드 느낌
    const showAlert = () => {
        alert('버튼 클릭됨');
    }

    // 메서드 느낌
    const showInputval = () => {
        alert(inputValue);
    }

    return (
        <table border="1">
            <tr>
                <td>1</td>
                <td>
                    <button onClick={showAlert}>버튼</button>
                </td>
                <td>
                    <input value={inputValue} onChange={(e) => setInputValue(e.target.value)} />
                    <button onClick={showInputval}>input에 쓴거 출력</button>

                </td>
            </tr>
        </table>
    )
}

export default MyTable;
