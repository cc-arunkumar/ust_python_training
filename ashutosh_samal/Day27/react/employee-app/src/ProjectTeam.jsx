import React from 'react'
import EmployeeCard from './EmployeeCard'

const ProjectTeam = () => {
  return (
    <div>
      <EmployeeCard name="Arun Kumar G."employeeId="123"role="Software Architect"location="Bangalore"/>
      <EmployeeCard name="Ashutosh"employeeId="1234"role="Devloper"location="Trivandrum"/>
      <EmployeeCard name="Deva"employeeId="1235"role="Devloper"location="Trivandrum"/>
    </div>
  )
}

export default ProjectTeam