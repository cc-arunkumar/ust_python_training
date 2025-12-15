import { useState } from "react";
import API from "../api";

export default function TaskForm({ refreshTasks }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title.trim()) {
      setError("Task title is required");
      return;
    }

    try {
      await API.post("/tasks", { title, description, completed: false });
      setTitle("");
      setDescription("");
      setError("");
      refreshTasks();
    } catch {
      setError("Failed to add task. Please try again.");
    }
  };

  return (
    <>
      <div className="taskform-container">
        {/* Right side form */}
        <div className="taskform-right">
          <form onSubmit={handleSubmit} className="task-form">
            <h2>Add a New Task</h2>
            <p className="form-subtitle">
              Fill in the details below to add your task
            </p>

            {error && <p className="form-error">{error}</p>}

            <div className="form-group">
              <label htmlFor="title" className="form-label">
                Title
              </label>
              <input
                id="title"
                className="input-field"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Enter task title"
              />
            </div>

            <div className="form-group">
              <label htmlFor="description" className="form-label">
                Description
              </label>
              <textarea
                id="description"
                className="input-field textarea-field"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Enter task details"
                rows={3}
              />
            </div>

            <button type="submit" className="btn-primary">
              Add Task
            </button>
          </form>
        </div>
      </div>
    </>
  );
}
