import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Hello from './Hello.jsx'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1 className='hello'>Hello Sunku 👋</h1>

      <Hello/>
      <Hello/>
      <Hello/>
      <Hello/>
      <Hello/>
      <Hello/>
    </>
  )
}

export default App
