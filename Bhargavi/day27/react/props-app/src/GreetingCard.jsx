import React from "react";

const GreetingCard = ({ name, ...props }) => {
  return (
    <div {...props}>
      <h2>good morning, {name}!</h2>
    </div>
  );
};

export default GreetingCard;
