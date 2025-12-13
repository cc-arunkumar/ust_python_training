import React from 'react'

const Weather = ({ city, temperature }) => {
  return (
    <div className="weather-card">
      <h1>{city}</h1>
      <p>{temperature}°C</p>
    </div>
  )
}

export default Weather
