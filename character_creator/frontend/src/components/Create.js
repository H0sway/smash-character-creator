// Import dependencies
import React, { Component } from 'react';
import axios from 'axios';

// Import components used to track the changes for each character.
import AddCharacter from './AddCharacter';
import AddMove from './AddMove';

class Create extends Component {
  constructor() {
    super();
    this.state = {
      fireRedirect: false,
      characterName: '',
      characterSeries: '',
      characterDescription: '',
      characterImage: '',
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(e) {
    const name = e.target.name;
    const value = e.target.value;
    this.setState({
      [name]: [value]
    })
  }
  handleSubmit(e) {
    e.preventDefault();
    axios.post('/api/characters', {
      name: this.state.characterName,
      series: this.state.characterSeries,
      description: this.state.characterDescription,
      char_image: this.state.characterImage
    })
    .then(response => {
      this.setState({
        fireRedirect: true
      });
    })
    .catch(error => {
      alert("There was a problem submitting your character.")
      console.log("Submit character error." + error);
    })
  }
  render() {
    return (
      <div className="Create">
        <form onSubmit={this.handleSubmit}>
          <AddCharacter
            nameValue={this.state.characterName}
            seriesValue={this.state.characterSeries}
            descriptionValue={this.state.characterDescription}
            characterImage={this.state.characterImage}
            handleChange={this.state.handleChange}
          />
        </form>
      </div>
    )
  }
}

export default Create;
