t1 = null
t2 = null

function show() {
// var a = document.getElementById("fno").value;
// var b = document.getElementById("sno").value;
// var r = a * b
// s = document.getElementById("result")
// s.innerHTML = ("Product is" + r)
t1 = setTimeout(f1, 0)
t2 = setInterval(f2, 1000)
let sec=f2();

}

function f3() {
setTimeout(f1, 1000)
setInterval(f2, 1000)
}

function f1() {
var d = document.getElementById("secretdiv")
d.style.display = "block"
}
min = 0
sec = 0

// function stop() {
// clearInterval(t2)
// return t2
// alert(t2)
// }

function f2() {

  sec++;

 msg =   sec
 var d = document.getElementById("secretdiv")
 d.innerHTML = msg;
return sec;
}