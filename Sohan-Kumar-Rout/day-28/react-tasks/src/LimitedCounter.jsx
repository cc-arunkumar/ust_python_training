import { useState } from "react";

export default function LimitedCounter() {
  const [count, setCount] = useState(0);

  const increment = () => {
    if (count === 10) return alert("Max limit reached!");
    setCount(count + 1);
  };

  const decrement = () => {
    if (count === 0) return alert("Min limit reached!");
    setCount(count - 1);
  };

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={decrement}>-</button>
      <button onClick={increment}>+</button>
    </div>
  );
}
