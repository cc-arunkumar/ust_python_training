import { useState } from "react";
import "./Increment.css";

export default function Increment() {
  const [count, setCount] = useState(0);

  return (
    <div className="hello">
      <h3 className="count-text">Count : {count}</h3>

      <div className="btn-group">
        <button className="btn" onClick={() => setCount(count + 1)}>
          Increment
        </button>

        <button className="btn" onClick={() => setCount(count - 1)}>
          Decrement
        </button>
      </div>
    </div>
  );
}
