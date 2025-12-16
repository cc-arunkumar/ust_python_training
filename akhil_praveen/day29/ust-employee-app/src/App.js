import EmployeeForm from "./components/EmployeeForm";
import { useState } from "react";

function App() {
  const [employees, setEmployees] = useState([]);

  const handleEmployeeAdded = (newEmployee) => {
    setEmployees([...employees, newEmployee]);
  };

  return (
    <div>
      <EmployeeForm onEmployeeAdded={handleEmployeeAdded} />
      {employees}
    </div>
  );
}

export default App;