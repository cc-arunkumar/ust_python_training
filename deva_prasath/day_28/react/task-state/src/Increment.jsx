import { useState } from "react";
 
function Increment() {
  const [count, setCount] = useState(0); // State
  return (
    <div className="buttons">
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>    </div>
  );
}

export default Increment