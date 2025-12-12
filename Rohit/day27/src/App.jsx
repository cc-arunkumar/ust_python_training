import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import EmployeeList from './component/EmployeeList'
import Project from './component/Project'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <EmployeeList/>
      <Project/>

    </>
  )
}

export default App
