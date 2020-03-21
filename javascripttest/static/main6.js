function func(){
    var season = prompt("좋아하는 계절을 입력하세요", "봄, 여름, 가을, 겨울 중에 선택하세요");
    var message = "";
    var img = "";

    switch(season){ // season에는 숫자(정수), 문자, 문자열만 입력 가능
        case "봄":
            message = "봄을 좋아하시네요!";
            img = "img01.jpg";
            break;
        case "여름":
            message = "여름을 좋아하시네요!";
            img = "img02.jpg";
            break;
        case "가을":
            message = "가을을 좋아하시네요!";
            img = "img03.jpg";
            break
        case "겨울":
            message = "겨울을 좋아하시네요!";
            img = "img04.jpg";
            break;
        default:
            alert("올바른 값이 아닙니다.");
    }
    ep = document.getElementById("message").innerHTML = message;
    ep = document.getElementById("img").src = "/static/img/" + img;
}