import React from "react";

const Weathercard = ({ city, temp } = { ...props }) => {
  return (
    <div className="wcard">
      <h1> {city}</h1>
      <h2>{temp}</h2>
    </div>
  );
};

export default Weathercard;
