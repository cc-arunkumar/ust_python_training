import { useState } from 'react';

export default function Level1() {
  const [count, setCount] = useState(0);
  const [showMessage, setShowMessage] = useState(false);
  const [inputText, setInputText] = useState('');

  return (
    <section className="level-section">
      <h2>Level 1: Basic State</h2>

      <div className="challenge">
        <h3>Counter</h3>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>+</button>
        <button onClick={() => setCount(count - 1)}>-</button>
      </div>

      <div className="challenge">
        <h3>Toggle Message</h3>
        <button onClick={() => setShowMessage(!showMessage)}>
          {showMessage ? 'Hide' : 'Show'} Message
        </button>
        {showMessage && <p className="welcome-message">Welcome to UST Dashboard!</p>}
      </div>

      <div className="challenge">
        <h3>Input Mirror</h3>
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Type something..."
        />
        <p>You typed: {inputText || '(nothing yet)'}</p>
      </div>
    </section>
  );
}