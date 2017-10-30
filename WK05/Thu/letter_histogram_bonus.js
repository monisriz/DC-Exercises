// Bonus
//
// Print the top 2 most frequently used letters in the string from the
// letter histogram exercise.

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

var countObj = letterHistogram('bananas');
var sortedObj = Object.keys(countObj).sort(function(a,b) {
  return countObj[a]-countObj[b];
});

// console.log(countObj);
sortedObj.reverse();
console.log(`Two most used letters in the given string are ${sortedObj[0]} and ${sortedObj[1]}.`);
