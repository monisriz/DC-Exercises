function letterHistogram(str) {
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
