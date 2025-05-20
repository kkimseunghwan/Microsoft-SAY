import React, { useState } from 'react';

const HwanKeyEvent = () => {
    const [eventInfo, setEventInfo] = useState('');
    const [keyInfo, setKeyInfo] = useState('');

    return (
        <>
            <input 
                onKeyDown={(e) => {
                    setKeyInfo(e.key);
                    setEventInfo("keyDown");
                }}

                onKeyUp={(e) => {
                    setKeyInfo(e.key);
                    setEventInfo("keyUp");
                }}
            />
            <h2>{eventInfo}</h2>
            <h2>{keyInfo}</h2>
        </>
    );
};

export default HwanKeyEvent;