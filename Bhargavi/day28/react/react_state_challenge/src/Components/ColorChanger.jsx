import React, { useState } from "react";

function ColorChanger() {
  const [colorIndex, setColorIndex] = useState(0);
  const colors = ["#f8b400", "#5f6368", "#34a853", "#e53935"];

  return (
    <div className="box" style={{ backgroundColor: colors[colorIndex] }}>
      <button onClick={() => setColorIndex((colorIndex + 1) % colors.length)}>
        Change Color
      </button>
    </div>
  );
}

export default ColorChanger;
