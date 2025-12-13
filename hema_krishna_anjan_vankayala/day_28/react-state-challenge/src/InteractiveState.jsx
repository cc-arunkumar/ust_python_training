import React, { useState } from "react";
import "./InteractiveState.css";

function InteractiveState() {
  // 1. Color Changer
  const colors = ["lightcoral", "lightgreen", "lightblue", "khaki"];
  const [colorIndex, setColorIndex] = useState(0);

  const changeColor = () => {
    setColorIndex((prev) => (prev + 1) % colors.length);
  };

  // 2. Counter with Limits
  const [count, setCount] = useState(0);

  const increase = () => {
    if (count === 10) {
      alert("Maximum limit reached!");
      return;
    }
    setCount(count + 1);
  };

  const decrease = () => {
    if (count === 0) {
      alert("Minimum limit reached!");
      return;
    }
    setCount(count - 1);
  };

  // 3. Visibility Toggle
  const [showDetails, setShowDetails] = useState(false);

  return (
    <div className="container">

      {/* Color Changer */}
      <div className="card">
        <h2 className="title">Color Changer</h2>
        <div
          className="color-box"
          style={{ backgroundColor: colors[colorIndex] }}
        ></div>
        <button className="btn" onClick={changeColor}>Change Color</button>
      </div>

      {/* Counter with Limits */}
      <div className="card">
        <h2 className="title">Counter with Limits (0–10)</h2>
        <div className="counter-box">
          <button className="btn" onClick={decrease}>-</button>
          <span className="count">{count}</span>
          <button className="btn" onClick={increase}>+</button>
        </div>
      </div>

      {/* Visibility Toggle */}
      <div className="card">
        <h2 className="title">Visibility Toggle</h2>
        <button className="btn toggle-btn" onClick={() => setShowDetails(!showDetails)}>
          {showDetails ? "Hide Details" : "Show Details"}
        </button>

        {showDetails && (
          <p className="details">
            These are some hidden details that appear when you click the button.
          </p>
        )}
      </div>

    </div>
  );
}

export default InteractiveState;
