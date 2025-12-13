import React, { useState } from "react";
import "./ObjectState.css";

function ObjectState() {

  const [tasks, setTasks] = useState([
    { id: 1, text: "Learn React", completed: false },
    { id: 2, text: "Practice JavaScript", completed: false },
    { id: 3, text: "Build Projects", completed: false },
  ]);

  const toggleTask = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };


  const [employees, setEmployees] = useState([]);
  const [empName, setEmpName] = useState("");
  const [empRole, setEmpRole] = useState("");

  const addEmployee = () => {
    if (empName.trim() === "" || empRole.trim() === "") return;

    const newEmployee = {
      id: Date.now(),
      name: empName,
      role: empRole,
    };

    setEmployees([...employees, newEmployee]);
    setEmpName("");
    setEmpRole("");
  };

  const removeEmployee = (id) => {
    setEmployees(employees.filter((emp) => emp.id !== id));
  };

  const items = ["Apple", "Banana", "Mango", "Orange", "Grapes"];
  const [checkedItems, setCheckedItems] = useState([]);

  const toggleCheck = (item) => {
    if (checkedItems.includes(item)) {
      setCheckedItems(checkedItems.filter((i) => i !== item));
    } else {
      setCheckedItems([...checkedItems, item]);
    }
  };

  return (
    <div className="container">

      {/* Task List Toggle */}
      <div className="card">
        <h2 className="title">Task List Toggle</h2>
        {tasks.map((task) => (
          <div key={task.id} className="task-row">
            <span
              className={task.completed ? "completed paragraph" : "paragraph"}
            >
              {task.text}
            </span>
            <button className="btn" onClick={() => toggleTask(task.id)}>
              {task.completed ? "Undo" : "Complete"}
            </button>
          </div>
        ))}
      </div>

      {/* Add + Remove Employee */}
      <div className="card">
        <h2 className="title">Add / Remove Employee</h2>

        <input
          className="input-box"
          type="text"
          placeholder="Employee Name"
          value={empName}
          onChange={(e) => setEmpName(e.target.value)}
        />

        <input
          className="input-box"
          type="text"
          placeholder="Role"
          value={empRole}
          onChange={(e) => setEmpRole(e.target.value)}
        />

        <button className="btn add-btn" onClick={addEmployee}>
          Add Employee
        </button>

        <ul className="employee-list">
          {employees.map((emp) => (
            <li key={emp.id} className="employee-item paragraph">
              {emp.name} — {emp.role}
              <button
                className="btn remove-btn"
                onClick={() => removeEmployee(emp.id)}
              >
                Remove
              </button>
            </li>
          ))}
        </ul>
      </div>

      {/* Checkbox List */}
      <div className="card">
        <h2 className="title">Checkbox List</h2>

        {items.map((item) => (
          <div key={item} className="checkbox-row paragraph">
            <input
              type="checkbox"
              checked={checkedItems.includes(item)}
              onChange={() => toggleCheck(item)}
            />
            <label>{item}</label>
          </div>
        ))}

        <p className="count-text">
          Checked Items: {checkedItems.length}
        </p>
      </div>

    </div>
  );
}

export default ObjectState;
