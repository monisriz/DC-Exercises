import React, { Component } from 'react';
import './App.css';

class MyForm extends Component {
  constructor() {
    super();
    this.state = {name: ''};
    this.state = {name: '', color: 'blue'};
  }

  update_name (event) {
    this.setState({name: event.target.value});
  }

  update_color (event) {
    this.setState({color: event.target.value});
  }

  handleSubmit(event) {
    console.log('submitted: ' + this.state.name);
    event.preventDefault();
  }
  render() {
    return (
      <form onSubmit={event => this.handleSubmit(event)}>
        <label>Your Name?</label>
        <input type="text" value={this.state.name}
        onChange={event => this.update_name(event)}/>
        <br/>

        <select value={this.state.color}
          onChange={event => this.update_color(event)}>
          <option value="red">Red</option>
          <option value="blue">Blue</option>
        </select>
        <br/>
        <button type="submit">Submit</button>
      </form>
    );
  }
}

export default MyForm;
