import React, { useState } from 'react';

const ToggleMessage = () => {
  const [isVisible, setIsVisible] = useState(false); // Initially the message is hidden

  return (
    <div>
      <button onClick={() => setIsVisible(!isVisible)}>
        Toggle Message
      </button>
      {isVisible && <p>Welcome to UST Dashboard!</p>}
    </div>
  );
};

export default ToggleMessage;
