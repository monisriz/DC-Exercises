// Counter 2
// Allow the caller of counter to initialize the count to the first argument that's passed in.

function mainCounter (x) {
  var count = x;
  var counter = function () {
    count++;
    return count;
  };
  return counter;
};

var count1 = mainCounter(4);

console.log(count1());
console.log(count1());
