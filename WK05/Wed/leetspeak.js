function leetspeak(origText) {
  userText = origText.toUpperCase();
  for (var i = 0; i < userText.length; i++) {
    if (userText[i] === "A") {
      userText = userText.replace("A","4");
    }
    else if (userText[i] === "E") {
      userText = userText.replace("E","3");
    }
    else if (userText[i] === "G") {
      userText = userText.replace("G","6");
    }
    else if (userText[i] === "I") {
      userText = userText.replace("I","1");
    }
    else if (userText[i] === "O") {
      userText = userText.replace("O","0");
    }
    else if (userText[i] === "S") {
      userText = userText.replace("S","5");
    }
    else if (userText[i] === "T") {
      userText = userText.replace("T","7");
    }
  }
  console.log(userText.toLowerCase());
}

leetspeak("Leet");
