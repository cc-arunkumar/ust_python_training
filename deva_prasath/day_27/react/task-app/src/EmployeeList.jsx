import React from 'react'
import EmployeeCard from './EmployeeCard'
const EmployeeList = () => {

  return (
    <div>
<EmployeeCard name="Deva" employee_id={101} role="AI Engineer" location="Salem" />
<EmployeeCard name="Asutosh" employee_id={102} role="SDE-1" location="Odisha" />
</div>
  )
}

export default EmployeeList