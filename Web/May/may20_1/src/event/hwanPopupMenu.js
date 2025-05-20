import React, { useState } from 'react';
import {ContextMenuTrigger, ContextMenu, MenuItem} from 'react-contextmenu';
// npm install 이름 = Node.js
// yarn add 이름 = React
//
// yarn add react-contextmenu

const HwanPopupMenu = () => {
    
    // ContextMenuTrigger 영역에 마우스를 우클릭하면
    // ContextMenu 영역이 나오는 형태

    return (
        <>
            <ContextMenuTrigger id="popupMenu">
                <div style={{width: 200, height: 200, backgroundColor: 'red'}}></div>
            </ContextMenuTrigger>

            <ContextMenu id="popupMenu">
                <MenuItem>
                    <a href='https://naver.com'>네이버</a>
                </MenuItem>
                <MenuItem>
                    <a href='https://daum.net'>다음</a>
                </MenuItem>
                <MenuItem>
                    <a href='https://google.com'>구글</a>
                </MenuItem>
            </ContextMenu>
        </>
    );
};

export default HwanPopupMenu;