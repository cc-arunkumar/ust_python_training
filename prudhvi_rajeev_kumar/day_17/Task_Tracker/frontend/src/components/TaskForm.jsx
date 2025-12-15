import { useState } from "react";
import { TextField, Button, Box, Snackbar, Alert } from "@mui/material";
import API from "../api/axios";

export default function TaskForm({ onTaskCreated }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [open, setOpen] = useState(false);

  const handleSubmit = async () => {
    await API.post("/tasks", { title, description });
    setTitle("");
    setDescription("");
    setOpen(true);
    onTaskCreated(); // trigger refresh in TaskList
  };

  return (
    <Box sx={{ mb: 3 }}>
      <TextField
        label="Title"
        fullWidth
        margin="normal"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <TextField
        label="Description"
        fullWidth
        margin="normal"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <Button variant="contained" onClick={handleSubmit}>
        Add Task
      </Button>

      {/* Snackbar for success message */}
      <Snackbar
        open={open}
        autoHideDuration={3000}
        onClose={() => setOpen(false)}
        anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
      >
        <Alert severity="success" sx={{ width: "100%" }}>
          Task added successfully
        </Alert>
      </Snackbar>
    </Box>
  );
}
