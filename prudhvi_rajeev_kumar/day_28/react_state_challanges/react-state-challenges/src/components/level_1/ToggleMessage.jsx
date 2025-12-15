import { useState } from "react";

export default function ToggleMessage() {
  const [show, setShow] = useState(false);

  return (
    <section className="card">
      <h3>Toggle Message</h3>
      <button onClick={() => setShow(s => !s)}>Toggle</button>
      {show && <p>Welcome to UST Dashboard!</p>}
    </section>
  );
}
