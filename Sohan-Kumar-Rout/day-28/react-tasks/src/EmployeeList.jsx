import { useState } from "react";

export default function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  const removeEmployee = (id) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  return (
    <div>
      <h3>Employees</h3>
      {employees.map(emp => (
        <div key={emp.id}>
          {emp.name} — {emp.role}
          <button onClick={() => removeEmployee(emp.id)}>Remove</button>
        </div>
      ))}
    </div>
  );
}
