import React, { useState } from 'react';

const VisibilityToggle = () => {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div>
      <button onClick={() => setIsVisible(!isVisible)}>
        {isVisible ? 'Hide Details' : 'Show Details'}
      </button>
      {isVisible && <p>Nan dhan da Leooo</p>}
    </div>
  );
};

export default VisibilityToggle;
