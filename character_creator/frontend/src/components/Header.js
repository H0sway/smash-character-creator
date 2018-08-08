import React from 'react';
import { Nav, NavItem, Navbar } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const Header = () => {
  return (
    <header className="header-wrapper">
      <Navbar staticTop>
        <Nav bsStyle="pills" justified>
          <Navbar.Brand>Super Smash Bros. Character Creator</Navbar.Brand>
          <LinkContainer to="/">
            <NavItem>Home</NavItem>
          </LinkContainer>
          <LinkContainer>
            <NavItem>Create!</NavItem>
          </LinkContainer>
        </Nav>
      </Navbar>
    </header>
  )
}

export default Header;
