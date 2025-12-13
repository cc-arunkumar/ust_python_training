import React, { useState } from "react";

// Intermediate component demonstrating state manipulation, color changes, and visibility toggles
function Intermediate() {
  // Array of colors to cycle through
  const colors = ["red", "blue", "green", "purple"];

  // State variables
  const [index, setIndex] = useState(0); // 'index' tracks the current color in the 'colors' array
  const [count, setCount] = useState(0); // 'count' tracks the current count value
  const [visible, setVisible] = useState(false); // 'visible' toggles the visibility of details section

  // Function to increment the count (up to 10)
  const increment = () => {
    if (count < 10) {
      setCount(count + 1); // Increment count by 1 if it's less than 10
    } else {
      alert("Max limit reached!"); // Alert when the max limit is reached
    }
  };

  // Function to decrement the count (down to 0)
  const decrement = () => {
    if (count > 0) {
      setCount(count - 1); // Decrement count by 1 if it's greater than 0
    } else {
      alert("Min limit reached!"); // Alert when the min limit is reached
    }
  };

  return (
    <>
      {/* Color Change Section */}
      <div className="input-mirror">
        {/* Display a square div with dynamic background color */}
        <div
          style={{ width: 100, height: 100, backgroundColor: colors[index] }}
        />
        {/* Button to cycle through colors */}
        <button onClick={() => setIndex((index + 1) % colors.length)}>
          Change Color
        </button>
      </div>

      {/* Counter Section */}
      <div className="counter">
        <h2>Count: {count}</h2> {/* Display the current count */}
        <button onClick={increment}>+</button> {/* Increment the count */}
        <button onClick={decrement}>-</button> {/* Decrement the count */}
      </div>

      {/* Visibility Toggle Section */}
      <div className="visibility-toggle">
        {/* Toggle button to show/hide details */}
        <button onClick={() => setVisible(!visible)}>
          {visible ? "Hide Details" : "Show Details"}
        </button>
        {/* Conditional rendering of the details section */}
        {visible && (
          <div className="details">
            <p>
              Here are some hidden details revealed when you click the button!
            </p>
          </div>
        )}
      </div>
    </>
  );
}

export default Intermediate; // Export the Intermediate component for use in other parts of the app
