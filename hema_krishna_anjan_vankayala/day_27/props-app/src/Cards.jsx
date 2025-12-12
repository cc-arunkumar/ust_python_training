import React from 'react'

const Cards = ({name,cost,rating,colorname}) => {
  return (
    <div className={`card ${colorname}`}>
        <h3 className="headfont">{name}</h3>
        <p className="font">Cost:{cost} </p>
        <p className="font">Rating:{rating}</p>
        </div>
  )
}

export default Cards
