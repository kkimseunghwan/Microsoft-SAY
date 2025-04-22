
function test() {
    alert("zzz")
}

function forTest() {
    for(var i=0; i <= 5; i++) {
        alert("For "+i)
    }

}

function whileTest() {
    
    while(true) {
        var r = Math.random(); // 0.0 ~ 0.99999999
        alert("while random " + r);
        if( r > 0.5) {
            break;
        }

    }
}