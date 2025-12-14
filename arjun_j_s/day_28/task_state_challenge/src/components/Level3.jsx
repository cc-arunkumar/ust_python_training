import React, { useState } from "react";

const Level3 = () => {
  const initialTasks = [
    { id: 1, text: "Task 1", completed: true },
    { id: 2, text: "Task 2", completed: true },
    { id: 3, text: "Task 3", completed: true },
  ];

  const [tasks, setTasks] = useState(initialTasks);
  const [emp_name, setEmpName] = useState("");  
  const [emp_role, setEmpRole] = useState(""); 
  const [dlt_name, setDltName] = useState("");  
  const [employees, setEmp] = useState([]);

  const handleTasks = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const handleEmployee = () => {
    setEmp([
      ...employees, { Name: emp_name, Role: emp_role }
    ]);

    // Reset input fields after adding employee
    setEmpName("");
    setEmpRole("");
  };

  const handleDeleteEmployee = () => {
    // Remove employee from list
    setEmp(employees.filter(emp => emp.Name !== dlt_name));

    // Reset input field for name
    setDltName("");
  };
   const items = [
    { id: 1, text: "Item 1" },
    { id: 2, text: "Item 2" },
    { id: 3, text: "Item 3" },
    { id: 4, text: "Item 4" },
    { id: 5, text: "Item 5" },
  ];
  const [checkedItems, setCheckedItems] = useState([]);


  const handleCheckboxChange = (id) => {
    setCheckedItems((prevCheckedItems) => {
      if (prevCheckedItems.includes(id)) {
        return prevCheckedItems.filter((item) => item !== id);
      } else {
        return [...prevCheckedItems, id];
      }
    });
  };

  return (
    <>
      <div>
        <h2>Task List</h2>
        <ul>
          {tasks.map((task) => (
            <li
              key={task.id}
              style={{
                textDecoration: task.completed ? "none" : "line-through",
              }}
            >
              {task.text}
              <button onClick={() => handleTasks(task.id)}>Complete</button>
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h2>Add Employee</h2>
        <input 
          type="text" 
          value={emp_name}
          onChange={(e) => setEmpName(e.target.value)}
          placeholder="Enter name...."
        />
        <input 
          type="text" 
          value={emp_role}
          onChange={(e) => setEmpRole(e.target.value)}
          placeholder="Enter role...."
        />
        <button onClick={handleEmployee}>
          Add Employee
        </button>
        
        <h3>Employee List</h3>
        <ul>
          {employees.map((emp, index) => (
            <li key={index}>
              Name : {emp.Name} | Role: {emp.Role}
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h2>Delete Employee</h2>
        <input 
          type="text" 
          value={dlt_name}
          onChange={(e) => setDltName(e.target.value)}
          placeholder="Enter name...."
        />
        <button onClick={handleDeleteEmployee}>
          Delete Employee
        </button>
      </div>

      <div>
        <h2>Checkbox List</h2>
        <ul>
          {items.map((item) => (
            <li key={item.id}>
              <input
                type="checkbox"
                checked={checkedItems.includes(item.id)}
                onChange={() => handleCheckboxChange(item.id)}
              />
              {item.text}
            </li>
          ))}
        </ul>
        <p>Checked Items Count: {checkedItems.length}</p> 
      </div>
    </>
  );
};

export default Level3;
