import React, { useState } from 'react';

// 1) Kekeke 에는 color 속성이 있고, 바꾸는 함수, 기본값은 black
// class Kekeke():
//     def __init__(self):
//         self.color = 'black';
//
//     def changeColor(self, color):
//         self.color = color;
//
// 2) Kekeke의 color 속성을 input의 내용에 연동
// 3) h1의 배경색을 color 속성에 연동


const Kekeke = () => {

    // color 속성이 있고, 기본값은 black
    // input의 내용에 연동
    const [colorBG , setColorBG ] = useState("white")
    const [colorText , setColorText ] = useState("black")
    
    // 3) h1의 배경색을 color 속성에 연동
    const [color , setColor] = useState({"BG": "white", "Text": "black"})
    
    const changeBG = (e) => {
        setColorBG(e.target.value)
    }

    const changeText = (e) => {
        setColorText(e.target.value)
    }

    const changeColor = () => {
        setColor({
            "BG": colorBG,
            "Text": colorText
        })
    }
    
    return (
        <>
            {/* CSS를 JS 객체 형태로 작성. 속성명은 낙타 표기법 */}
            <h1 style={{backgroundColor:color["BG"], color:color["Text"]}}>COlOR</h1>
            배경색 : <input value={colorBG} onChange={changeBG}/> <br />
            글자색 : <input value={colorText} onChange={changeText}/> <br />
            <button onClick={changeColor}>색 변경하기</button>
        </>
    )
}

export default Kekeke;