import { useState } from "react";

export default function TaskForm({ onSubmit }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [assignedTo, setAssignedTo] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ title, description, assigned_to: Number(assignedTo) });
    setTitle("");
    setDescription("");
    setAssignedTo("");
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <h2>Create Task</h2>
      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        placeholder="Assign to employee_id"
        value={assignedTo}
        onChange={(e) => setAssignedTo(e.target.value)}
      />
      <button type="submit">Create</button>
    </form>
  );
}
