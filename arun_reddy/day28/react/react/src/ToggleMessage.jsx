import React, { useState } from "react";

export default function ToggleMessage() {
  const [count, setcount] = useState(0);
  return (
    <div>
      <button
        onClick={() => (count == 0 ? setcount(count + 1) : setcount(count - 1))}
      >
        ClickME
      </button>
      <span>{count > 0 && <p>Welcome to UST Dashboard</p>}</span>
    </div>
  );
}
