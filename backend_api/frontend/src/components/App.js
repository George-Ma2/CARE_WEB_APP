import React, { Component } from "react";
import { createRoot } from "react-dom/client";
import HomePage from "./HomePage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
    <HomePage/>
   </div>
    );
  }
}


// Create an app container
const appDiv = document.getElementById("app");

// Use createRoot instead of render to render the app
const root = createRoot(appDiv);
root.render(<App/>);
