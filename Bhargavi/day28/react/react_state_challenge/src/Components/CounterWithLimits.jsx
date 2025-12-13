import React, { useState } from "react";

function CounterWithLimits() {
  const [count, setCount] = useState(0);
  const min = 0;
  const max = 10;

  const handleIncrement = () => {
    if (count < max) {
      setCount(count + 1);
    } else {
      alert("Max limit reached!");
    }
  };

  const handleDecrement = () => {
    if (count > min) {
      setCount(count - 1);
    } else {
      alert("Min limit reached!");
    }
  };

  return (
    <div className="box">
      <h2>Counter: {count}</h2>
      <button onClick={handleIncrement}>+</button>
      <button onClick={handleDecrement}>-</button>
    </div>
  );
}

export default CounterWithLimits;
