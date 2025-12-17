import { useState } from "react";
import api from "../api/api";

function DeleteEmployee() {
  const [id, setId] = useState("");
  const [message, setMessage] = useState("");

  const handleDelete = () => {
    api
      .delete(`/employees/${id}`)
      .then(() => setMessage("Employee deleted successfully"))
      .catch(() => setMessage("Error deleting employee"));
  };

  return (
    <div>
      <h2>Delete Employee</h2>
      <input
        type="number"
        placeholder="Employee ID"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <button onClick={handleDelete}>Delete</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default DeleteEmployee;
