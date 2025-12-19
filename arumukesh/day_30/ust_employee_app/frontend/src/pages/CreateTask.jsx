import { useState } from "react";
import { createTask } from "../api/taskApi";

const CreateTask = () => {
  const [title, setTitle] = useState("");
  const [description, setDesc] = useState("");
  const [assignedTo, setAssignedTo] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    await createTask({
      title,
      description,
      assigned_to: Number(assignedTo),
    });
    alert("Task created");
  };

  return (
    <form onSubmit={submit} className="p-6 max-w-md space-y-3">
      <h2 className="text-xl font-bold">Create Task</h2>

      <input
        className="border p-2 w-full"
        placeholder="Title"
        onChange={(e) => setTitle(e.target.value)}
      />

      <textarea
        className="border p-2 w-full"
        placeholder="Description"
        onChange={(e) => setDesc(e.target.value)}
      />

      <input
        className="border p-2 w-full"
        placeholder="Assign To (Emp ID)"
        onChange={(e) => setAssignedTo(e.target.value)}
      />

      <button className="bg-blue-600 text-white px-4 py-2 rounded">
        Create
      </button>
    </form>
  );
};

export default CreateTask;
