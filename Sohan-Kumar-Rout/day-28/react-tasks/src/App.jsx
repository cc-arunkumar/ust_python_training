import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Counter from './Counter'
import TogleEvent from './TogleEvent'
import InputMirror from './InputMinor'
import ColorChanger from './ColourChanger'
import LimitedCounter from './LimitedCounter'
import VisibilityToggle from './VisibilityToggle'
import TaskList from './TaskList'
import EmployeeList from './EmployeeList'
import CheckboxList from './CheckBoxList'
import AddEmployee from './AddEmployee'
import Increment from '../Increment'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <Counter/>
    <TogleEvent/>
    <InputMirror/>
    <ColorChanger/>
    <LimitedCounter/>
    <VisibilityToggle/>  
    <TaskList/>
    <EmployeeList/>
    <CheckboxList/>
    <AddEmployee/>   */}
    <Increment/>
    </>
  )
}

export default App
