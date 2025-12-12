import React from 'react'

const Greet = ({ message, author }) => {
  return (
    <div className="greet-card">
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero suscipit facilis ab quas omnis mollitia dolore beatae.
      </p>
      <p>{message}</p>
      <p>{author}</p>
    </div>
  )
}

export default Greet