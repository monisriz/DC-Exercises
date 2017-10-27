// function Person(name) {
//   this.name = name;
//   this.friends = [];
// }
//
// Person.prototype.addFriend = function(friend) {
//   this.friends.push(friend);
// };
//
// Person.prototype.createGreeting = function(other) {
//   return 'Yo ' + other.name + '! from ' + this.name + '.';
// };
//
// Person.prototype.greet = function(other) {
//   console.log(this.createGreeting(other));
// };

class Person {
  constructor(name) {
    this.name = name;
    this.friends = [];
  };

  addFriend(friend) {
    this.friends.push(friend);
  };

  createGreeting(other) {
    return 'Yo ' + other.name + '! from ' + this.name + '.';
  };

  greet(other) {
    console.log(this.createGreeting(other));
  };

  lazyGreet(other) {
    // var self = this;
    setTimeout(() => { this.greet(other) }, 2000);
  };
};

var monis = new Person('Monis');
var paul = new Person('Paul');
monis.lazyGreet(paul);

// These thises
// Given the Person type given in the last problem, add to it a lazyGreet
// method which will print out the same greeting message but only after
// 2 seconds.
