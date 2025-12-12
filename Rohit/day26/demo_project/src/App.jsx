import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Hello from './components/Hello'
import Temperature from './components/Temperature'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <Hello/>
     <div className='temp-head'>

     <Temperature food="munch" cost="24" rating="4.2"/>         
     <Temperature food="munch" cost="24" rating="4.2"/>         
     <Temperature food="munch" cost="24" rating="4.2"/>         
     </div>
    </>
  )
}

export default App
