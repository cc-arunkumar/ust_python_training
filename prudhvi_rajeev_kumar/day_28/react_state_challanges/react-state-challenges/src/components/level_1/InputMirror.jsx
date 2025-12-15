import { useState } from "react";

export default function InputMirror() {
  const [text, setText] = useState("");

  return (
    <section className="card">
      <h3>Input Mirror</h3>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type here..."
      />
      <p>{text}</p>
    </section>
  );
}
