import React from 'react'
import EmployeeCard from './EmployeeCard'

const ProjectList = () => {
  return (
    <div>
        <h2>Project Team</h2>
        <EmployeeCard name="shyam" employeeid={101} role="Developer-I" location="Trivandrum"/>
        <EmployeeCard name="Ram" employeeid={102} role="Lead-II" location="Hyderabad"/>
        <EmployeeCard name="anjan" employeeid={103} role="Developer-II" location="Trivandrum"/>
        <EmployeeCard name="arun" employeeid={104} role="Tester-II" location="Chennai"/>
    </div>
  )
}

export default ProjectList
