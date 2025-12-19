export default function EmployeeTable({ employees, onDelete }) {
  return (
    <table className="w-full border">
      <thead>
        <tr className="bg-gray-200">
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Designation</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {employees.map(emp => (
          <tr key={emp.emp_id}>
            <td>{emp.emp_id}</td>
            <td>{emp.name}</td>
            <td>{emp.email}</td>
            <td>{emp.designation}</td>
            <td>
              <button
                className="text-red-500"
                onClick={() => onDelete(emp.emp_id)}
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
