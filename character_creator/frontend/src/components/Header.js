import React from 'react';
import { Nav, NavItem, Navbar } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const Header = () => {
  return (
    <header className="header-wrapper">
      <Navbar staticTop fluid collapseOnSelect>
        <Navbar.Header>
          <Navbar.Brand>Super Smash Bros. Character Creator</Navbar.Brand>
        </Navbar.Header>
        <Navbar.Toggle />
        <Navbar.Collapse>
          <Nav pullRight>
            <LinkContainer to="/">
              <NavItem>Home</NavItem>
            </LinkContainer>
            <LinkContainer to="/create">
              <NavItem>Create!</NavItem>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    </header>
  )
}

export default Header;
