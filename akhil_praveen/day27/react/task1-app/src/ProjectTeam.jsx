import React from 'react'
import EmployeeCard from './EmployeeCard'

const ProjectTeam = ({cardname}) => {
  return (
    <div className={cardname}>
        <h2>Project Team</h2>
        <EmployeeCard name = "Akhil" empid= {101} role="IT" location="TVM"/>
    </div>
  )
}

export default ProjectTeam