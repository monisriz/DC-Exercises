function positiveNumbers(numArray) {
  newArray = [];

  for (var i = 0; i < numArray.length; i++){
    if (numArray[i] >= 0) {
      newArray.push(numArray[i]);
    }
  }
  console.log(newArray);
}

positiveNumbers([1, -3, 5, -3, 0]);
