import Navbar from "../components/Navbar";
import TaskForm from "../components/TaskForm";
import TaskList from "../components/TaskList";
import { Container } from "@mui/material";
import { useState } from "react";

export default function Dashboard({ darkMode, setDarkMode }) {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  const handleTaskCreated = () => {
    setRefreshTrigger((prev) => prev + 1); // trigger TaskList refresh
  };

  return (
    <>
      <Navbar darkMode={darkMode} setDarkMode={setDarkMode} />
      <Container sx={{ mt: 3 }}>
        <TaskForm onTaskCreated={handleTaskCreated} />
        <TaskList refreshTrigger={refreshTrigger} />
      </Container>
    </>
  );
}
