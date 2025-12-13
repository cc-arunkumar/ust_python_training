import { useState } from "react";
import "./index.css";

export default function CounterWithLimits() {
  const [count, setCount] = useState(0);
  const MIN = 0;
  const MAX = 10;

  const increment = () => {
    if (count >= MAX) {
      alert("Maximum limit reached! (10)");
    } else {
      setCount(count + 1);
    }
  };

  const decrement = () => {
    if (count <= MIN) {
      alert("Minimum limit reached! (0)");
    } else {
      setCount(count - 1);
    }
  };

  return (
    <div className="counter-limits-container">
      <div className="counter-limits-card">
        <h2 className="counter-limits-title">Counter (0-10)</h2>
        <div className="counter-limits-display">{count}</div>
        <div className="counter-limits-buttons">
          <button onClick={decrement} className="counter-limits-btn">
            -
          </button>
          <button onClick={increment} className="counter-limits-btn">
            +
          </button>
        </div>
      </div>
    </div>
  );
}
