import React, { useState } from "react";
import "./index.css";
export default function Counter() {
  const [Count, setCount] = useState(0);
  return (
    <div className="counter-container">
      <button
        onClick={() => setCount(Count + 1)}
        className="counter-btn increment"
      >
        +
      </button>
      <span className="counter-display">{Count}</span>
      <button
        onClick={() => setCount(Count - 1)}
        className="counter-btn decrement"
      >
        -
      </button>
      <button onClick={() => setCount(0)} className="counter-btn reset">
        RESET
      </button>
    </div>
  );
}
