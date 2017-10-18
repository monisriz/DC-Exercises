// Counter
// Make a counter function that returns a function
// that returns a successive number each time it is called.

function mainCounter () {
  var count = 0;
  var counter = function () {
    count++;
    return count;
  };
  return counter;
};

var count1 = mainCounter();
var count2 = mainCounter();

console.log(count1());
console.log(count1());
console.log(count2());
console.log(count2());
console.log(count1());
console.log(count2());
