import { useState } from "react";
import "./Counter.css"; // Import CSS file

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="counter-container">
      <h2>Count : </h2>
      <p className="count-display">{count}</p>
      <div className="button-group">
        <button onClick={() => setCount(count + 1)}>Increase</button>
        <button onClick={() => setCount(count - 1)}>Decrease</button>
      </div>
    </div>
  );
}
