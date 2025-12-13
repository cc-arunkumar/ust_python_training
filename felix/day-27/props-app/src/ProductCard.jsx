import React from 'react'

export default function ProductCard({name,price,rating} = {...props}) {
  return (
    <div className='card'>
      <h4>{name}</h4>
      <p>Cost: {price}💵</p>
      <p>Rating: {rating}⭐</p>
    </div>
  )
}
