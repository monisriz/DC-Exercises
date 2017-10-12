function decipher(cipherStr, offset) {
  for (var i = 0; i < cipherStr.length; i++) {
    var resultStr = "";
    var getCode = cipherStr.charCodeAt(i);
    var getChar = String.fromCharCode;

// to test uppercase characters
    if (getCode >= 65 && getCode <= 90) {
      if (getCode + offset < 65) {
        resultStr += getChar(getCode + offset - 26);
      }
      else {
        resultStr += getChar(getCode + offset);
      }
    }
// to test lowercase characters
    else if (getCode >= 97 && getCode <= 122) {
        if (getCode + offset < 97) {
          resultStr += getChar(getCode + offset + 26);
        }
        else {
          resultStr += getChar(getCode + offset);
        }
    }
// to test non-letter characters
    else {
      resultStr += getChar(getCode);
    }
    console.log(resultStr);
  }
}

decipher("Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar", -13);
