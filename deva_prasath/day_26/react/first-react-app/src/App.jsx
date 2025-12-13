import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {Greet,Greet1} from './Greet'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Helooo Carol</h1>
    <Greet />
    <Greet1 />
    <Greet />
    <Greet1 />
    

    </>
  )
}

export default App
