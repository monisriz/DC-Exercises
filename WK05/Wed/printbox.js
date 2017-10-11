function printBox(w, h) {
  console.log("*".repeat(w));
  for (var i = 0; i < h-2; i++) {
    console.log("*" + " ".repeat(w-2) + "*");
  }
  console.log("*".repeat(w));
}
printBox(6, 4);
