import React from 'react'
import EmployeeCard from './EmployeeCard'
const ProjectTeam = () => {
  return (
    <div>
      <EmployeeCard name="Arumueksh" emp_id={123} role="DEveloper" location="Chennai"/>
      <EmployeeCard name="John Doe" emp_id={124} role="Designer" location="New York"/>
      <EmployeeCard name="Jane Smith" emp_id={125} role="Manager" location="London"/>
    </div>
  )
}

export default ProjectTeam
