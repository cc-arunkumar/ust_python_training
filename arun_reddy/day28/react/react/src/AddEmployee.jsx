import { useState } from "react";

export default function AddEmployee() {
  const [name, setName] = useState("");
  const [role, setRole] = useState("");
  const [employees, setEmployees] = useState([]);

  const addEmployee = () => {
    if (name.trim() && role.trim()) {
      setEmployees([...employees, { id: Date.now(), name, role }]);
      setName("");
      setRole("");
    }
  };

  return (
    <div className="add-employee-container">
      <div className="add-employee-card">
        <h2 className="add-employee-title">Employee Manager</h2>

        <div className="add-employee-form">
          <input
            type="text"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="add-employee-input"
          />
          <input
            type="text"
            placeholder="Role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="add-employee-input"
          />
          <button onClick={addEmployee} className="add-employee-btn">
            Add Employee
          </button>
        </div>

        <ul className="employee-list">
          {employees.map((emp) => (
            <li key={emp.id} className="employee-item">
              <div>
                <div className="employee-name">{emp.name}</div>
                <div className="employee-role">{emp.role}</div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
