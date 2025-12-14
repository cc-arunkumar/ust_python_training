import { useState } from 'react'

import './App.css'
import EmployeeList from './EmployeeList'
import ProjectTeam from './ProjectTeam'

function App() {

  return (
    <>
      
      <div>
        <h2>List Of Employees</h2>
        <EmployeeList/>
      </div>

      <div>
        <h2>Meet The Project Team</h2>
        <ProjectTeam/>
      </div>
    </>
  )
}

export default App
