// JavaScript 유효성검사 라이브러리
// - 다양한 상황에 대응가능하게 최대한 일반적으로 제작
// - 부정적인 컨셉

// <input> 넣었을때
// 안썼으면 true, 썼으면 false -> 잘못된게 true
function isEmpty(field) {
    return !field.value;
}

// <input>, 최소글자수 넣었을때
// 짧으면, true, 안짧으면 false
function lessThan(field, len) {
    alert(field.value + " 글자수가 너무 짧음 " + field.value.length)
    return field.value.length < len;
}

document.joinForm.abc;
function isLimit(field) {
    return field.value.length;
}

// <input>, 최소글자수 넣었을때
// ID에 한글 못쓰게, 특수문자, 한자, 일본어, ...안됨
function containsHS(feield) {
    var set1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_@.";
    
    for( var i = 0; i< field.value.length; i++) {
        if(set1.indexOf(feield.value[i] == -1)) {
            return false;
        }    
    }
    return true;
}

// pw, pwChk 같은지?
function notEqual(feield1, feield2) {
    return feield1.value != feield2.value;
}

// <input> 넣었을때
// 숫자가 아니면 true
function notNotNum(feield) {
    return isNaN(feield.value) || (feield.value.indexOf(" ") != -1);
}

// pw조합
//  A : 소문자, 숫자
//  B : 대문자
//  C : 특수문자, 숫자
//  D : abc, 123
//  E : !@#, iop

// <input>, 문자열 세트를 넣었을 때.

function notContains(feield, set) {
    for( var i = 0; i< field.value.length; i++) {
        if(set.indexOf(feield.value[i] == -1)) {
            return false;
        }    
    }
    return true;
}



// 파일 종류 검사
