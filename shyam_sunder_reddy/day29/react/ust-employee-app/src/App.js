import { useState } from "react";
import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";

function App() {
  const [employees, setEmployees] = useState([]);

  const handleEmployeeAdded = (newEmployee) => {
    setEmployees([...employees, newEmployee]);
  };

  const handleEmployeeUpdated = (updatedEmployee) => {
    setEmployees(
      employees.map((emp) => (emp.id === updatedEmployee.id ? updatedEmployee : emp))
    );
  };

  const handleEmployeeDeleted = (id) => {
    setEmployees(employees.filter((emp) => emp.id !== id));
  };

  return (
    <div>
      <h2>Employee Management</h2>
      <EmployeeForm onEmployeeAdded={handleEmployeeAdded} />
      <EmployeeList
        onEmployeeUpdated={handleEmployeeUpdated}
        onEmployeeDeleted={handleEmployeeDeleted}
      />
    </div>
  );
}

export default App;
