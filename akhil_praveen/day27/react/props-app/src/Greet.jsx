import React from 'react'

const Greet = ({name,greet,cardname} = {...props}) => {
  return (
    <>
    <div className={cardname}>
      <h2>{name}</h2>
      <p>{greet}</p>
    </div>
    
    </>
  )
}

export default Greet