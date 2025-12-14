import { useState } from 'react'
import ShoppingApp from './ShoppingApp'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <ShoppingApp/>
      </div>
    </>
  )
}

export default App
