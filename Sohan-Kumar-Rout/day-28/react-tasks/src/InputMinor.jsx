import { useState } from "react";

export default function InputMirror() {
  const [text, setText] = useState("");

  return (
    <div>
      <input 
        type="text" 
        onChange={(e) => setText(e.target.value)} 
        placeholder="Type something..."
      />
      <p>{text}</p>
    </div>
  );
}
