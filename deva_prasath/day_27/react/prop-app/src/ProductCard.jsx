import React from 'react'

const ProductCard = ({name,price,rating}) => {
  return (
    <div className="product-card">
        <h2>{name}</h2>
        <h3>Cost:{price}</h3>
        <h3>Rating:{rating}</h3>
    </div>
  )
}

export default ProductCard