import { useState } from "react";
 
function Increment() {
  const [count, setCount] = useState(0); // State
  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
}