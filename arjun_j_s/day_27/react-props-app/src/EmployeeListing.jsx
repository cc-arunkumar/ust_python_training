import React from 'react'
import EmployeeCard from './EmployeeCard'

const EmployeeListing = ({name,id,role,location}) => {
  return (
    <EmployeeCard>
        <h2>Employee Listing</h2>
        <p>Name : {name}</p>
        <p>Emp ID : {id}</p>
        <p>Role : {role}</p>
        <p>Location : {location}</p>
    </EmployeeCard>
  )
}

export default EmployeeListing