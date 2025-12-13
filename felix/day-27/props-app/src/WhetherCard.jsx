import React from 'react'

export default function WhetherCard({name,temparature} = {...props}) {
  return (
    <div className='card'>
          <h2>{name}</h2>
          <p>Temparature: {temparature} °C</p>
    </div>
  )
}
