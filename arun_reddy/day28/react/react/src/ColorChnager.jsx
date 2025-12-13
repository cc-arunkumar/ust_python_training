import React from "react";
import { useState } from "react";
import "./index.css";
export default function ColorChnager() {
  const colors = ["#3b82f6", "#ef4444", "#10b981", "#f59e0b"];
  const [colorIndex, setColorIndex] = useState(0);

  const changeColor = () => {
    setColorIndex((colorIndex + 1) % colors.length);
  };

  return (
    <div className="color-changer-container">
      <div
        className="color-box"
        style={{ backgroundColor: colors[colorIndex] }}
      >
        <button onClick={changeColor} className="color-btn">
          Change Color
        </button>
      </div>
    </div>
  );
}
