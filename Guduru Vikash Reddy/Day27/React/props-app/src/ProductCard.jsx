import React from 'react'

const ProductCard = ({name,price,rating}) => {
  return (
    <div className="ProductCard">
     <h4>{name}</h4>
     <p>cost:{price}💵 </p>
     <p>Rating:{rating}</p>
    </div>
  )
}

export default ProductCard