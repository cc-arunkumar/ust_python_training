import { useState } from "react";
function ColorChanger() {
  const colors = ["red", "blue", "green", "orange"];
  const [index, setIndex] = useState(0);

  return (
    <div>
      <div style={{ width: 100, height: 100, backgroundColor: colors[index] }}></div>
      <button onClick={() => setIndex((index + 1) % colors.length)}>Change Color</button>
    </div>
  );
}

export default ColorChanger