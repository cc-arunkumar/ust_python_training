import React, { useEffect, useState } from 'react'
import { fetchTasks } from '../services/api'  // Import fetchTasks API function

function TaskList() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    const getTasks = async () => {
      try {
        const response = await fetchTasks()  // Fetch tasks from the API
        setTasks(response.data)  // Store tasks in state
      } catch (error) {
        alert('Error fetching tasks')
      }
    }

    getTasks()  // Call the function to get tasks
  }, [])

  return (
    <div className="task-list">
      <h2>Your Tasks</h2>
      <ul>
        {tasks.length > 0 ? (
          tasks.map((task) => (
            <li key={task.id}>{task.name}</li>  // Display task name
          ))
        ) : (
          <li>No tasks found</li>
        )}
      </ul>
    </div>
  )
}

export default TaskList
