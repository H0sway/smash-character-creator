// Import dependencies. React for compiling, BrowserRouter for routes, and bootstrap's grid for responsive rendering
import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Grid } from 'react-bootstrap';

// Import stylesheet
import './App.css';

// Import components
import Header from './components/Header';
import Home from './components/Home';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Grid>
            <Header />
            <Route exact path="/" component={Home} />
          </Grid>
        </div>
      </Router>
    );
  }
}

export default App;
