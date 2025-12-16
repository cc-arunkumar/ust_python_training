import React, { useState } from 'react';

const InputMirror = () => {
  const [text, setText] = useState("");

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Input Mirror</h2>
      <input 
        type="text" 
        value={text} 
        onChange={(e) => setText(e.target.value)} 
        placeholder="Type something..."
        style={styles.input}
      />
      <p style={styles.mirror}>{text}</p>
    </div>
  );
};

// Inline styles with linear gradient
const styles = {
  container: {
    textAlign: "center",
    padding: "2rem",
    borderRadius: "12px",
    background: "linear-gradient(135deg, #89f7fe, #66a6ff)",
    boxShadow: "0 8px 20px rgba(0,0,0,0.2)",
    maxWidth: "400px",
    margin: "2rem auto",
    fontFamily: "Segoe UI, sans-serif"
  },
  heading: {
    marginBottom: "1rem",
    color: "#333"
  },
  input: {
    padding: "10px",
    borderRadius: "6px",
    border: "1px solid #ccc",
    width: "80%",
    marginBottom: "1rem",
    fontSize: "1rem"
  },
  mirror: {
    fontSize: "1.2rem",
    fontWeight: "bold",
    color: "#222"
  }
};

export default InputMirror;
