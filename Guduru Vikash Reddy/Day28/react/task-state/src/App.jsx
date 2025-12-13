import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ToggleMessage from './ToggleMessage'
import InputMirror from './InputMirror'
import Counter from './Counter'
import VisibilityToggle from './VisibilityToggle'
import CounterWithLimits from './CounterWithLimits'
import ColorChanger from './ColorChanger'

import CheckboxList from './CheckboxList.'
import ManageEmployees from './ManageEmployees'
import AddEmployee from './AddEmployee'
import TaskListToggle from './TaskListToggle'
import Increment from './Increment'
import Decrement from './Decrement'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <ToggleMessage />
      <Counter />
      <InputMirror /> */}
      {/* <VisibilityToggle />
      <CounterWithLimits />
      <ColorChanger /> */}
      {/* <CheckboxList />
      <ManageEmployees />
      <AddEmployee />
      <TaskListToggle /> */}

      <Increment />

    </>
  )
}



export default App;
