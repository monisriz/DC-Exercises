// Sum an array
//
// Write a function sum that takes an array of numbers as argument and
// returns the sum of those numbers. Use the reduce method to do this.

var numArray = [1, 2, 3, 4];
var res = numArray.reduce(function (total, num) {
            return total + num;
          });
console.log(res);
