import React, { useState } from "react";

// Basic component demonstrating basic React state management
function Basic() {
  // State for counting
  const [count, setCount] = useState(0); // 'count' holds the current count value, and 'setCount' is used to update it

  // State to manage visibility of a message
  const [show, setShow] = useState(false); // 'show' determines if the message is visible, 'setShow' updates its value

  // State to store text input
  const [text, setText] = useState(""); // 'text' stores the value of the input field, 'setText' updates it

  return (
    <>
      {/* Counter Section */}
      <div className="counter">
        <h2>Count: {count}</h2> {/* Display the current count */}
        <button onClick={() => setCount(count + 1)}>+</button>{" "}
        {/* Increase the count */}
        <button onClick={() => setCount(count - 1)}>-</button>{" "}
        {/* Decrease the count */}
        <button onClick={() => setCount(0)}>reset</button>{" "}
        {/* Reset the count to 0 */}
      </div>

      {/* Input Mirror Section */}
      <div className="input-mirror">
        <input
          value={text} // Bind the input field to 'text' state
          onChange={(e) => setText(e.target.value)} // Update 'text' when input changes
        />
        <p>{text}</p> {/* Display the value of 'text' */}
      </div>

      {/* Toggle Message Section */}
      <div className="toggle-message">
        <h2>Toggle Message</h2>
        <button onClick={() => setShow(!show)}>
          {show ? "Hide Message" : "Show Message"}
        </button>
        {show && <p>Welcome to UST Dashboard!</p>}{" "}
        {/* Conditionally render the message */}
      </div>
    </>
  );
}

export default Basic; // Export the Basic component for use in other parts of the app
