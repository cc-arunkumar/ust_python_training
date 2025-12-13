import { useState } from "react";
 
function Decrement() {
  const [count, setCount] = useState(0); // State
  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count - 1)}>Decrease</button>
    </div>
  );
}

export default Decrement