import { useState } from "react";

export default function EmployeeListWithRemove() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  const addEmployee = () => {
    if (!name.trim() || !role.trim()) return;
    setEmployees(es => [...es, { id: crypto.randomUUID(), name, role }]);
    setName("");
    setRole("");
  };

  const removeEmployee = (id) =>
    setEmployees(es => es.filter(e => e.id !== id));

  return (
    <section className="card">
      <h3>Add & Remove Employee</h3>
      <div className="row">
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
        <input value={role} onChange={(e) => setRole(e.target.value)} placeholder="Role" />
        <button onClick={addEmployee}>Add Employee</button>
      </div>

      <ul>
        {employees.map(emp => (
          <li key={emp.id}>
            {emp.name} — {emp.role}
            <button className="danger" onClick={() => removeEmployee(emp.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </section>
  );
}
