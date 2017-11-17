import React, { Component } from 'react';
import './agecheck.css';

class AgeCheck extends Component {
  constructor(props) {
    super(props);
    this.state = {
      friends: [
        {id: 1, name: 'Monis', age: 33},
        {id: 2, name: 'Rafi', age: 30},
        {id: 2, name: "Youngun'", age: 19}
      ]
    };
  }

  can_party (age) {
    if (age > 21) {
      return (
        <span>Going</span>
    )}
    return (
      <span>Cannot go</span>
  )}

  render() {
    return (
      <ul>
        {this.state.friends.map((friend) =>
        <li key={friend.id}>
          {friend.name}, {friend.age} - {this.can_party(friend.age)}
        </li>)}
      </ul>
    );
  };
};
export default AgeCheck;
