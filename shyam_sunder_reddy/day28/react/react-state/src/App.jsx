import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Counter from './Counter.jsx'
import ToggleMessage from './ToggleMessage.jsx'
import InputMirror from './InputMirror.jsx'
import ColorChanger from './ColorChanger.jsx'
import LimitedCounter from './LimitedCounter.jsx'
import VisibilityToggle from './VisibilityToggle.jsx'
import TaskList from './TaskList.jsx'
import EmployeeList from './EmployeeList.jsx'
import EmployeeListWithRemove from './EmployeeListWithRemove.jsx'
import CheckboxList from './ChechboxList.jsx'

function App() {

  return (
    <>
      {/* <Counter/> */}
      {/* <ToggleMessage/> */}
      {/* <InputMirror/> */}
      {/* <ColorChanger/> */}
      {/* <LimitedCounter/> */}
      {/* <VisibilityToggle/> */}
      {/* <TaskList/> */}
      <EmployeeList/>
      <EmployeeListWithRemove/>
      <CheckboxList/>
    </>
  )
}

export default App
