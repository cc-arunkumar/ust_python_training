import { useEffect, useState } from "react";
import {
  List,
  ListItem,
  ListItemText,
  Button,
  Snackbar,
  Alert,
  Typography,
} from "@mui/material";
import API from "../api/axios";

export default function TaskList({ refreshTrigger }) {
  const [tasks, setTasks] = useState([]);
  const [message, setMessage] = useState("");
  const [open, setOpen] = useState(false);

  // Fetch tasks from backend
  const fetchTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data);
  };

  useEffect(() => {
    fetchTasks();
  }, [refreshTrigger]); // auto update when refreshTrigger changes

  const markCompleted = async (task) => {
    await API.put(`/tasks/${task.id}`, {
      ...task,
      completed: true,
    });
    setMessage("Task modified successfully");
    setOpen(true);
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await API.delete(`/tasks/${id}`);
    setMessage("Task deleted successfully");
    setOpen(true);
    fetchTasks();
  };

  return (
    <>
      <Typography variant="h5" gutterBottom sx={{ mb: 2 }}>
        List of Tasks
      </Typography>
      <List>
        {tasks.map((task) => (
          <ListItem
            key={task.id}
            sx={{
              display: "flex",
              flexDirection: "column",
              alignItems: "flex-start",
              mb: 2,
              border: "1px solid #ccc",
              borderRadius: "8px",
              p: 2,
            }}
          >
            <ListItemText
              primary={task.title}
              secondary={task.description}
              sx={{ mb: 1 }}
            />
            <Typography
              variant="body2"
              color={task.completed ? "success.main" : "error.main"}
              sx={{ mb: 1 }}
            >
              {task.completed ? "Completed" : "Pending"}
            </Typography>
            {!task.completed && (
              <Button
                variant="contained"
                color="success"
                onClick={() => markCompleted(task)}
                sx={{ mr: 1 }}
              >
                Mark as Completed
              </Button>
            )}
            <Button
              variant="outlined"
              color="error"
              onClick={() => deleteTask(task.id)}
            >
              Delete
            </Button>
          </ListItem>
        ))}
      </List>

      {/* Snackbar for success messages */}
      <Snackbar
        open={open}
        autoHideDuration={3000}
        onClose={() => setOpen(false)}
        anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
      >
        <Alert severity="success" sx={{ width: "100%" }}>
          {message}
        </Alert>
      </Snackbar>
    </>
  );
}
