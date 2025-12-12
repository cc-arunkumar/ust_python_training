import React from 'react'

const Wheather = ({city,temp,cardname} = {...props}) => {
  return (
    <>
    <div className={cardname}>
      <h2>{city}</h2>
      <p>{temp}&#176;C</p>
    </div>
    
    </>
  )
}

export default Wheather