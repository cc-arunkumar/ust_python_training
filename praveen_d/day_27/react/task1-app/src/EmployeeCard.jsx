import React from 'react'

const EmployeeCard = ({name,empid,role,location} = {...props}) => {
  return (
    <div>
        <p>Employeeid : {empid}</p>
        <p>Name : {name}</p>
        <p>Role : {role}</p>
        <p>Location : {location}</p>
    </div>
  )
}

export default EmployeeCard