function func(){
    var num = prompt("숫자를 입력하세요", "100");
    var sum = 0;
    for(i = 0; i <= num; i++){
        sum = sum + i;
    }
    document.write("합계 : " + sum);
}
