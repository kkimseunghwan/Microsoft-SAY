import React, { useState } from 'react';
import './snackBBS.css';

// <div></dic> 대신 쓰라고 React 에서 제공하는 태그 : <></>
const SnackBBS = () => {

    const [snackData, setSnackData] = useState({ name: "", price: ""});
    const [snackList, setSnackList] = useState([]);

    const btnEvent = () => {
        if (snackData.name === "" || snackData.price === "") {
            alert("이름과 가격을 입력해주세요.");
            return;
        }
        alert(JSON.stringify(snackData));
        setSnackList([...snackList, snackData]);

        setSnackData({ name: "", price: ""});
    }

    const changeName = (e) => {
        setSnackData({...snackData, name: e.target.value});
    }

    const changePrice = (e) => {
        setSnackData({...snackData, price: e.target.value});
    }

    // table 리스트 추가
    const setTableList = () => {
        return snackList.map((item, index) => {
            return (
                <tr id={index} onClick={deleteEvent} class='snackList'>
                    <td>{item.name}</td>
                    <td>{item.price}</td>
                </tr>
            )
        })
    }

    const deleteEvent = (e) => {
        // 해당 태그 내의 키 데이터
        const sncakIndex = e.currentTarget.id;
        const snackListValue = [...snackList];
        snackListValue.splice(sncakIndex, 1);
        setSnackList(snackListValue);
    }

    return (
        <div id='snackArea'>
            <h1>SnackBBS</h1>
            이름 : <input className="txtTypeInput" type="text" value={snackData.name} onChange={changeName} /> <br />
            가격 : <input className="txtTypeInput" type="text" value={snackData.price} onChange={changePrice} /> <br />
            <button onClick={btnEvent}>등록</button>

            <hr />

            <table id='snackBBSTable'>
                <tr>
                    <th>이름</th>
                    <th>가격</th>
                </tr>
                {/* 위에서 등록 버튼 누를 시, 이 테이블에 해당 데이터가 추가됨 */}
                {/* 그리고 해당 리스트를 클릭 시, 해당 행은 삭제됨 */}
                
                {setTableList()}
            </table>

        </div>
    );
};

export default SnackBBS;