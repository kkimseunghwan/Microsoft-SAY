// form없이 
// button누르면
// input 내용 받아다가 
// reqParam만들어서 요청
function gogo(){
    // document : 이 html
    var nInput = document.getElementById("nameInput");
    var aInput = document.getElementById("ageInput");
    
    // GET방식 요청
    location.href = "http://localhost/te.st?name=" + nInput.value
                    + "&age=" + aInput.value;
    // 불편한데요? jQuery/react
    // POST는요? JS로 form을 만들어서...
}