import React from 'react'

const EmployeeCard = ({name,employeeid,role,location}) => {
  return (
    <div className='employee-card'>
        <h2>Employee Card</h2>
        
        <p>Name : {name}</p>
        <p>EmployeeID : {employeeid}</p>
        <p>Role : {role}</p>
        <p>Location : {location}</p>
    </div>
  )
}

export default EmployeeCard