

// input 내용 받아다가
// reqParam 만들어서 요청
function gogo() {
    var nInput = document.getElementById(nameInput);
    var aInput = document.getElementById(ageInput);

    //Get 방식 요청
    location.href = "http://localhost/te.st?name=" + nInput.value + "&age=" + aInput.value;


}
