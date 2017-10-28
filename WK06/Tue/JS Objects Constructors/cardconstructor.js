// Card constructor
class Card {
  constructor(name, point, suit) {
    this.name = name;
    this.point = point;
    this.suit = suit;
  };
// Get card image url
  getImageUrl () {
    var url = `images/${this.name}_of_${this.suit}.png`;
    return url
  };
};
// Hand constructor
class Hand {
  constructor(hand) {
    this.hand = [];
  };
// Add a card to the empty array (this.hand) above
  addCard(card) {
    return this.hand.push(card);
  };
// Get a total of points of the cards in the array (this.hand)
  getPoints() {
    var totalPoints = 0;
    for (var i=0; i < this.hand.length; i++) {
      totalPoints += this.hand[i].point;
    };
    return totalPoints;
  };
};
// Deck constructor
class Deck {
  constructor() {
    this.deck = [];
  };
  generate_deck() {
    var name = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king'];
    var suit = ['clubs', 'diamonds', 'hearts', 'spades'];
    for (var i=0; i < name.length; i++) {
      for (var j=0; j < suit.length; j++) {
        if (name[i] === 'jack' || name[i] === 'queen' || name[i] === 'king') {
          this.deck.push(new Card(name[i], 10, suit[j]));
        }
        else {
          this.deck.push(new Card(name[i], i+1, suit[j]));
        };
      };
    };
  };

  shuffleDeck(deck) {
      for (var i = this.deck.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var temp = this.deck[i];
          this.deck[i] = this.deck[j];
          this.deck[j] = temp;
      };
      return deck
  };

};

var myHand = new Hand();
var card1 = new Card('5', 5, 'diamonds');
var card2 = new Card('queen', 10, 'clubs');
myHand.addCard(card1);
myHand.addCard(card2);
console.log(myHand.getPoints());
console.log(card2.getImageUrl());
