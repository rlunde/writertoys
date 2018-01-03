import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/css/bootstrap-theme.css'

import { Nav, NavItem, MenuItem, Navbar, NavDropdown } from 'react-bootstrap'

const navbarInstance = (
  <Navbar inverse>
    <Navbar.Header>
      <Navbar.Brand>
        <a href="/">WriterToys</a>
      </Navbar.Brand>
    </Navbar.Header>
    <Nav>
      <NavItem eventKey={1} href="/">Link</NavItem>
      <NavItem eventKey={2} href="/">Link</NavItem>
      <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
        <MenuItem eventKey={3.1}>Action</MenuItem>
        <MenuItem eventKey={3.2}>Another action</MenuItem>
        <MenuItem eventKey={3.3}>Something else here</MenuItem>
        <MenuItem divider />
        <MenuItem eventKey={3.4}>Separated link</MenuItem>
      </NavDropdown>
    </Nav>
  </Navbar>
);

class App extends Component {
  render() {
    return (
      <div>
        {navbarInstance}
        <div className="main">
          <div className="main-content">Main panel goes here</div>
        </div>
        <footer className="footer">
          <div className="container">
            <p className="text-muted">
              WriterToys: A Fiction Writer's Toolkit, version 0.0.1
            </p>
          </div>
        </footer>
        <script src="../node_modules/jquery/dist/jquery.min.js"></script>
        <script src="../node_modules/tether/dist/js/tether.js"></script>
        <script src="../node_modules/bootstrap/dist/js/bootstrap.min.js"></script>

      </div>
    );
  }
}
export default App;
