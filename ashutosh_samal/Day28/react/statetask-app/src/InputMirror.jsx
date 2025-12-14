import React, { useState } from "react";

const InputMirror = () => {
  const [input, setInput] = useState("");

  return (
    <div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <p>{input}</p>
    </div>
  );
};

export default InputMirror;
