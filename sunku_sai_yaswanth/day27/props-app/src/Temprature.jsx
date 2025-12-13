import React from 'react'

const Temprature = ({city,weather}={...props}) => {
  return (
    <div className='card'>
      <h2>{city}</h2>
      <h4>Temprature:{weather} °c</h4>
    </div>
  )
}

export default Temprature
