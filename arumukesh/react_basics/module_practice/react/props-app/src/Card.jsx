import React from 'react'

const Card = ({children}={...props}) => {
  return (
    <div className='card' text-align="center" >
        {/* <h2>Name:{product}</h2>
        <h3>Price{price}</h3>
        <h3>Rating{rating}</h3> */}
        {children}
    </div>
  )
};

export default Card
