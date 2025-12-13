import React, { useState } from 'react';

const ColorChanger = () => {
  const [colorIndex, setColorIndex] = useState(0); 

  const colors = ['red', 'blue', 'green', 'yellow']; 

  const changeColor = () => {
    setColorIndex((prevIndex) => (prevIndex + 1) % colors.length); 
  };

  return (
    <div>
      <div style={{ width: 100, height: 100, backgroundColor: colors[colorIndex] }} />
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default ColorChanger;
