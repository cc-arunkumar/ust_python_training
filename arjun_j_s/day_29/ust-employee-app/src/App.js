import { useEffect, useState } from "react";
import api from "./api/api";
import EmployeeForm from "./EmployeeForm";
import EmployeeList from "./EmployeeList";
import EditEmployee from "./EditEmployee";
 
function App() {
  const [employees, setEmployees] = useState([]);
  const [editingEmployee, setEditingEmployee] = useState(null);
 
  // READ
  useEffect(() => {
    api.get("/employees").then((res) => {
      setEmployees(res.data);
    });
  }, []);
 
  // CREATE
  const addEmployee = (emp) => {
    setEmployees([...employees, emp]);
  };
 
  // DELETE
  const deleteEmployee = (id) => {
    setEmployees(employees.filter((e) => e.id !== id));
  };
 
  // UPDATE
  const updateEmployee = (updated) => {
    setEmployees(
      employees.map((e) => (e.id === updated.id ? updated : e))
    );
    setEditingEmployee(null);
  };
 
  return (
    <div>
      <h2>Employee Management</h2>
 
      {!editingEmployee ? (
        <EmployeeForm onEmployeeAdded={addEmployee} />
      ) : (
        <EditEmployee
          employee={editingEmployee}
          onUpdated={updateEmployee}
          onCancel={() => setEditingEmployee(null)}
        />
      )}
 
      <EmployeeList
        employees={employees}
        onDelete={deleteEmployee}
        onEdit={setEditingEmployee}
      />
    </div>
  );
}
 
export default App;
 
 