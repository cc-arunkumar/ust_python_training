import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  
   const sub = () => {
    setCount(prev => (prev - 1 < 0 ? 0 : prev - 1));
  };
  return (
    <div>
      <h2>Counter: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Add</button>
      <button onClick={sub}>Remove</button>
    </div>
  );
}
