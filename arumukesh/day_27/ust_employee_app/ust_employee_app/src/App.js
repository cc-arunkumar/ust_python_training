import { useState } from "react";
import EmployeeCreate from "./components/CreateEmployee";
import EmployeeRead from "./components/EmployeeList";
import EmployeeUpdate from "./components/UpdateEmployee";

function App() {
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [refresh, setRefresh] = useState(false);

  return (
    <div>
      <h2>Employee Create </h2>
      <EmployeeCreate onSuccess={() => setRefresh(!refresh)} />

      

      <h2>Employee Update </h2>

      <EmployeeUpdate
        employee={selectedEmployee}
        onUpdated={() => {
          setSelectedEmployee(null);
          setRefresh(!refresh);
        }}
      />
      <h2>Employee Read</h2>

      <EmployeeRead key={refresh} onEdit={setSelectedEmployee} />
    </div>
  );
}

export default App;
