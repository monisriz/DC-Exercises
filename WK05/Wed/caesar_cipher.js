function cipher(userStr, offset) {
  for (var i = 0; i < userStr.length; i++) {
    var cipherStr = "";
    var getCode = userStr.charCodeAt(i);
    var getChar = String.fromCharCode;

// to test uppercase characters
    if (getCode >= 65 && getCode <= 90) {
        if (getCode + offset > 90) {
          cipherStr += getChar(getCode + offset - 26);
        }
        else {
          cipherStr += getChar(getCode + offset);
        }
    }
// to test lowercase characters
    else if (getCode >= 97 && getCode <= 122) {
        if (getCode + offset > 122) {
          cipherStr += getChar(getCode + offset - 26);
        }
        else {
          cipherStr += getChar(getCode + offset);
        }
    }
// to test non-letter characters
    else {
      cipherStr += getChar(getCode);
    }
    console.log(cipherStr);
  }
}

cipher("Genius without education is like silver in the mine", 13);
