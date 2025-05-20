import { useState } from "react";

// React : JS OOP Library
// 객체를 만들려면 class가 필요
//  -> React 측에서 class보다 function쪽을 권장
//  -> 그래서 나온게 Hooks
//  -> 함수형 컴포넌트에서 상태 관리를 할 수 있게 해주는 기능

// 객체 (class)
//      속성 (멤버변수)
//      맥션 (메소드)
//      객체가 만들어질 때 뭐시기 어쩌고 (생성자)
//      -> 저런것들이 함수에 있을 수 있나?
//      -> React 측에서 Hook이라는걸 제공해줘서 저런 느낌 나게 함.

// useState : 멤버 변수 + 멤버변수 값을 바꿀 수 있는 메소드 
const HwanHookFirst = () => {
    // const [멤버변수, 멤버변수 값을 바꿀 수 있는 메소드] = useState(멤버변수의 초기값);
    const [count, setCount] = useState(0);
    
    return (
        <>
            <h1>{count}</h1>
            <button onClick={() => setCount(count + 1)}>버튼</button>
        </>
    );
};

export default HwanHookFirst;