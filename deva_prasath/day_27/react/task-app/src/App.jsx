import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import EmployeeList from './EmployeeList'
import EmployeeCard from './EmployeeCard'
import ProjectTeam from './ProjectTeam'; // Add this import

function App() {

  return (
    <>
      <h1>Employee List</h1>
      <EmployeeList />

      <h1>Manager List</h1>

      <ProjectTeam />

    </>
  )
}

export default App
