var user = confirm("계속할까요?");
if(user == true){
    document.write("확인 버튼을 눌렀습니다.")
}
else{
    document.write("취소 버튼을 눌렀습니다.")
}

document.write("<br>")

user = prompt("아이디를 넣으세요", "admin"); // 기본값 : admin
document.write(user);