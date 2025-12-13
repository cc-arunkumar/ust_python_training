import { useState } from "react";
import "./App.css";

function App() {
  const [name, setName] = useState("");
  const [role, setRole] = useState("");
  const [employees, setEmployees] = useState([]);

  const addEmployee = () => {
    if (name.trim() === "" || role.trim() === "") {
      alert("Please enter both name and role!");
      return;
    }
    const newEmployee = { id: Date.now(), name, role };
    setEmployees([...employees, newEmployee]);
    setName("");
    setRole("");
  };

  const removeEmployee = (id) => {
    setEmployees(employees.filter((emp) => emp.id !== id));
  };

  return (
    <div className="App">
      <h1>Employee Manager</h1>

      {/* Input fields */}
      <input
        type="text"
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="input-box"
      />
      <input
        type="text"
        placeholder="Enter role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
        className="input-box"
      />

      {/* Add button */}
      <button onClick={addEmployee}>Add Employee</button>

      {/* Employee list */}
      <ul>
        {employees.map((emp) => (
          <li key={emp.id}>
            <strong>{emp.name}</strong> — {emp.role}
            <button
              className="remove-btn"
              onClick={() => removeEmployee(emp.id)}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
