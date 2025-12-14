import React from 'react'

const Product = ({name,cost,rating}={...props}) => {
  return (
    <>
    <div className='choco-card'>
        <h2>{name[0]}</h2>
        <p>Price : ₹{cost[0]}</p>
        <p>Rating : {rating[0]}⭐</p>
    </div>
    <div className='choco-card'>
        <h2>{name[1]}</h2>
        <p>Price : ₹{cost[1]}</p>
        <p>Rating : {rating[1]}⭐</p>
    </div>
    <div className='choco-card'>
        <h2>{name[2]}</h2>
        <p>Price : ₹{cost[2]}</p>
        <p>Rating : {rating[2]}⭐</p>
    </div>
    </>
  )
}

export default Product;