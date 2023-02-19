import React from 'react';
import { render } from 'react-dom';
import { createStore, applyMiddleware, compose } from 'redux';
import { Provider } from 'react-redux';
import reduxThunk from 'redux-thunk';

import App from './components/App/index.jsx';

import reducers from './store/reducers';

import './index.css';

const composeEnhansers = (window).__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(reducers, composeEnhansers(applyMiddleware(reduxThunk)));

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.querySelector('#root'),
);

