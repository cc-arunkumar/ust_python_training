import React from 'react'

// const GreetingCard = ({name}={...props}) => {
//   return (
//     <h2>
//         Good Morning,{name}!
//     </h2>
//   )
// }

const GreetingCard = ({name,greet}={...props}) => {
  return (
    <div className="card1">
    <h2>{name}</h2>
    <h3>{greet}</h3>
    </div>
  )
}

export default GreetingCard