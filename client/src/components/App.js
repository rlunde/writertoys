import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css'
import '../style/writertoys.css'

class App extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-toggleable-md navbar-inverse fixed-top bg-inverse">
          <button
            className="navbar-toggler navbar-toggler-right"
            type="button"
            data-toggle="collapse"
            data-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <a className="navbar-brand" href="/">WriterToys</a>
          <div className="collapse navbar-collapse" id="navbarCollapse">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item active">
                <a className="nav-link" href="/">Home
                  <span className="sr-only">(current)</span>
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/about">About</a>
              </li>
              <li className="nav-item">
                <a className="nav-link disabled" href="/logout">Logout</a>
              </li>
            </ul>
          </div>
        </nav>
        <div className="main">
          Main panel goes here
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
