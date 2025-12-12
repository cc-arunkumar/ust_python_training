import React from 'react'

const EmployeeCard = ({name,role, employee_id,location}) => {
  return (
    <div>
      <h1>{name}</h1>
      <h1>{role}</h1>
      <h1>{employee_id}</h1>
      <h1>{location}</h1>
    </div>
  )
}

export default EmployeeCard
