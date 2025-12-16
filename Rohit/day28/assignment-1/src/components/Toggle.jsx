import { useState } from 'react'
const Toggle = () => {
const [val ,setVal] = useState("")
  return (
    <div>
        <button onClick={()=> setVal("welecome to ust dashboard")}>CLick me</button>
        <p>{val}</p>
        <button onClick={()=> setVal("")}>Remove text</button>
      
    </div>
  )
}

export default Toggle
