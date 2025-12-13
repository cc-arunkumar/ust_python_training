import { useState } from "react";

export default function ToggleMessage() {
  const [show, setShow] = useState(false);

  return (
    <div>
      <button onClick={() => setShow(!show)}>Toggle Message</button>
      {show && <p>Welcome to UST Dashboard!</p>}
    </div>
  );
}
