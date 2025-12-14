import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import EmployeeListing from './EmployeeListing'
import ProjectTeam from './ProjectTeam'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h2>A Reusable EmployeeCard Component</h2>
      <EmployeeListing name="Arjun" id={1} role="SDE1" location="TVM"/>
      <ProjectTeam name="Arjun" id={1} role="SDE1" location="TVM"/>
    </>
  )
}

export default App
