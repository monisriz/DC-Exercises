import React, { Component } from 'react';

class HelloList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      friends: [
        {id: 1, name: 'Monis', age: 33},
        {id: 2, name: 'Rafi', age: 30}
      ]
    };
  }
  render() {
    return (
      <ul>
        {this.state.friends.map((friend) =>
        <li key={friend.id}>
          {friend.name}, {friend.age}
        </li>)}
      </ul>
    );
  };
};
export default HelloList;
