import { useState } from "react";

export default function EmployeeManager() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  const addEmployee = () => {
    if (name && role) {
      setEmployees([...employees, { id: Date.now(), name, role }]);
      setName("");
      setRole("");
    }
  };

  const removeEmployee = (id) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  return (
    <div >
      <h3>Employee Manager</h3>
      <input placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
      <input placeholder="Role" value={role} onChange={(e) => setRole(e.target.value)} />
      <button onClick={addEmployee}>Add Employee</button>
      <ul>
        {employees.map(emp => (
          <li key={emp.id}>
            {emp.name} - {emp.role} <button onClick={() => removeEmployee(emp.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
