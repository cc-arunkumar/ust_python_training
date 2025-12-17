import { Link } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";

export default function Sidebar() {
  const { user } = useContext(AuthContext);

  return (
    <div className="sidebar">
      <Link to="/dashboard">Dashboard</Link>
      <Link to="/tasks">Tasks</Link>
      {user?.role === "manager" && <Link to="/manage">Manage</Link>}
      {user?.role === "admin" && <Link to="/admin">Admin</Link>}
    </div>
  );
}
