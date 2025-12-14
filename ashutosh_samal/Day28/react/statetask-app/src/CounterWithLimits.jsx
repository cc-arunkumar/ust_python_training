import React, { useState } from "react";

const CounterWithLimits = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    if (count < 10) setCount(count + 1);
    else alert("Limit reached!");
  };

  const decrement = () => {
    if (count > 0) setCount(count - 1);
  };

  return (
    <div>
      <button onClick={decrement}>-</button>
      <span>{count}</span>
      <button onClick={increment}>+</button>
    </div>
  );
};

export default CounterWithLimits;
