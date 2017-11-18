document.addEventListener("DOMContentLoaded", function(){

var deck;

// blackjack buttons - bet, cancel, chip, deal, hit, stand
var chip = document.getElementsByClassName("chipButton");
var chipbuttons = document.getElementById("chipbuttons");
var controlbuttons = document.getElementById("controlbuttons");
var bet = document.getElementById("bet-button");
var cancel = document.getElementById("cancel-button");
var deal = document.getElementById("deal-button");
var hit = document.getElementById("hit-button");
var stand = document.getElementById("stand-button");

// ###########################
// ######### CLASSES #########
// ###########################

    // Create Person Class
    class Person {
        constructor (name){
            this.name = name;
            this.hand = [];
            this.points = 0;
            this.bet = 0;
            this.bank = 500;
            this.wins = 0;
            this.totalhands = 0;
        }

        // Calculates values of cards in hand
        calculateHand(){
            // Sorts cards highest to lowerst value
            this.hand.sort(function(a, b){
                return b.value - a.value;
            });
            // Calcute sum of cards in hand
            this.points = this.hand.reduce(function(sum, card){
            if (card.rank === "ace" && sum < 11){
                return sum + 11;
            };
            return sum + card.value;
            }, 0);
            document.getElementById(`${this.name}-points`).innerHTML = this.points;
        }
    };

    // Create Card Class
    class Card {
        constructor (value, rank, suit){
            this.value = value;
            this.rank = rank;
            this.suit = suit;
        }

        getCardImageURL(){
            return `images/cards/${this.rank}_of_${this.suit}.png`
        }
    };

    // Create Deck Class
    class Deck {
        constructor (){
            this.deckOfCards = [];
        }

        // Creates new deck of cards
        createNewDeck(){
            var suits = ['diamonds', 'clubs', 'hearts', 'spades'];
            var ranks = ['ace', '2', '3', '4', '5', '6',
                        '7', '8', '9', '10', 'jack', 'queen', 'king']

            // Create deck of cards, 52 cards in a deck
            for (var i = 0; i < suits.length; i++){
                for(var j = 0; j < ranks.length; j++){
                    if (ranks[j] === "jack" || ranks[j] === "queen" || ranks[j]=== "king"){
                        this.deckOfCards.push(new Card(10, ranks[j], suits[i]));
                    }
                    else {
                        this.deckOfCards.push(new Card(j + 1, ranks[j], suits[i]));
                    };
                };
            };
        };

        // Shuffle deck of cards
        shuffle(){
            for (let i = this.deckOfCards.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [this.deckOfCards[i], this.deckOfCards[j]] = [this.deckOfCards[j], this.deckOfCards[i]];
            };
        }

        dealCard(person){
            let image = document.createElement("img");
            // Retrieve card from deckOfCards
            let card = deck.deckOfCards.pop();
            // reshuffles deck if found empty
            if (deck.deckOfCards.length === 0){
                deck.createNewDeck();
                deck.shuffle();
            };
            // Add card to hand
            person.hand.push(card);
            image.className = "animated slideInLeft"
            // Hide Dealer's second card during initial deal
            if (person.name === 'dealer' && person.hand.length === 2){
                image.id = "holeCard";
                image.src = `images/cards/deck_back.png`;
            }
            else {
                image.src = card.getCardImageURL();
                // Calculate points from cards in hand
                person.calculateHand();
            };
            // Display card on table
            document.getElementById(`${person.name}-hand`).appendChild(image);
        }
    };

    startNewGame();

// ###################################
// ########## BUTTON EVENTS ##########
// ###################################

    // Set bet of player

    Array.from(chip).forEach(function(element) {
      element.addEventListener("click", function() {
        chipbuttons.style.display = "none";
        controlbuttons.style.display = "flex";
        bet.style.display = "";
        cancel.style.display = "";
        deal.style.display = "none";
        hit.style.display = "none";
        stand.style.display = "none";
        // Array.from(chip).forEach(function(element){
        //     element.style.display = "none";
        // });
      })
    });


    bet.addEventListener("click", function(){
        betAmount = parseInt(document.getElementById("bet-amount").innerHTML);
        bankAmount = parseInt(document.getElementById("bank-amount").innerHTML);
        player.bet = betAmount;
        player.bank = bankAmount;
        document.getElementById("messages").innerHTML = "Your bet amount: $" + player.bet;
        chipbuttons.style.display = "none";
        bet.style.display = "none";
        cancel.style.display = "none";
        deal.style.display = "";

        // Array.from(chip).forEach(function(element) {
        //     element.style.display = "none";
        //   })

    });

    // Allows player to cancel the bet, returns money to bank and set bet to zero
    cancel.addEventListener("click", function(){
        betAmount = parseInt(document.getElementById("bet-amount").innerHTML)
        bankAmount = parseInt(document.getElementById("bank-amount").innerHTML)
        document.getElementById("bet-amount").innerHTML = 0;
        document.getElementById("bank-amount").innerHTML = bankAmount + betAmount;
        player.bank = bankAmount + betAmount;
        document.getElementById("messages").innerHTML = "Pick the bet amount";
        chipbuttons.style.display = "flex";
        controlbuttons.style.display = "none";

    });


    // Receive value of chip when clicked on, update bank amount and betting amount
    Array.from(chip).forEach(function(element){
        element.addEventListener("click", function(){
            chipValue = parseInt(element.value);
            betAmount = parseInt(document.getElementById("bet-amount").innerHTML);
            if (player.bank - chipValue >= 0){
                player.bank -= chipValue;
                document.getElementById("bank-amount").innerHTML = player.bank;
                document.getElementById("bet-amount").innerHTML = betAmount + chipValue;
            }
        });
    })

    // Deals two cards to each player and dealer when deal button is clicked
    deal.addEventListener("click", function(){
        for (var i = 0; i < 2; i++){
            // Adds  2 cards to player and dealer hand
            deck.dealCard(player);
            deck.dealCard(dealer);
        };
        // Can only deal once per game, disables deal button
        deal.style.display = "none";
        // Enable hit and stand button
        hit.style.display = "";
        stand.style.display = "";
    });

    // Deals one card to the player when hit button is clicked
    hit.addEventListener("click", function(){
        deck.dealCard(player);
        gameResults(player);
    });

    // Start dealer's turn after stand button is clicked by player
    stand.addEventListener("click", function(){
        // Disable hit and stand button
        hit.style.display = "none";
        stand.style.display = "none";
        // Flip over deal's second card, hole card
        holeCard = document.getElementById("holeCard");
        holeCard.className = "animated flipInY";
        card = dealer.hand[1];
        holeCard.src = card.getCardImageURL();
        // Recalculate dealer's points
        dealer.calculateHand();
        while (dealer.points < 17){
            deck.dealCard(dealer);
        };
        gameResults(dealer);
    });

// ###################################
// ###### GAME HELPER FUNCTIONS ######
// ###################################

    // Outcome between player and dealer
    function gameResults(currentPlayer){
        let message = "";
        let gameOver = false;
        // During player's turn
        if (currentPlayer.name === "player"){
            if (player.points > 21){
                message = "You Bust!"
                gameOver = true;

                // Disable hit and stand button
                hit.style.display = 'none';
                stand.style.display = 'none';
            }
        }

        // During Dealer's turn
        else if (currentPlayer.name === "dealer"){
            if (player.points === 21 && player.hand.length === 2 && dealer.points !== 21){
                message = "You Won! BLACKJACK!";
                player.wins += 1;
                player.bank += Math.round((player.bet * 1.5) + player.bet);
            }
            else if (dealer.points > 21) {
                message = "Dealer Bust!"
                player.wins += 1;
                player.bank += player.bet * 2;
            }
            else if (player.points === dealer.points){
                message = "Push";
                player.bank += player.bet;
            }
            else if (player.points > dealer.points){
                player.wins += 1;
                message = "You Won!";
                player.bank += player.bet * 2;
            }
            else {
                message = "You Lost!";
            }
            gameOver = true;
        }

        document.getElementById("messages").innerHTML = message;
        if (gameOver){
            if (player.bank === 0){
                document.getElementById("messages").innerHTML += " You are broke!";
                setTimeout(function(){
                    startNewGame();
                }, 3000);
            } else {
                playAgain();
            }
        }
    };

    // Restarts with a new game in current player session
    function playAgain(){
        // Reset bet amount, player hand, player points, and new dealer
        player.hand = [];
        player.bet = 0;
        player.points = 0;
        player.totalhands += 1;
        dealer = new Person("dealer");
        // Delay table being cleared
        setTimeout(function(){
            displayGameInfo();
            clearTable();
        }, 3000);
    };

    // Displays game info and displays betting buttons
    function displayGameInfo(){
        // Game Stats
        document.getElementById("dealer-points").innerHTML = dealer.points;
        document.getElementById("player-points").innerHTML = player.points;
        document.getElementById("bet-amount").innerHTML = player.bet;
        document.getElementById("bank-amount").innerHTML = player.bank;
        document.getElementById("wins").innerHTML = player.wins;
        document.getElementById("totalhands").innerHTML = player.totalhands;
        // Control Buttons
        // document.getElementById("bet-button").style.display = "none";
        // document.getElementById("cancel-button").style.display = "none";
        // document.getElementById("deal-button").style.display = "none";
        // document.getElementById("hit-button").style.display = "none";
        // document.getElementById("stand-button").style.display = "none";
        document.getElementById("messages").innerHTML = "Pick the bet amount";
        document.getElementById("playerSection").style.display = "flex";


        // Array.from(chip).forEach(function(element){
        //     element.style.display = "";
        // });
        chipbuttons.style.display = "flex";
        // document.getElementById("controlbuttons").style.display = "none";
    };

    // Clears table of cards from dealer and player
    function clearTable(){
        playerNode = document.getElementById("player-hand");
        dealerNode = document.getElementById("dealer-hand");
        if (playerNode.hasChildNodes()){
            while (playerNode.firstChild){
                playerNode.removeChild(playerNode.firstChild);
            };
            while (dealerNode.firstChild){
                dealerNode.removeChild(dealerNode.firstChild);
            };
        };
        document.getElementById("messages").innerHTML = "Pick the bet amount";
    };

    // Start a complete new game session
    function startNewGame(){
        player = new Person("player");
        dealer = new Person("dealer");
        deck = new Deck();
        deck.createNewDeck();
        deck.shuffle();
        clearTable();
        displayGameInfo();
    };

}) // End of DOM
