import React from 'react'

const EmployeeCard = ({name,employee_id,role,location}) => {
  return (
    <div  className='card'>
        <h2>Name:{name}</h2>
        <h2>Employee id:{employee_id}</h2>
        <h2>Role:{role}</h2>
        <h2>Location:{location}</h2>
    </div>
  )
}

export default EmployeeCard
