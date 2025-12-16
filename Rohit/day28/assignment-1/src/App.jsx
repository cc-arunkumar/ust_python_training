import { useState } from 'react'
import './App.css'
import Toggle from './components/Toggle'
import InputMirror from './components/InputMirror'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>

      <div className="card">
        <button >
          Value {count}
        </button>
      </div>
      <div>
        <button onClick={()=> setCount((count)=> count+1)}>Plus</button>
      </div>
      <div>
        <button onClick={()=> setCount((count)=> count-1)}>Minus</button>
      </div>
    <Toggle/>
    <InputMirror/>
      
    </>
  )
}

export default App
