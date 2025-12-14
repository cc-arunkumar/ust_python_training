import React from 'react'

const Weather = ({city,temp}={...props}) => {
  return (
    <>
    <div className='weather-card'>
        <h2>{city[0]}</h2>
        <p>Temperature : {temp[0]}°C</p>
    </div>
    <div className='weather-card'>
        <h2>{city[1]}</h2>
        <p>Temperature : {temp[1]}°C</p>
    </div>
    </>
  )
}

export default Weather;