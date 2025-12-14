import React from 'react';

const WeatherCard = ({ city, temp }) => {
  return (
    <div>
      <h2>{city}</h2>
      <p>Temperature:{temp}°C</p>
    </div>
  );
};

export default WeatherCard;