import { useState } from 'react';

export default function Level2() {
  const colors = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow'];
  const [colorIndex, setColorIndex] = useState(0);
  const [limitedCount, setLimitedCount] = useState(0);
  const [showDetails, setShowDetails] = useState(false);

  return (
    <section className="level-section">
      <h2>Level 2: Interactive State</h2>

      <div className="challenge">
        <h3>Color Changer</h3>
        <div className="color-box" style={{ backgroundColor: colors[colorIndex] }}>
          {colors[colorIndex]}
        </div>
        <button onClick={() => setColorIndex((colorIndex + 1) % colors.length)}>
          Change Color
        </button>
      </div>

      <div className="challenge">
        <h3>Counter with Limits (0-10)</h3>
        <p>Count: {limitedCount}</p>
        <button onClick={() => setLimitedCount(Math.max(0, limitedCount - 1))}>-</button>
        <button onClick={() => setLimitedCount(Math.min(10, limitedCount + 1))}>+</button>
        {(limitedCount === 0 || limitedCount === 10) && (
          <p className="limit-alert">Limit reached!</p>
        )}
      </div>

      <div className="challenge">
        <h3>Visibility Toggle</h3>
        <button onClick={() => setShowDetails(!showDetails)}>
          {showDetails ? 'Hide' : 'Show'} Details
        </button>
        {showDetails && (
          <div className="details-box">
            <p>Here are some hidden details about React state!</p>
            <ul>
              <li>useState is a Hook</li>
              <li>Never mutate state directly</li>
              <li>Always use the setter function</li>
            </ul>
          </div>
        )}
      </div>
    </section>
  );
}