// Import dependencies, bootstrap elements
import React from 'react';
import { Jumbotron } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

import './styles/Home.css';

// Functional component, no need to use a React component for now.
const Home = () => {
  return (
    <div className="Home">
      <Jumbotron className="home-title">
        <h1>WELCOME</h1>
        <h3>Conceptualize the characters you want to see in Smash!</h3>
        <LinkContainer to="/create">
          <button className="home-button">Create a Character</button>
        </LinkContainer>
      </Jumbotron>
    </div>
  )
}

export default Home;
