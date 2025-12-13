import React from 'react'

const WeatherCard = ({city,degree} = {...props}) => {
  return (
    <div className="GreetingCard">
      <h1>{city}</h1>
      <p>Temperature:{degree}</p>
    </div>
  )
}

export default WeatherCard
