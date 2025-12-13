import React, { useState } from "react";

// Array component to handle tasks, employees, and shopping list functionalities
function Array() {
  // State for managing tasks with their completion status
  const [tasks, setTasks] = useState([
    { id: 1, text: "Task 1", done: false },
    { id: 2, text: "Task 2", done: false },
    { id: 3, text: "Task 3", done: false },
  ]);

  // State for managing employees
  const [employees, setEmployees] = useState([]);
  
  // State for handling input fields for new employees
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  // Function to add a new employee to the list
  const addEmployee = () => {
    if (name && role) {
      setEmployees([...employees, { id: Date.now(), name, role }]);
      setName(""); // Reset name field after adding
      setRole(""); // Reset role field after adding
      console.log(employees); // Log current list of employees
    }
  };

  // Function to mark a task as completed (done)
  const completeTask = (id) => {
    setTasks(tasks.map(task =>
      task.id === id ? { ...task, done: true } : task
    ));
    console.log(tasks); // Log updated tasks list
  };

  // Function to remove an employee from the list
  const removeEmployee = (id) => {
    setEmployees(employees.filter(emp => emp.id !== id));
    console.log(employees); // Log updated employees list
  };

  // Example shopping list items
  const items = ["Apples", "Bananas", "Carrots", "Milk", "Bread"];
  
  // State for managing the items that are checked
  const [checked, setChecked] = useState([]);

  // Function to toggle check/uncheck an item in the shopping list
  const toggleCheck = (item) => {
    setChecked(
      checked.includes(item) // If item is already checked, uncheck it
        ? checked.filter(i => i !== item)
        : [...checked, item] // If item is unchecked, add it to the checked array
    );
    console.log(checked); // Log checked items
  };

  return (
    <>
      {/* Task List Section */}
      <div className="Task-list">
        <h2>Task List</h2>
        <ul>
          {/* Map over tasks and render them as list items */}
          {tasks.map(task => (
            <li
              key={task.id}
              style={{ textDecoration: task.done ? "line-through" : "none" }} // Line-through for completed tasks
            >
              {task.text}
              <button onClick={() => completeTask(task.id)}>Complete</button>
            </li>
          ))}
        </ul>
      </div>

      {/* Add Employee Section */}
      <div className="add-employee">
        <h2>Add Employee</h2>
        <input
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)} // Update name state on input change
        />
        <input
          placeholder="Role"
          value={role}
          onChange={(e) => setRole(e.target.value)} // Update role state on input change
        />
        <button onClick={addEmployee}>Add Employee</button>

        {/* Display employee list */}
        <ul>
          {employees.map(emp => (
            <li key={emp.id}>{emp.name} - {emp.role}</li>
          ))}
        </ul>
      </div>

      {/* Employee Manager Section */}
      <div className="employee-manager">
        <h2>Employee Manager</h2>
        {employees.length === 0 && <p>No employees yet.</p>} {/* Display if there are no employees */}
        <ul>
          {/* Display each employee with a remove button */}
          {employees.map(emp => (
            <li key={emp.id}>
              {emp.name} - {emp.role}
              <button onClick={() => removeEmployee(emp.id)}>Remove</button>
            </li>
          ))}
        </ul>
      </div>

      {/* Shopping List Section */}
      <div className="shopping-list">
        <h2>Shopping List</h2>
        {/* Map over shopping list items and create a checkbox for each */}
        {items.map(item => (
          <label key={item} style={{ display: "block", margin: "5px 0" }}>
            <input
              type="checkbox"
              checked={checked.includes(item)} // Check if the item is in the 'checked' list
              onChange={() => toggleCheck(item)} // Toggle the check/uncheck state
            />
            {item}
          </label>
        ))}
        <p>Checked items: {checked.length}</p> {/* Display number of checked items */}
      </div>
    </>
  );
}

export default Array; // Export the component for use in other parts of the app
