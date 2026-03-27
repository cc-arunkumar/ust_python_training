import React, { useState } from "react";

function VisibilityToggle() {
  const [visible, setVisible] = useState(false);

  return (
    <div className="box">
      <button onClick={() => setVisible(!visible)}>
        {visible ? "Hide" : "Show"} Details
      </button>
      {visible && <p>Here are the hidden details...</p>}
    </div>
  );
}

export default VisibilityToggle;
