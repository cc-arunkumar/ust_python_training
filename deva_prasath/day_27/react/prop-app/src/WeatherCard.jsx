import React from 'react'

const WeatherCard = ({city,temperature}={...props}) => {
  return (
    <div className='weather'>
        <h2>{city}</h2>
        <h3>{temperature}</h3>
    </div>
  )
}

export default WeatherCard