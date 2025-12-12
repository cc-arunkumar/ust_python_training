import React from 'react'

const Greet = ({colorname}) => {
  return (
    <div className={`card ${colorname}`}>
        <h3>HELLO</h3>
      <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
        Asperiores odit dolorem tempore quo voluptates molestiae rerum repellendus vero maxime, quisquam explicabo expedita eaque pariatur laboriosam enim velit, 
        minima delectus modi!</p>
    </div>
  )
}

export default Greet
