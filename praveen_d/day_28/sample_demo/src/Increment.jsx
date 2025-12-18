import React from "react";
import { useState } from "react";

const Increment = () => {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increase</button>
      <button onClick={() => setCount((count) => count - 1)}>Decrease</button>
      <button onClick={() => setCount(0)}>reset</button>
    </div>
  );
};

export default Increment;
