import React, { useState } from "react";

const Increment = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Count : {count}</h2>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
  );
};

export default Increment;
