import { useState } from "react";

export default function ColorChanger() {
  const colors = ["lightblue", "lightgreen", "lightpink", "lightyellow"];
  const [index, setIndex] = useState(0);

  return (
    <div>
      <h3>Color Changer</h3>
      <div
        className="color-box"
        style={{ backgroundColor: colors[index], height: "50px" }}
      ></div>
      <button onClick={() => setIndex((index + 1) % colors.length)}>
        Change Color
      </button>
    </div>
  );
}
