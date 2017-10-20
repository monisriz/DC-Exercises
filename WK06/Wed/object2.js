// Inheritance

var mom = {
  firstName: 'Alice',
  lastName: 'Wong',
  eyeColor: 'brown',
  hairColor: 'black'
};
var daughter = {
  firstName: 'Ilene',
  hairColor: 'brown'
};

// One

daughter.__proto__ = mom;
console.log(daughter);
// console.log(daughter.lastName);
// console.log(daughter.eyeColor);
// console.log(daughter.hairColor);
