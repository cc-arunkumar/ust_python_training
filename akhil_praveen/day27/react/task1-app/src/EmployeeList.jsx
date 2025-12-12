import React from 'react'
import EmployeeCard from './EmployeeCard'


const EmployeeList = ({cardname}) => {
  return (
    <div className={cardname}>
        <h2>Employee List</h2>
        <EmployeeCard name = "Akhil" empid= {101} role="IT" location="TVM"/>
    </div>
  )
}

export default EmployeeList