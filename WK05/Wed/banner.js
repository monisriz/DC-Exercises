function printBanner(bannerText) {
  var char = "";
  var len = bannerText.length;

  for (var i = 0; i < len+4; i++) {
    char += "*";
  }
  console.log(char);
  console.log("* " + bannerText + " *");
  console.log(char);
}

printBanner("Welcome to DigitalCrafts");
