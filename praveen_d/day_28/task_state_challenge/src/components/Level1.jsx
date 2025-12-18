import React from "react";
import { useState } from "react";

const Level1 = () => {
  const [count, setCount] = useState(0);
  const [toggle, settoggle] = useState(false);
  const [inputvalue, setinput] = useState('');

  const handleInput = (event) => {
    setinput(event.target.value);
  }
  return (
    <>
      <div className="counter">
        <h2>Counter</h2>
        <div className="button_card">
          <button onClick={() => setCount((count) => count + 1)}>
            increase
          </button>
          <button onClick={() => setCount((count) => count - 1)}>
            Decrease
          </button>
        </div>
        count is {count}
      </div>
      <div className="toggle">
        <h2>Toggle Message</h2>
        <div>
          <button onClick={() => settoggle(!toggle)}>Toggle</button>
        </div>
        {toggle && <p>Welcome to UST Dashboard!</p>}
      </div>
      <div className="input_mirror">
        <h2>Input Mirror</h2>
        <div>
          <input
            type="text"
            value={inputvalue}
            onChange={handleInput}
            placeholder="Enter something...."
          />
        </div>
        {inputvalue}
      </div>
    </>
  );
};

export default Level1;
