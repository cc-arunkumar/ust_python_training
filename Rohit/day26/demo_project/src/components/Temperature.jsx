import React from 'react'
import "./Temaparature.css"
const Temperature = ({food,cost,rating}) => {
  return (
    <div className='box'>
        <h2>{food}</h2>
        <h4>{cost}</h4>
        <h5>{rating}</h5>
      
    </div>
  )
}

export default Temperature
