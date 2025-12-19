import React from 'react'

const EmployeeCard = ({name,emp_id,role,location}) => {
  return (
    <div className='card' >
        <img src="img.svg" width="50px" height="50px" align="left"/>

        <h2>Name: {name}</h2>
        <h3>EmployeeID: {emp_id}</h3>
        <h3>Role: {role}</h3>
        <h3>Location: {location}</h3>
      
    </div>
  )
}

export default EmployeeCard
