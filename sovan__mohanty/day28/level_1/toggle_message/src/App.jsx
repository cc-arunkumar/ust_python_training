import { useState } from "react";
import "./App.css";

function App() {
  // state to track visibility
  const [showMessage, setShowMessage] = useState(false);

  // toggle function
  const toggleMessage = () => {
    setShowMessage(!showMessage);
  };

  return (
    <div className="App">
      <h1>Click The Button</h1>
      <button onClick={toggleMessage}>
        {showMessage ? "Hide Message" : "Show Message"}
      </button>

      {showMessage && (
        <p className="message">Welcome to UST Dashboard!</p>
      )}
    </div>
  );
}

export default App;
