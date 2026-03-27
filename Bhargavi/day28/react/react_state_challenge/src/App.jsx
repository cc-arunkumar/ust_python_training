// React State Challenge Sheet
// Level 1: Basic State
// 1. Counter
// Create a counter starting at 0.
// Add + and – buttons to change the count.
// 2. Toggle Message
// Button toggles a message: “Welcome to UST Dashboard!”.
// Clicking the button shows/hides the message.
// 3. Input Mirror
// Input field where whatever you type appears below in real-time.
// Level 2: Interactive State
// 1. Color Changer
// A div changes its background color when a button is clicked.
// Cycle through 3–4 colors.
// 2. Counter with Limits
// Counter with min 0 and max 10.
// Show an alert when limit is reached.
// 3. Visibility Toggle
// Create a “Show Details” button that reveals some hidden details.
// Clicking again hides the details.
// Level 3: Array/Object State
// 1. Task List Toggle
// List of 3 tasks.
// React State Challenge Sheet 1
// Each task has a “Complete” button that marks it done (strike-through).
// 2. Add Employee
// Input fields: name, role.
// Button “Add Employee” adds them to a list.
// 3. Remove Employee
// Extend above.
// Each employee has a remove button to delete them from the list.
// 4. Checkbox List
// List of 5 items with checkboxes.
// Maintain an array in state of checked items.
// Display checked items count below.
// �� Tips
// Use useState for every piece of changing data.
// Always update state via setter function, never mutate state directly.
// Use console.log() to debug your state updates.
// Try combining state with simple styling to see changes clearly.
// React State Challenge Sheet 2

import React from "react";
import Counter from "./Components/Counter";
import ToggleMessage from "./Components/ToggleMessage";
import InputMirror from "./Components/InputMirror";
import ColorChanger from "./Components/ColorChanger";
import CounterWithLimits from "./Components/CounterWithLimits";
import VisibilityToggle from "./Components/VisibilityToggle";
import TaskListToggle from "./Components/TaskListToggle";
import AddEmployee from "./Components/AddEmployee";
import RemoveEmployee from "./Components/RemoveEmployee";
import CheckboxList from "./Components/CheckboxList";
import "./index.css";

function App() {
  return (
    <div className="app">
      <div className="level-box">
        <h2>Level 1: Basic State</h2>
        <div className="level-section" style={{ backgroundColor: "#FAD02E" }}>
          <h3>Counter</h3>
          <Counter />
        </div>
        <div className="level-section" style={{ backgroundColor: "#FF6F61" }}>
          <h3>Toggle Message</h3>
          <ToggleMessage />
        </div>
        <div className="level-section" style={{ backgroundColor: "#6B4226" }}>
          <h3>Input Mirror</h3>
          <InputMirror />
        </div>
      </div>

      <div className="level-box">
        <h2>Level 2: Interactive State</h2>
        <div className="level-section" style={{ backgroundColor: "#4F8A8B" }}>
          <h3>Color Changer</h3>
          <ColorChanger />
        </div>
        <div className="level-section" style={{ backgroundColor: "#FFD700" }}>
          <h3>Counter with Limits</h3>
          <CounterWithLimits />
        </div>
        <div className="level-section" style={{ backgroundColor: "#FF6347" }}>
          <h3>Visibility Toggle</h3>
          <VisibilityToggle />
        </div>
      </div>

      <div className="level-box">
        <h2>Level 3: Array/Object State</h2>
        <div className="level-section" style={{ backgroundColor: "#FFB6C1" }}>
          <h3>Task List Toggle</h3>
          <TaskListToggle />
        </div>
        <div className="level-section" style={{ backgroundColor: "#98C4B4" }}>
          <h3>Add Employee</h3>
          <AddEmployee />
        </div>
        <div className="level-section" style={{ backgroundColor: "#D3B8AE" }}>
          <h3>Remove Employee</h3>
          <RemoveEmployee />
        </div>
        <div className="level-section" style={{ backgroundColor: "#6D9DC5" }}>
          <h3>Checkbox List</h3>
          <CheckboxList />
        </div>
      </div>
    </div>
  );
}

export default App;
