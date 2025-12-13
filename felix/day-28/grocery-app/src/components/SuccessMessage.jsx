import React, { useEffect } from 'react';

const SuccessMessage = ({ message, onClose }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, 3000);
    return () => clearTimeout(timer);
  }, [onClose]);

  return (
    <div className="success-message">
      <p>{message}</p>
    </div>
  );
};

export default SuccessMessage;