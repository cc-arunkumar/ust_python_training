import React from 'react'
 
const ProductCard=({name,price,rating}={...props})=> {
  return (
    <div className='product-card'>
        <h2>{name}</h2>
        <h4>Price: {price}</h4>
        <h4>Rating: {rating}</h4>
     
    </div>
  )
}
 
export default ProductCard