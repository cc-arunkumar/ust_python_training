import { useState } from "react";

export default function CounterWithLimits() {
  const [count, setCount] = useState(0);

  const increment = () => {
    if (count < 10) setCount(count + 1);
    else alert("Max limit reached!");
  };

  const decrement = () => {
    if (count > 0) setCount(count - 1);
    else alert("Min limit reached!");
  };

  return (
    <div >
      <h3>Counter with Limits</h3>
      <p>{count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
