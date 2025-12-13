import React, { useState } from "react";

const Level2 = () => {
  const [count, setCount] = useState(0);
  const [color, setColor] = useState("color1");
  const colors = ["color1", "color2", "color3", "color4"];
  const [toggle, settoggle] = useState(false);

  const handleColor = () => {
    const randomIndex = Math.floor(Math.random() * colors.length); // Corrected Math
    setColor(colors[randomIndex]);
  };
  const handleCount = () => {
    if (count < 10) {
      setCount((count) => count + 1);
    }
  };

  return (
    <>
      <div className="color_changer">
        <h2>Color changer</h2>
        <div className={color}>
          <button onClick={handleColor}>Change color</button>
        </div>
      </div>
      <div className="counter">
        <h2>Counter</h2>
        <div className="button_card">
          <button onClick={handleCount}>increase</button>
          <button onClick={() => setCount(0)}>reset</button>
        </div>
        count is {count}
        {count >= 10 && <p>Limit reached</p>}
      </div>
      <div className="toggle">
        <h2>Toggle Details</h2>
        <div>
          {toggle && <p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>}
          <button onClick={() => settoggle(!toggle)}>
            {!toggle && <p>Show details</p>}
            {toggle && <p>Hide details</p>}
            </button>
          {toggle && <p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>}
        </div>
      </div>
    </>
  );
};

export default Level2;
