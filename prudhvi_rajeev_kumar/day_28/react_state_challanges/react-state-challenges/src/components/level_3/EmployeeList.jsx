import { useState } from "react";

export default function EmployeeList() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  const addEmployee = () => {
    if (!name.trim() || !role.trim()) return;
    setEmployees(es => [...es, { id: crypto.randomUUID(), name, role }]);
    setName("");
    setRole("");
  };

  return (
    <section className="card">
      <h3>Add Employee</h3>
      <div className="row">
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
        <input value={role} onChange={(e) => setRole(e.target.value)} placeholder="Role" />
        <button onClick={addEmployee}>Add Employee</button>
      </div>

      <ul>
        {employees.map(emp => (
          <li key={emp.id}>{emp.name} — {emp.role}</li>
        ))}
      </ul>
    </section>
  );
}
