import React from 'react'
import './App.css'

const ProductCard = ({ name, price, rating }) => {
  return (
    <div className="product-card">
      <h2>{name}</h2>
      <p>💰 Price: {price}</p>
      <p>⭐ Rating: {rating}</p>
    </div>
  )
}

export default ProductCard
