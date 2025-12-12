import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import EmployeeList from './EmployeeList'
import ProjectTeam from './ProjectTeam'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>A Reusable EmployeeCard 
Component</h1>
    <div className='card_container'>
      <EmployeeList cardname = "card1"></EmployeeList>
      <ProjectTeam cardname  = "card2"></ProjectTeam>
    </div>
    </>
  )
}

export default App
