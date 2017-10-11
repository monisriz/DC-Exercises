function totalAmount(billAmt, svcLevel) {
  if (svcLevel == 'good') {
    tipLevel = 0.20;
  }
  else if (svcLevel == 'fair') {
    tipLevel = 0.15;
  }
  else {
    tipLevel = 0.10;
  }
  var tipAmt = billAmt * tipLevel;
  var totalAmt = billAmt + tipAmt;
  return(totalAmt);
}

console.log(totalAmount(100, 'good'))
