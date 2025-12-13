import React, { useState } from "react";

function BasicStateDemo() {
  const [count, setCount] = useState(0);
  const [showMessage, setShowMessage] = useState(false);
  const [text, setText] = useState("");

  return (
    <div className="container">
      {/* Counter */}
      <div className="card">
        <h2 className="counter-title">Counter</h2>
        <div className="counter-box">
          <button className="btn" onClick={() => setCount(count - 1)}>-</button>
          <span className="count">{count}</span>
          <button className="btn" onClick={() => setCount(count + 1)}>+</button>
        </div>
      </div>

      {/* Toggle Message */}
      <div className="card">
        <h2 className="counter-title">Toggle Message</h2>
        <button className="btn toggle-btn" onClick={() => setShowMessage(!showMessage)}>
          Toggle Message
        </button>
        {showMessage && <p className="message">Welcome to UST Dashboard!</p>}
      </div>

      {/* Input Mirror */}
      <div className="card">
        <h2 className="counter-title">Input Mirror</h2>
        <input
          className="input-box"
          type="text"
          placeholder="Type something..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <p className="mirror-text">You typed: {text}</p>
      </div>
    </div>
  );
}

export default BasicStateDemo;
