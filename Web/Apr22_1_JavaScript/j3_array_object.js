

function arrayTest() {

    var a = [12, 43, 5467, 454];
    alert(a.length) // 갯수
    alert(a[0]) // index는 0번부터
    for(var i = 0; i < a.length ; i++) {
        alert(a[i]);
    }

    for (var i of a) {
        alert(i);
    }

}

function aoTest() {
    var dogs = [
        {name:"후추", age:3},
        {name:"후치", age:23},
        {name:"후차", age:13}

    ];

    for(var i of dogs) {
        alert(i.name)
        alert(i.age)
    }
}

