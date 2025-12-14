import { useState } from 'react'
import './App.css'
import Counter from './Counter'
import ToggleMessage from './ToggleMessage'
import InputMirror from './InputMirror'
import ColorChanger from './ColorChanger'
import CounterWithLimits from './CounterWithLimits'
import VisibilityToggle from './VisibilityToggle'
import TaskListToggle from './TaskListToggle'
import AddEmployee from './AddEmployee'
import RemoveEmployee from './RemoveEmployee'
import CheckboxList from './CheckboxList'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <h2>Counter</h2>
        <Counter/>
      </div>
      <br />
      <div>
        <h2>Toggle Message</h2>
        <ToggleMessage/>
      </div>
      <br />
      <div>
        <h2>Input Mirror</h2>
        <InputMirror/>
      </div>
      <br />
      <div>
        <h2>Color Changer</h2>
        <ColorChanger/>
      </div>
      <br />
      <div>
        <h2>Counter with Limits</h2>
        <CounterWithLimits/>
      </div>
      <br />
      <div>
        <h2>Visibility Toggle</h2>
        <VisibilityToggle/>
      </div>
      <br />
      <div>
        <h2>Task List Toggle</h2>
        <TaskListToggle/>
      </div>
      <br />
      <div>
        <h2>Add Employee</h2>
        <AddEmployee/>
      </div>
      <br />
      <div>
        <h2>Remove Employee</h2>
        <RemoveEmployee/>
      </div>
      <br />
      <div>
        <h2>Checkbox List</h2>
        <CheckboxList/>
      </div>
    </>
  )
}

export default App
