import React, { useState } from "react";

function InputMirror() {
  const [input, setInput] = useState("");

  return (
    <div className="box">
      <input
        type="text"
        placeholder="Type something"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <p>{input}</p>
    </div>
  );
}

export default InputMirror;
