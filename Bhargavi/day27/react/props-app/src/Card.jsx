// Card.jsx
import React from "react";

const Card = ({ title, children }) => {
  return (
    <div className="card2">
      <h2>{title}</h2>
      <hr />
      <div>{children}</div>
    </div>
  );
};

export default Card;
