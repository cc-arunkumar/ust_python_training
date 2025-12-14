import React from 'react'

const GreetingCard = ({name,greet}) => {
  return (
    <div className='card1'>
        <h2>{name}</h2>
        <h3>{greet}</h3>
    </div>
  )
}

export default GreetingCard