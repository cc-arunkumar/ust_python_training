import React from 'react'

const GreetingCard = ({name, greet}) => {
  return (
    <h2 className='cards'>{name}  {greet}</h2>
  )
}

export default GreetingCard