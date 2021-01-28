import logo from './logo.svg';
import './App.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;


import React from 'react';
import './App.css';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from "@stripe/stripe-js/pure";
import CheckoutForm from "./components/CheckoutForm";

const stripePromise = loadStripe('pk_test_');

const App = () => (
  <Elements stripe={stripePromise}>
    <CheckoutForm />
  </Elements>
);

export default App;