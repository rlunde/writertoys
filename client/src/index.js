import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import './style/index.css';

import App from './components/App';
// BrowserRouter creates a browser history
//import { BrowserRouter, Link, Route } from 'react-router-dom';
import { BrowserRouter, Route } from 'react-router-dom';

import reducers from './reducers';

// note: this is from Stephen Grider's Redux Simple Starter. I deleted
// the following from the default create-react-app index.js:
// import App from './components/App';
// import registerServiceWorker from './registerServiceWorker';
// ReactDOM.render(<App />, document.getElementById('root'));
// registerServiceWorker();

const createStoreWithMiddleware = applyMiddleware()(createStore);

ReactDOM.render(
  <Provider store={createStoreWithMiddleware(reducers)}>
    <BrowserRouter>
    <div>
      <Route path="/" component={App} />
    </div>
    </BrowserRouter> 
  </Provider>
  // Router replaces App
  // This is from Redux Simple Starter, but I don't need an index.html, I think,
  // so I'm sticking with the create-react-app approach
  // , document.querySelector('.container'));
  , document.getElementById('root'));

