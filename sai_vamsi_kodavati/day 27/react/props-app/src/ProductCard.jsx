import React from 'react'

const ProductCard = ({name,price,rating}) => {
  return (
    <div className="GreetingCard">
      <h2>{name}</h2>
      <p>Cost:{price}</p>
      <p>Rating:{rating}</p>
    </div>
  )
}

export default ProductCard
