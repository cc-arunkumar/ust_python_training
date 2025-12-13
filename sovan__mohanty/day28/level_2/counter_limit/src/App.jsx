import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  const increment = () => {
    if (count < 10) {
      setCount(count + 1);
    } else {
      alert("Maximum limit reached (10)!");
    }
  };

  const decrement = () => {
    if (count > 0) {
      setCount(count - 1);
    } else {
      alert("Minimum limit reached (0)!");
    }
  };

  return (
    <div className="App">
      <h1>Counter with Limits</h1>
      <p className="count">Count: {count}</p>
      <div className="buttons">
        <button onClick={increment}>+</button>
        <button onClick={decrement}>-</button>
      </div>
    </div>
  );
}

export default App;
