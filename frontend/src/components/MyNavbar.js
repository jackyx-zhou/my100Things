import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';

const MyNavbar = () => {
  return (
    <Navbar bg="dark" variant="dark">
      <Navbar.Brand href="#home">
        My 100 Things
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Nav className="mr-auto">
        <NavDropdown title="Categories" id="collasible-nav-dropdown">
          <NavDropdown.Item href="#action/1.1">Clothes</NavDropdown.Item>
          <NavDropdown.Item href="#action/1.2">Books</NavDropdown.Item>
          <NavDropdown.Item href="#action/1.3">Papers</NavDropdown.Item>
          <NavDropdown.Item href="#action/1.4">Komono</NavDropdown.Item>
          <NavDropdown.Divider />
          <NavDropdown.Item href="#action/1.5">Sentimental Items</NavDropdown.Item>
        </NavDropdown>
        <Nav.Link href="#archive">Archived</Nav.Link>
        </Nav>
    </Navbar>
  );
}

export default MyNavbar;
