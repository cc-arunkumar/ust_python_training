import { useState } from "react";

export default function VisibilityToggle() {
  const [show, setShow] = useState(false);

  return (
    <div>
      <button onClick={() => setShow(!show)}>
        {show ? "Hide Details" : "Show Details"}
      </button>

      {show && <p>Here are some hidden details...</p>}
    </div>
  );
}
