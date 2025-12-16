import React, { useEffect, useState } from "react";
import { createTask, updateTask } from "../services/taskService";

const CreateTask = ({ selectedTask, onSuccess }) => {
  const [task, setTask] = useState({
    title: "",
    description: "",
    assignedTo: "",
    assignedBy: "Admin",
    assignedAt: new Date().toISOString().slice(0, 16),
    updatedBy: "",
    updatedAt: "",
    priority: "",
    status: "",
    remark: "",
    review: "",
  });

  useEffect(() => {
    if (selectedTask) {
      setTask(selectedTask);
    }
  }, [selectedTask]);

  const handleChange = (e) => {
    setTask({ ...task, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (selectedTask) {
      await updateTask(selectedTask.task_id, task);
      alert("Task updated successfully");
    } else {
      await createTask(task);
      alert("Task created successfully");
    }

    onSuccess();
    setTask({
      title: "",
      description: "",
      assignedTo: "",
      assignedBy: "Admin",
      assignedAt: new Date().toISOString().slice(0, 16),
      updatedBy: "",
      updatedAt: "",
      priority: "",
      status: "",
      remark: "",
      review: "",
    });
  };

  return (
    <div className="bg-[#1F2635] p-6 rounded-xl shadow-lg text-white max-w-2xl">
      <h2 className="text-2xl font-bold mb-6 text-blue-400">
        {selectedTask ? "Update Task" : "Create Task"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Title */}
        <div>
          <label className="block mb-1 text-sm font-medium">Title</label>
          <input
            type="text"
            name="title"
            value={task.title}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
            onChange={handleChange}
          />
        </div>

        {/* Description */}
        <div>
          <label className="block mb-1 text-sm font-medium">Description</label>
          <textarea
            name="description"
            rows="3"
            value={task.description}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
            onChange={handleChange}
          />
        </div>

        {/* Assigned To */}
        <div>
          <label className="block mb-1 text-sm font-medium">Assigned To</label>
          <input
            type="text"
            name="assignedTo"
            value={task.assignedTo}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
            onChange={handleChange}
          />
        </div>

        {/* Priority */}
        <div>
          <label className="block mb-1 text-sm font-medium">Priority</label>
          <select
            name="priority"
            value={task.priority}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
            onChange={handleChange}
          >
            <option value="">Select Priority</option>
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
          </select>
        </div>

        {/* Status */}
        <div>
          <label className="block mb-1 text-sm font-medium">Status</label>
          <select
            name="status"
            value={task.status}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
            onChange={handleChange}
          >
            <option value="">Select Status</option>
            <option value="Pending">Pending</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
          </select>
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 py-3 rounded-lg font-semibold hover:bg-blue-700"
        >
          {selectedTask ? "Update Task" : "Create Task"}
        </button>
      </form>
    </div>
  );
};

export default CreateTask;
