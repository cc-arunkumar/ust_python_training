import { useState } from "react";

export default function LimitedCounter() {
  const [count, setCount] = useState(0);

  const inc = () => {
    if (count < 10) setCount(c => c + 1);
    else alert("Max limit reached!");
  };

  const dec = () => {
    if (count > 0) setCount(c => c - 1);
    else alert("Min limit reached!");
  };

  return (
    <section className="card">
      <h3>Counter with Limits</h3>
      <p>Count: {count}</p>
      <div className="row">
        <button onClick={inc}>+</button>
        <button onClick={dec}>-</button>
      </div>
    </section>
  );
}
