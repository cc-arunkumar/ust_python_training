import React from 'react'

function ProdectCard({name,cost,rating}={...props}) {
  return (
    <div className='card'>
      <h4>{name}</h4>
      <h3>cost:{cost}</h3>
      <h3>Rating:{rating}</h3>

    </div>
  )
}

export default ProdectCard
