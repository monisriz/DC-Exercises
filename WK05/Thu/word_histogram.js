// Word Histogram
//
// Write a function wordHistogram which takes a string as argument and tallies
// the number of times each word appears in the string, and returns the tally as
// an object. Example:
//
// > wordHistogram('to be or not to be')
// { to: 2, be: 2, or: 1, not: 1 }

function wordHistogram(str) {
  str = str.toLowerCase().split(" ");
  wordCount = {};
  for (var word = 0; word < str.length; word++) {
    if (str[word] in wordCount) {
      wordCount[str[word]] += 1;
    }
    else {
      wordCount[str[word]] = 1;
    };
  };
  return wordCount;
};

console.log(wordHistogram('to be or not to be'));
