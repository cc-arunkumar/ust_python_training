import React, { useState } from 'react';  // Import useState hook
import Level2 from './level2';  // Import Level2 component


function Level1() {
  const [count, setCount] = useState(10);  // Initialize state with a value of 10

  return (
    <div>
      <h2>Counter: {count}</h2>
      <Level2 count={count} setCount={setCount} />  {/* Pass count and setCount as props */}
    </div>
  );
}

export default Level1;
