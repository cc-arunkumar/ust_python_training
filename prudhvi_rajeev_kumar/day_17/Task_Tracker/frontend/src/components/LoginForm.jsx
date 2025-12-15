import { useState } from "react";
import { TextField, Button, Box, Typography } from "@mui/material";
import API from "../api/axios";
import { useNavigate, Link } from "react-router-dom";

export default function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await API.post("/login", { username, password });
      localStorage.setItem("token", res.data.access_token);
      localStorage.setItem("username", username); // ✅ save username
      navigate("/dashboard");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <Box sx={{ maxWidth: 400, mx: "auto", mt: 10 }}>
      <Typography variant="h5" gutterBottom>Login</Typography>
      <TextField fullWidth label="Username" margin="normal"
        value={username} onChange={(e) => setUsername(e.target.value)} />
      <TextField fullWidth label="Password" type="password" margin="normal"
        value={password} onChange={(e) => setPassword(e.target.value)} />
      <Button fullWidth variant="contained" sx={{ mt: 2 }} onClick={handleLogin}>
        Login
      </Button>
      <Typography sx={{ mt: 2 }}>
        Don’t have an account? <Link to="/register">Register</Link>
      </Typography>
    </Box>
  );
}
