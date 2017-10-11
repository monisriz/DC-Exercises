function madlib(name, subject) {
  var statement = `${name}'s favorite subject is ${subject}.`;
  return(statement);
}

console.log(madlib('Monis', 'JavaScript'));
