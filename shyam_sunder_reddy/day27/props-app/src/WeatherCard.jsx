import React from 'react'

const WeatherCard=({city,temperature}={...props})=> {
  return (
    <div className='weathercard'>
        <h2>{city}</h2>
        <h4>Temperature: {temperature}°C</h4>
      
    </div>
  )
}

export default WeatherCard
