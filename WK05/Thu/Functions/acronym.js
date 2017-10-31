// Acronym
//
// Write a function acronym that takes an array of words as argument and
// returns the acronym of the words. Use the reduce method to do this.

var wordArray = ['very', 'important', 'person'];
var res = wordArray.reduce(function (a, b) {
  return (a + b[0]).toUpperCase();
}, "");
console.log(res);
