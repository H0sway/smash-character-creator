// Import dependencies, bootstrap elements
import React from 'react';
import { LinkContainer } from 'react-router-bootstrap';

// Functional component, no need to use a React component for now.
const Home = () => {
  return (
    <div className="Home">
      <div className="home-title">
        <h1>WELCOME</h1>
        <h3>Conceptualize the characters you want to see in Smash!</h3>
      </div>
      <LinkContainer to="/create">
        <button className="home-button">Create a Character</button>
      </LinkContainer>
    </div>
  )
}

export default Home;
