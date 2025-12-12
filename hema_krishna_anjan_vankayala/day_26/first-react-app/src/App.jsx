import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Hello from './Hello.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div>
        <Hello colorname="color1" />
        <Hello colorname="color2" />
        <Hello colorname="color1" />
        <Hello colorname="color2" />
        <Hello colorname="color1" />
        <Hello colorname="color2" />
      
      </div>
   
    </>
  )
}

export default App
