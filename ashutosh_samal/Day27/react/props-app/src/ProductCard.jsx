import React from 'react'

const ProductCard = ({name,price,ratings}={...props}) => {
  return (
    <div className='card1'>
        <h2>Name: {name}</h2>
        <h3>Price: {price}</h3>
        <h3>Rating: {ratings}</h3>
    </div>
  )
}

export default ProductCard