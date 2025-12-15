import { useState } from "react";

export default function VisibilityToggle() {
  const [visible, setVisible] = useState(false);

  return (
    <section className="card">
      <h3>Visibility Toggle</h3>
      <button onClick={() => setVisible(v => !v)}>
        {visible ? "Hide Details" : "Show Details"}
      </button>
      {visible && (
        <div className="panel">
          <p>Here are the hidden details!</p>
        </div>
      )}
    </section>
  );
}
