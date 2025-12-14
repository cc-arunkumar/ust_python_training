import React, { useState } from "react";

const VisibilityToggle = () => {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div>
      <button onClick={() => setIsVisible(!isVisible)}>
        {isVisible ? "Hide" : "Show"} Details
      </button>
      {isVisible && <p>Here are some hidden details.</p>}
    </div>
  );
};

export default VisibilityToggle;
