import { useState } from "react";
 
export default function Increment() {
  const [count, setCount] = useState(10); // State
  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increase</button>
      <hr />
      <button onClick={() => setCount(count - 1)}>Decrease</button>
    </div>
  );
}

 
