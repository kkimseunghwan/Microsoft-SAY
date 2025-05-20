import { useState } from 'react';

const HwanEventFirst = () => {

    // 사용자 입력 데이터 저장
    const [human, setHuman] = useState({
        name: '',
        height: '',
        weight: '',
        bmi: '',
        result: ''
    });

    // INPUT 한 번에 처리
    const changeHuman = (e) => {
        setHuman({ ...human, [e.target.name]: e.target.value});
    }

    // BMI 게산식 : 몸무게(kg) / 키(m)의 제곱
    const bmiCalcul = () => {
        const bmiRes = human.weight / ((human.height * 0.01) * (human.height * 0.01))
                
        if (bmiRes < 18.5) {
            setHuman({ ...human, "bmi": bmiRes, "result": '저체중'});
        } else if (bmiRes < 23) {
            setHuman({ ...human, "bmi": bmiRes, "result": '정상'});
        } else if (bmiRes < 25) {
            setHuman({ ...human, "bmi": bmiRes, "result": '과체중'});
        } else if (bmiRes < 35) {
            setHuman({ ...human, "bmi": bmiRes, "result": '비만'});
        } else {
            setHuman({ ...human, "bmi": bmiRes, "result": '고도비만'});
        }
    }

    return (
        <div className="bmi-calculator-container">
            <h1>BMI 계산기</h1>
            이름 : <input id="name" name="name" type="text" value={human.name} onChange={changeHuman} /> <br />
            키 : <input name="height" type="text" value={human.height} onChange={changeHuman} /> <br />
            몸무게 : <input name="weight" type="text" value={human.weight} onChange={changeHuman} /> <br />
    
            <button onClick={bmiCalcul} >계산</button>
    
            <hr />
    
            <h2>BMI 결과</h2>
            <p><strong>BMI :</strong> {human.bmi ? human.bmi.toFixed(2) : 'N/A'}</p>
            <p><strong>결과 :</strong> {human.result || 'N/A'}</p>
        </div>
    );
};

export default HwanEventFirst;