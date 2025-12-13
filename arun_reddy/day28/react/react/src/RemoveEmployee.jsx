import { useState } from "react";

export default function RemoveEmployee() {
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

  const removeEmployee = (id) => {
    setEmployees(employees.filter((emp) => emp.id !== id));
  };

  return (
    <div className="remove-employee-container">
      <div className="remove-employee-card">
        <h2 className="remove-employee-title">Employee Manager</h2>

        <div className="remove-employee-form">
          <input
            type="text"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="remove-employee-input"
          />
          <input
            type="text"
            placeholder="Role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="remove-employee-input"
          />
          <button onClick={addEmployee} className="remove-employee-btn-add">
            Add Employee
          </button>
        </div>

        <ul className="remove-employee-list">
          {employees.map((emp) => (
            <li key={emp.id} className="remove-employee-item">
              <div>
                <div className="remove-employee-name">{emp.name}</div>
                <div className="remove-employee-role">{emp.role}</div>
              </div>
              <button
                onClick={() => removeEmployee(emp.id)}
                className="remove-employee-btn"
              >
                Remove
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
