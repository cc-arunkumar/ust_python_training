import React from 'react'

export default function GreetingCard({name,text} = {...props}) {
  return (
    <>
      <div className='card'>
          <h2>{name}</h2>
          <p>{text}</p>
      </div>
    </>
  )
}
