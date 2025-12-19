import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card  from './Card.jsx'
import EmployeeList from './EmployeeList.jsx'
import ProjectTeam from './ProjectTeam.jsx'
function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <EmployeeList/>
        <ProjectTeam/>
        
          {/* <Card/>
        <Card product="Munch" price={22} rating={2.2}/>
        <Card product="Kitkat" price={28} rating={3.5}/> */}
        {/* <Card product="python" tprice=5}/>
        <Card product="python" tprice=3}/> */}
      </div>
    
      
    </>
  )
}

export default App
