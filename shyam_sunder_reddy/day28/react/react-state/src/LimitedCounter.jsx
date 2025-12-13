import { useState } from "react";
function LimitedCounter() {
  const [count, setCount] = useState(0);

  const increase = () => {
    if (count < 10) setCount(count + 1);
    else alert("Max limit reached!");
  };

  const decrease = () => {
    if (count > 0) setCount(count - 1);
    else alert("Min limit reached!");
  };

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={increase}>+</button>
      <button onClick={decrease}>-</button>
    </div>
  );
}

export default LimitedCounter