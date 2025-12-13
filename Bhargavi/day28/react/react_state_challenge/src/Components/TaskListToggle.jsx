import React, { useState } from "react";

function TaskList() {
  const [tasks, setTasks] = useState([
    { id: 1, name: "Task 1", completed: false },
    { id: 2, name: "Task 2", completed: false },
    { id: 3, name: "Task 3", completed: false },
  ]);

  const toggleTaskCompletion = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <div>
      {tasks.map((task) => (
        <div key={task.id}>
          <p
            style={{ textDecoration: task.completed ? "line-through" : "none" }}
          >
            {task.name}
          </p>
          <button onClick={() => toggleTaskCompletion(task.id)}>
            {task.completed ? "Undo" : "Complete"}
          </button>
        </div>
      ))}
    </div>
  );
}

export default TaskList;
