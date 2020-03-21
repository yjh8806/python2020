function gugu(){
    var dan = document.getElementById("dan").value;
    var str = "";
    for(var i = 1; i <= 9; i++){
        str += dan + "x" + i + "=" + dan*i + "<br>";
    }
    document.getElementById("result").innerHTML = str;
 // document.getElementById("result").innerText = str; -> text로 출력
}

function enter(){
    console.log(window.event.keyCode);
    if(window.event.keyCode == 13){
        gugu();
    }
}// 웹 개발자 모드의 console에서 enter입력 시 코드값(keyCode) 확인할 수 있음