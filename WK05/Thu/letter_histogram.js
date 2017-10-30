// Letter Histogram

// Write a function letterHistogram which takes a string as argument.
// It will tally(histogram) the number of times each character appears in
// the string, and return the tally as an object. Example:
//
// letterHistogram('bananas')
// { b: 1, a: 3, n: 2, s: 1 }
// Note: the order of the keys doesn't matter.

function letterHistogram(str) {
  str = str.toLowerCase();
  var letterCount = {};
  for (var char = 0; char < str.length; char++) {
    if (str[char] in letterCount) {
      letterCount[str[char]] += 1;
    }
    else {
      letterCount[str[char]] = 1;
    };
  };
  return letterCount;
};

console.log(letterHistogram('bananas'));
