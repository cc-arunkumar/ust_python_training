import React from 'react'

const Card = ({children,cardname}) => {
  return (
    <div className={cardname}>
        {children}
    </div>
  )
}

export default Card