// Import dependencies. React for compiling, BrowserRouter for routes, and bootstrap's grid for responsive rendering
import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Grid } from 'react-bootstrap';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Grid>
          </Grid>
        </div>
      </Router>
    );
  }
}

export default App;
