import { useState } from "react";

export default function ColorChanger() {
  const colors = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b"];
  const [index, setIndex] = useState(0);

  return (
    <section className="card">
      <h3>Color Changer</h3>
      <div
        className="box"
        style={{ backgroundColor: colors[index] }}
      />
      <button onClick={() => setIndex(i => (i + 1) % colors.length)}>
        Change Color
      </button>
    </section>
  );
}
