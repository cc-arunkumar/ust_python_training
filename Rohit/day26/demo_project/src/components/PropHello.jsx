import React from 'react'

const PropHello = ({tag_name,description}={...props}) => {
  return (
     
        <div className="card">
          <h1 className="tag-name">{tag_name}</h1>
          <p className="text">
            {description}
          </p>
        </div>
    
  )
}

export default PropHello
