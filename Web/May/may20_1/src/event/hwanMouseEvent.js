import React, { useState } from 'react';

const HwanMouseEvent = () => {
    
    const divCss = { width: 200, height: 200, border: "black solid 2px"};
    const [moveInfo, setMoveInfo] = useState('');
    const [xyInfo, setXyInfo] = useState('');
    const [clickInfo, setClickInfo] = useState('');



    return (
        <>
        <h1>마우스 이벤트</h1>

        <div
            style={divCss}
            onMouseEnter = {() => {
                setMoveInfo('Mouse Enter');
            }}

            onMouseMove = {(e) => {
                // e.clientX, e.clientY : HTML 기준
                // setXyInfo('HTML기준 : ' + e.clientX + ' , ' + e.clientY);

                // e.nativeEvent.offsetX, e.nativeEvent.offsetY : 객체 기준
                setXyInfo('객체기준 : ' + e.nativeEvent.offsetX + ' , ' + e.nativeEvent.offsetY);
            }}

            onMouseLeave = {() => {
                setMoveInfo('Mouse Leave');
            }}

            onMouseDown = {(e) => {
                setClickInfo('Mouse Down : ' + e.button);

            }}

            onMouseUp = {(e) => {
                setClickInfo('Mouse Up : ' + e.button);
            }}
            
        ></div>
        <h2>{moveInfo}</h2>
        <h2>{xyInfo}</h2>
        <h2>{clickInfo}</h2>
        </>
    );
};

export default HwanMouseEvent;