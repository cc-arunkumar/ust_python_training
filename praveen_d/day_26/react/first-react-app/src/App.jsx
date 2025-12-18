import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Greet from './Greet'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div class='title'>
    <h1>Hello World</h1>
    </div>
    <Greet/>
    <Greet/>
    <Greet/>
    <Greet/>
    <Greet/>
    <Greet/>
    <Greet/>
    <Greet/>
    </>
    )
}

export default App
