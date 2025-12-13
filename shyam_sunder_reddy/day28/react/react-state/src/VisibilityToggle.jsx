import { useState } from "react";
function VisibilityToggle() {
  const [visible, setVisible] = useState(false);

  return (
    <div>
      <button onClick={() => setVisible(!visible)}>
        {visible ? "Hide Details" : "Show Details"}
      </button>
      {visible && <p>Here are some hidden details...</p>}
    </div>
  );
}

export default VisibilityToggle