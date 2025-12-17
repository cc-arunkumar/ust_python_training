import { useEffect, useState } from "react";
import api from "./api/api";
import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";

function App() {
  const [employees, setEmployees] = useState([]);

  //READ ALL (GET)
  const fetchEmployees = () => {
    api.get("/employees")
      .then((res) => setEmployees(res.data))
      .catch((err) => console.error("Fetch error", err));
  };

  //CREATE (POST)
  const handleEmployeeAdded = (newEmployee) => {
    setEmployees([...employees, newEmployee]);
  };

  //DELETE (DELETE)
  const handleDelete = (id) => {
    api.delete(`/employees/${id}`)
      .then(() => {
        setEmployees(employees.filter((emp) => emp.id !== id));
      })
      .catch((err) => console.error("Delete error", err));
  };

  //UPDATE (PUT)
  const handleUpdate = (id, updatedEmployee) => {
    api.put(`/employees/${id}`, updatedEmployee)
      .then((res) => {
        setEmployees(
          employees.map((emp) =>
            emp.id === id ? res.data : emp
          )
        );
      })
      .catch((err) => console.error("Update error", err));
  };

  //Load employees on page load
  useEffect(() => {
    fetchEmployees();
  }, []);

  return (
    <div>
      <h2>Employee Management</h2>

      <EmployeeForm onEmployeeAdded={handleEmployeeAdded} />

      <EmployeeList
        employees={employees}
        onDelete={handleDelete}
        onUpdate={handleUpdate}
      />
    </div>
  );
}

export default App;




