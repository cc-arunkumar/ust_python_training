import React from 'react'

const WeatherCard = ({city,Temparature}={...props}) => {
  return (
    <div className="WeatherCard">
     <h1>{city}</h1>
     <h2>{Temparature}</h2>
    </div>
  )
}

export default WeatherCard