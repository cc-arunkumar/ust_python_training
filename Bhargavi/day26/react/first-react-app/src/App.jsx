import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Hello from './Hello'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <h1>Hello World!</h1>
      <Hello />
      <Hello />
      <Hello />
      <Hello />
      </div>
    </>
  )
}

export default App

