function test() {
    alert("ㅋ");
}

function forTest() {
    // for (변수초기화;조건식;증감) {
    // }
    for (var a = 1; a < 5; a++) {
        alert(a);
    }
}

function whileTest(){
    while (true) {
        var r = Math.random(); // 0.0 ~ 1.0
        alert(r);
        if (r > 0.3) {
            break;
        }
    }
}