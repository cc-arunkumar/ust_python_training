import React, { useState } from 'react';

const CounterWithLimits = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    if (count < 10) {
      setCount(count + 1);
    } else {
      alert('Maximum limit reached!');
    }
  };

  const decrement = () => {
    if (count > 0) {
      setCount(count - 1);
    } else {
      alert('Minimum limit reached!');
    }
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
};

export default CounterWithLimits;
