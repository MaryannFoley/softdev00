/*Team MAD - Anton Danylenko, Maryann Foley
SoftDev1 pd8
K28 -- Sequential Progression
2018-12-18
*/

var fibonacci = (n) => {
  if (n == 0)
    return 0;
  else if (n == 1)
    return 1;
  else
    return fibonacci(n - 2) + fibonacci(n - 1);
};

var gcd = (a, b) => {
  if (a > b) {
    for (x = b; x > 0; x--)
      if (((a % x) == 0) && ((b % x) == 0))
        return x;
  }
  else {
    for (x = a; x > 0; x--)
      if (((a % x) == 0) && ((b % x) == 0))
        return x;
  }
}

var students = ["bob", "sally", "john", "john2"];

var randomNumber = () => {
  return Math.floor(Math.random() * 3)
}
var randomStudent = () => {
  randIndex = randomNumber();
  return students[randIndex];
}

var b0 = document.getElementById("b0");
var b1 = document.getElementById("b1");
var b2 = document.getElementById("b2");
var p0 = document.getElementById("p0");
var p1 = document.getElementById("p1");
var p2 = document.getElementById("p2");
b0.addEventListener('click', function(){
  console.log(fibonacci(5));
  p0.innerHTML=fibonacci(5);
});
b1.addEventListener('click', function(){
  console.log(gcd(15, 255));
  p1.innerHTML=gcd(15, 255);
});
b2.addEventListener('click', function(){
  console.log(randomStudent());
  p2.innerHTML=randomStudent();
});