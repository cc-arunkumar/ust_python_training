import { useState } from 'react'
import './App.css'
import Greet from './Greet'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="app-container">
      <h1 className="main-title"><center>Hello World!</center></h1>
      <div className="greet-grid">
         <Greet 
        message="Hello, welcome to my React app!" 
        author="Harsh" 
      />
      <Greet 
        message="KOKA" author="KA" 
      />
        <Greet message="Kyaa haal bhai ke" author="Author 2:- TBSM"/>
        <Greet />
        <Greet />
        <Greet />
      </div>
    </div>
  )
}

export default App