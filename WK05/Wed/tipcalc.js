function tipAmount(billAmt, svcLevel) {
  if (svcLevel === 'good') {
    tipLevel = 0.20;
  }
  else if (svcLevel === 'fair') {
    tipLevel = 0.15;
  }
  else {
    tipLevel = 0.10;
  }
  return(billAmt * tipLevel);
}

console.log(tipAmount(100, 'fair'));
