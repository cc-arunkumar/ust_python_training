import React from 'react'

const Product = ({name,price,rating,cardname} = {...props}) => {
  return (
    <>
    <div className={cardname}>
      <h2>{name}</h2>
      <p>Cost: ${price}💵</p>
      <p>Rating: {rating}⭐</p>
    </div>
    
    </>
  )
}

export default Product