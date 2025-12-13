import { useState } from "react";
import "./App.css";

function App() {
  const colors = ["lightblue", "lightgreen", "lightcoral", "khaki"];

  const [index, setIndex] = useState(0);

  const changeColor = () => {
    setIndex((prevIndex) => (prevIndex + 1) % colors.length);
  };

  return (
    <div className="App">
      <h1>Color Changer</h1>

      <div
        className="color-box"
        style={{ backgroundColor: colors[index] }}
      >
        Background Color: {colors[index]}
      </div>

      {/* Button to change color */}
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
}

export default App;
