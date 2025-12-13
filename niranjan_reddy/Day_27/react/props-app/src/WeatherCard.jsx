import React from "react";

const WeatherCard = ({ city, temprature } = { ...props }) => {
  return (
    <div className="card">
      <h1>{city}</h1>
      <h2>Temprature: {temprature}°C</h2>
    </div>
  );
};

export default WeatherCard;
