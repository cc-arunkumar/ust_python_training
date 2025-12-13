import React from "react";

import { useState } from "react";

export default function InputMirror() {
  const [text, setText] = useState("");

  return (
    <div className="input-mirror-container">
      <div className="input-mirror-card">
        <h1 className="input-mirror-title">Input Mirror</h1>

        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type something..."
          className="input-mirror-field"
        />

        <div className="input-mirror-display">
          <p className="input-mirror-text">
            {text || (
              <span className="input-mirror-placeholder">
                Your text will appear here...
              </span>
            )}
          </p>
        </div>
      </div>
    </div>
  );
}
