import React, { useState } from 'react';

const InputMirror = () => {
  const [inputValue, setInputValue] = useState(""); // State for input value

  return (
    <div>
      <input 
        type="text" 
        value={inputValue} 
        onChange={(e) => setInputValue(e.target.value)} // Update state on input change
      />
      <p>{inputValue}</p>
    </div>
  );
};

export default InputMirror;
