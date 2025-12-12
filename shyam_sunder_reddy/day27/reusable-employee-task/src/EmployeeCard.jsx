import React from 'react'
import OIP from './assets/react.svg'

const EmployeeCard = ({name,employeeid,role,location}={...props}) => {
  return (
    <div className='employee'>

        <h2>{name}</h2>
        <h4>Employee Id : {employeeid}</h4>
        <h4>Role : {role}</h4>
        <h4>location : {location}</h4>
    </div>
  )
}

export default EmployeeCard
