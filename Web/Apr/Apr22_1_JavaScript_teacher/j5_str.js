function strTest(){
    var a = "그래서 뭐가 글자가 있는데";
    alert(a);
    alert(a.length); // 글자수
    alert(a[1]); // 두번째 글자
    alert(a.indexOf("래")); // '래'는 몇번째에
    alert(a.indexOf("ㅋ") != -1); // 'ㅋ'가 있나
}