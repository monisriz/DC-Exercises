function longvowels(origString) {
  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var userString = origString.toLowerCase();

  for (var i = 0; i < userString.length; i++) {
    for (var j = 0; j < vowels.length; j++) {
      if (userString[i] == vowels[j] && userString[i+1] == userString[i]) {
        var newString = userString.replace(userString[i], vowels[j].repeat(4));
      }
    }
  }
  console.log(newString);
}

longvowels("door");
