import React from "react";

const GreetingCard = ({ name, greet } = { ...props }) => {
  return (
    <div className="GreetingCard">
      <h1>{name}</h1>
      <h2>{greet}</h2>
    </div>
  );
};

export default GreetingCard;
