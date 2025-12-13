import { useState } from "react";
function EmployeeList() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [role, setRole] = useState("");

  const addEmployee = () => {
    setEmployees([...employees, { id: Date.now(), name, role }]);
    setName("");
    setRole("");
  };

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <input value={role} onChange={(e) => setRole(e.target.value)} placeholder="Role" />
      <button onClick={addEmployee}>Add Employee</button>

      <ul>
        {employees.map(emp => (
          <li key={emp.id}>{emp.name} - {emp.role}</li>
        ))}
      </ul>
    </div>
  );
}

export default EmployeeList