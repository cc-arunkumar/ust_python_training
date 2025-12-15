import React, { useState } from "react";

export default function TaskForm({ onCreate, loading }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const submit = () => {
    if (!title.trim() || !description.trim()) return;
    onCreate(title.trim(), description.trim());
    setTitle("");
    setDescription("");
  };

  return (
    <div className="section glass-section">
      <h2>Create task</h2>
      <div className="form-row">
        <input
          className="input"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          className="input"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <button className="btn primary" onClick={submit} disabled={loading}>
          Add
        </button>
      </div>
    </div>
  );
}
