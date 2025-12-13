import { useState } from "react";

function Increment() {
  const [count, setCount] = useState(0); // State
  return (
    <div>
      <div className="app-container"></div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)} style={{ marginRight: "10px" }}>Increase</button>
      <button onClick={() => setCount(count - 1)}>Decrease</button>
    </div>
  );
}
export default Increment;