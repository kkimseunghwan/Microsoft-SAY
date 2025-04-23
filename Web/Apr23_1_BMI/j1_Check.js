function check() {
    var nameField = document.joinForm.name;
    var h_Field = document.joinForm.height;
    var w_Field = document.joinForm.weight;
    var psaField = document.joinForm.profile;

    //이름 입력 확인
    if (isEmpty(nameField) || lessThan(nameField, 2) ) {
        alert("이름 재확인");
        nameField.value = "";
        nameField.focus();
        return false;
    }

    // 키 입력 확인
    if (isEmpty(h_Field) || lessThan(h_Field, 2) || isNotNum(h_Field)) {
        alert("키 재확인");
        h_Field.value = "";
        h_Field.focus();
        return false;
    }

    // 몸무게 입력 확인
    if (isEmpty(w_Field) || lessThan(w_Field, 2) || isNotNum(w_Field)) {
        alert("몸무게 재확인");
        w_Field.value = "";
        w_Field.focus();
        return false;
    }

    // 사진 검사
    if(isEmpty(psaField) || 
        (isNotType(psaField, "jpg")
        && isNotType(psaField, "gif")
        && isNotType(psaField, "png")
        && isNotType(psaField, "bmp"))) 
    {
        alert("프사 재확인");
        psaField.value = null;
        return false;
    }

    return true;
}