import React, { useReducer, useState } from "react";

//setter역할 할 함수.
const doFlagGame = (state, action) => {
    if(state === "시작") {
        state = "";
    }

    if(action === "청기올려") {
        return state + "청기올려";
    } else if(action === "청기내려") {
        return state + "청기내려";
    } else if(action === "백기내려") {
        return state + "백기내려";
    } else if(action === "백기올려") {
        return state + "백기올려";
    }
};

// useReducer : 멤버변수 + 멤버변수값 바꿀 수 있는 메서드 (setter)
//              + setter에 변화 (단순히 바꾸기만 하는 거 이상의: 조건문, 반복문, 예외처리 등)
//              + 정리효과

const HwanHookSecond = () => {
    // const [멤버변수, setState] = useReducer(함수, 초기값);
    // setter역할 할 함수를 호출하면 setState가 호출되고, 그 함수의 인자로 넘어가는 값이 멤버변수에 저장된다.
    const [history, setHistory] = useReducer(doFlagGame, "시작");


    return (
        <>
            <h1>{history}</h1>
            <button onClick={() => setHistory("청기올려")}>청기올려</button>
            <button onClick={() => setHistory("청기내려")}>청기내려</button>
            <button onClick={() => setHistory("백기내려")}>백기내려</button>
            <button onClick={() => setHistory("백기올려")}>백기올려</button>
        </>
    );
};

export default HwanHookSecond;