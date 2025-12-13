import { useState } from "react";
import "./App.css";

function App() {
  // state for the counter
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1>Counter</h1>
      <p className="count">Count: {count}</p>
      <div className="buttons">
        <button onClick={() => setCount(count + 1)}>+</button>
        <button onClick={() => setCount(count - 1)}>-</button>
      </div>
    </div>
  );
}

export default App;
