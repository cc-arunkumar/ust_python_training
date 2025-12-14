import React from 'react'
import EmployeeCard from './EmployeeCard'

const EmployeeList = () => {
  return (
    <div>
      <EmployeeCard name="Arun Kumar G."employeeId="123"role="Software Architect"location="Bangalore"/>
      <EmployeeCard name="Ashutosh"employeeId="1234"role="Devloper"location="Trivandrum"/>
      <EmployeeCard name="Deva"employeeId="1235"role="Devloper"location="Trivandrum"/>
      <EmployeeCard name="Prithvi"employeeId="1239"role="Devloper"location="Bangalore"/>
      <EmployeeCard name="Rohit"employeeId="1238"role="Testig"location="Hyderabad"/>
      <EmployeeCard name="Sovan"employeeId="1237"role="Devloper"location="Bangalore"/>
    </div>
  )
}

export default EmployeeList