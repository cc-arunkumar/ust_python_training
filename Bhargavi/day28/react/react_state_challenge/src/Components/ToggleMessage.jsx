import React, { useState } from "react";

function TaskListToggle() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Task 1", completed: false },
    { id: 2, text: "Task 2", completed: false },
    { id: 3, text: "Task 3", completed: false },
  ]);

  const toggleCompletion = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <div className="box">
      {tasks.map((task) => (
        <div key={task.id} className={task.completed ? "completed" : ""}>
          <p>{task.text}</p>
          <button onClick={() => toggleCompletion(task.id)}>
            {task.completed ? "Undo" : "Complete"}
          </button>
        </div>
      ))}
    </div>
  );
}

export default TaskListToggle;
