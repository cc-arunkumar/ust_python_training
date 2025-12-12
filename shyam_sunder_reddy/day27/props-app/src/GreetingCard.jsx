import React from 'react'

const GreetingCard = ({colorname,name,message}={...props}) => {
  return (
    <div className={`card ${colorname}`}>
        <h2>{name}</h2>
        <h4>
          {message}
        </h4>
    </div>
  )
}

export default GreetingCard
