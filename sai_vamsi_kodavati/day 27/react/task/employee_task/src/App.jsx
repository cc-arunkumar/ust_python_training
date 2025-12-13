import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import './index.css'
import EmployeeList from './EmployeeList'
import ProjectTeam from './ProjectTeam'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <EmployeeList/>
      <ProjectTeam/>
    </>
  )
}

export default App
