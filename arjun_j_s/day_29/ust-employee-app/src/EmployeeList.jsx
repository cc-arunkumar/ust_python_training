import api from "./api/api";
 
function EmployeeList({ employees, onDelete, onEdit }) {
  const handleDelete = (id) => {
    api.delete(`/employees/${id}`).then(() => {
      onDelete(id);
    });
  };
 
  return (
    <div>
      <h3>Employee List</h3>
 
      {employees.length === 0 && <p>No employees found</p>}
 
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Name</th>
            <th>Designation</th>
            <th>Location</th>
            <th>Project</th>
            <th>Actions</th>
          </tr>
        </thead>
 
        <tbody>
          {employees.map((emp) => (
            <tr key={emp.id}>
              <td>{emp.name}</td>
              <td>{emp.designation}</td>
              <td>{emp.location}</td>
              <td>{emp.project}</td>
              <td>
                <button onClick={() => onEdit(emp)}>Edit</button>
                <button onClick={() => handleDelete(emp.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
 
export default EmployeeList;
 
 