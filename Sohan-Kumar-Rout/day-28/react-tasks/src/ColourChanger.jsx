import { useState } from "react";

export default function ColorChanger() {
  const colors = ["red", "green", "blue", "orange"];
  const [index, setIndex] = useState(0);

  const changeColor = () => {
    setIndex((index + 1) % colors.length);
  };

  return (
    <div>
      <div 
        style={{
          width: "150px",
          height: "150px",
          backgroundColor: colors[index],
          marginBottom: "10px"
        }}
      />
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
}
