//Counter 3
// Allow the counter to either increment 1 or decrement by 1 by calling the
// increment and decrement methods, respectively. Note: now the counter needs to
// return an object rather than a function.

function mainCounter (x) {
  var count = x;

  function increment () {
    count+=1;
    return count;
  };

  function decrement () {
    count-=1;
    return count;
  };
  return {
    increment: increment,
    decrement: decrement
  };
};

var count = mainCounter(4);

console.log(count.increment());
console.log(count.decrement());
