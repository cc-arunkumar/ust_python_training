import { useState } from "react";

import EmployeeForm from "./components/EmployeeForm";
import GetEmployee from "./components/GetEmployee";
import UpdateEmployee from "./components/UpdateEmployee";
import DeleteEmployee from "./components/DeleteEmployee";

function App() {
  const [employees, setEmployees] = useState([]);

  const handleEmployeeAdded = (newEmployee) => {
    setEmployees([...employees, newEmployee]);
  };

  return (
    <div>
      <h2>Employee Management</h2>

      {/* Create */}
      <EmployeeForm onEmployeeAdded={handleEmployeeAdded} />

      <hr />

      {/* Read */}
      <GetEmployee />

      <hr />

      {/* Update */}
      <UpdateEmployee />

      <hr />

      {/* Delete */}
      <DeleteEmployee />
    </div>
  );
}

export default App;
