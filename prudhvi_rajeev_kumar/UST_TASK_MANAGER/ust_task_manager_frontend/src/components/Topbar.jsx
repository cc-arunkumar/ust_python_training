import { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";

export default function Topbar({ search, setSearch }) {
  const { user, logout } = useContext(AuthContext);

  return (
    <div className="topbar">
      <input
        type="text"
        placeholder="Search tasks..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: "6px",
          borderRadius: "4px",
          border: "1px solid #555",
          background: "#2c2c3c",
          color: "#f5f5f5",
          marginRight: "12px"
        }}
      />
      <span>{user ? `${user.sub} (${user.role})` : "UST Task Manager"}</span>
      {user && <button onClick={logout}>Logout</button>}
    </div>
  );
}
