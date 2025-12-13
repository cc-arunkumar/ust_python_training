import React from "react";

const WeatherCard = ({ city, temperature, ...props }) => {
  return (
    <div className="card1" {...props}>
      <h2>{city}</h2>
      <h3>Temp:{temperature}</h3>
    </div>
  );
};

export default WeatherCard;
