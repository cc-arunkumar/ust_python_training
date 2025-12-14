import { useState } from "react";

export default function AddEmployee() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  const addEmployee = () => {
    if (!name || !role) return;
    setEmployees([...employees, { id: Date.now(), name, role }]);
    setName("");
    setRole("");
  };

  return (
    <div>
      <input 
        placeholder="Name" 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
      />
      <input 
        placeholder="Role" 
        value={role} 
        onChange={(e) => setRole(e.target.value)} 
      />
      <button onClick={addEmployee}>Add Employee</button>

      <ul>
        {employees.map(emp => (
          <li key={emp.id}>{emp.name} — {emp.role}</li>
        ))}
      </ul>
    </div>
  );
}
