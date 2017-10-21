// Inheritance

// One
// Write code to make daughter inherit properties from mom. What are the daugther's properties and their values? Print them out.
//
// Two
// Add a method called showInfo to mom by attaching a function to it as a property. Calling this method will print out all four properties. Call this method on both mom and daugther.



var mom = {
  firstName: 'Alice',
  lastName: 'Wong',
  eyeColor: 'brown',
  hairColor: 'black',
  showInfo: function() {
    console.log(`First name: ${this.firstName}, Last name: ${this.lastName}, Eye color: ${this.eyeColor}, Hair color: ${this.hairColor}`);
  }
};
var daughter = {
  firstName: 'Ilene',
  hairColor: 'brown'
};

// One
daughter.__proto__ = mom;
console.log(daughter.firstName);
console.log(daughter.lastName);
console.log(daughter.eyeColor);
console.log(daughter.hairColor);

// Two
mom.showInfo();
daughter.showInfo();
