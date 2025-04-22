function check() {
    var idField = document.joinForm.id; 
    var pwField = document.joinForm.pw;
    var pwChkField = document.joinForm.pwChk;
    var ageField = document.joinForm.age;
    
    alert("ID " + idField.value)
    alert("ID isEmpty " + isEmpty(idField))
    alert("ID lessThan " + lessThan(idField, 4))
    alert("ID containsHS " + containsHS(idField))

    if (isEmpty(idField) || lessThan(idField, 4) || containsHS(idField)) {
        alert("ID?");
        idField.value = "";
        idField.focus();
        return false;
    }


    alert(pwField.value)
    alert(pwChkField.value)
    alert(ageField.value)




    if(isEmpty(pwField) || lessThan(pwField, 5) 
        || notEqual(pwField, pwChkField)
        || notContains(pwField, "1234")
        || notContains(pwField, "abcd")) 
    {
        alert("PW?");
        pwField.value = "";
        pwField.focus();
        return false;
    }

    if (isEmpty(ageField) || notNotNum(ageField)) {
        alert("AGE?");
        ageField.value = "";
        ageFieldidField.focus();
        return false;
    }

    return true;
}