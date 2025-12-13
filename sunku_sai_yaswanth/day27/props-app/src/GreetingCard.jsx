import React from "react";

const GreetingCard = ({ name, great } = { ...props }) => {
  return (
    <div className="card">
      <h2>Good morning,{name}</h2>
      <h3>{great}</h3>
    </div>
  );
};

export default GreetingCard;
