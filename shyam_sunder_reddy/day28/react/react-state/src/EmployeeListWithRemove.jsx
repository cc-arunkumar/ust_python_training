import { useState } from "react";
function EmployeeListWithRemove() {
  const [employees, setEmployees] = useState([]);

  const removeEmployee = (id) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  return (
    <div>
      {/* Add Employee inputs same as above */}
      <ul>
        {employees.map(emp => (
          <li key={emp.id}>
            {emp.name} - {emp.role}
            <button onClick={() => removeEmployee(emp.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EmployeeListWithRemove