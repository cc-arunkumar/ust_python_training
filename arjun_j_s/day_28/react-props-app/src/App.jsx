import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Increment from './Increment'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Increment/>
      
    </>
  )
}

export default App
