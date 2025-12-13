import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Greet from './Greet'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Hey There.....</h1>
    <div className='left-side'><Greet/></div>
    <div className='right-side'><Greet/></div>
    <div className='left-side'><Greet/></div>
    <div className='right-side'><Greet/></div>
    <div className='left-side'><Greet/></div>
    <div className='right-side'><Greet/></div>
    </>
  )
}

export default App
