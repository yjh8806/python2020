function calc(){
    var x = document.getElementById("x").value;
    var y = document.getElementById("y").value;
    sum = parseInt(x) + parseInt(y);
    document.getElementById("sum").value = sum;
}