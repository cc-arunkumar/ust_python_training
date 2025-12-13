import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");

  return (
    <div className="root">
    <div className="App">
      <h1>Input Mirror</h1>
      
      {/* Input field */}
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type something..."
        className="input-box"
      />

      {/* Mirrored text */}
      <p className="mirror-text">{text}</p>
    </div>
    </div>
  );
}

export default App;
