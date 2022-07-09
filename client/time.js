let timein, hrs, min, sec;
function timeIn() {
  timein = new Date().getTime();
  let d = new Date(timein);
  sec = d.getSeconds();
  min = d.getMinutes();
  hrs = d.getHours();
  hrs = hrs.toString().padStart(2, "0");
  min = min.toString().padStart(2, "0");
  sec = sec.toString().padStart(2, "0");
  alert(`input time is ${hrs}hrs ${min}min ${sec}sec`);
}
let seconds;
function timeOut() {
  let s = new Date().getTime();
  let diff = s - timein;
  console.log(diff);
  seconds = diff / 1000;
  // let min=sec/60;
  // let hrs=min/60;
  //   hrs=hrs%24;
  //   min=min%60;
  seconds = seconds % 60;
  //   hrs=hrs.toFixed(0);
  // min=min.toFixed(0);
  seconds = seconds.toFixed(0);
  alert(`Actual Time is ${seconds}sec`);
}
