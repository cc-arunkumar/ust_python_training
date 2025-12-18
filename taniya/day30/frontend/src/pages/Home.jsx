import { useState } from "react";

function Home({ setIsLoggedIn }) {
  const [role, setRole] = useState(localStorage.getItem("role"));

  const switchRole = () => {
    const newRole = role === "MANAGER" ? "EMPLOYEE" : "MANAGER";
    setRole(newRole);
    localStorage.setItem("role", newRole);
  };

  const logout = () => {
    localStorage.clear();
    setIsLoggedIn(false);
  };

  return (
    <div style={{ padding: "40px" }}>
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <h2>Home</h2>
        <div>👤</div>
      </div>

      <p>
        Logged in as: <strong>{role}</strong>
      </p>

      {role === "MANAGER" && (
        <button onClick={switchRole}>
          Switch Role
        </button>
      )}

      <br /><br />

      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default Home;
