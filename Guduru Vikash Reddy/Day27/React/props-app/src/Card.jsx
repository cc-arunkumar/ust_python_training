import React from 'react';

const Card = ({name,message}={...props}) => {
  return (
    <div className="Card">
   
      
      <h1>{name}</h1>
      <h2>{message}</h2>
    </div>
  )
};

export default Card;