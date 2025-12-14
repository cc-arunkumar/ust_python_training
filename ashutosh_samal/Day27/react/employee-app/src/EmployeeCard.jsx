import React from 'react'

const EmployeeCard = ({name,employeeId,role,location}) => {
  return (
    <div className='empcard'>
        <h2>Name : {name}</h2>
        <h3>Employee ID : {employeeId}</h3>
        <h3>Role : {role}</h3>
        <h3>Location : {location}</h3>
    </div>
  )
}

export default EmployeeCard