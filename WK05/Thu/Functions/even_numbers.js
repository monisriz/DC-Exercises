//Even Numbers
//
// Write a function which takes an array of numbers as input and returns a
// new array containing only the even numbers in the given array.

var numArray = [1, 2, 3, 4];
function evenNumbers (num) {
  return num % 2 == 0;
};
console.log(numArray.filter(evenNumbers));
