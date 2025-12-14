import React from 'react'

const Hello = ({first,second}={...props}) => {
  return (
    <>
    <div className='card'>
        <h2>{first[0]}</h2>
        <p>{first[1]}</p>
    </div>
    <div className='card-two'>
        <h2>{second[0]}</h2>
        <p>{second[1]}</p>
    </div>
    </>
  )
}

export default Hello