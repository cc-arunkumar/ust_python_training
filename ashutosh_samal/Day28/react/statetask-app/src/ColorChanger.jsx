import React, { useState } from "react";

const ColorChanger = () => {
  const [colorIndex, setColorIndex] = useState(0);
  const colors = ["red", "green", "blue", "yellow"];

  const changeColor = () => {
    setColorIndex((prevIndex) => (prevIndex + 1) % colors.length);
  };

  return (
    <div>
      <button onClick={changeColor}>Change Color</button>
      <div
        style={{
          width: "100px",
          height: "100px",
          backgroundColor: colors[colorIndex],
        }}
      ></div>
    </div>
  );
};

export default ColorChanger;
