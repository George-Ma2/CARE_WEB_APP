import React, { Component } from "react";
import { createRoot } from "react-dom/client";
//import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (<h1> Testing React Code </h1>);
  }
}


// Create an app container
const appDiv = document.getElementById("app");

// Use createRoot instead of render to render the app
const root = createRoot(appDiv);
root.render(<App/>);
