import { useState } from "react";
import { switchRole as switchRoleAPI } from "../api/auth.api";
import { useAuth } from "../context/AuthContext";

export default function RoleSwitch() {
  const { switchRole } = useAuth();
  const [loading, setLoading] = useState(false);

  const roles = ["DEVELOPER", "MANAGER", "ADMIN"];

  const handleSwitch = async (role) => {
    if (!role) return;

    try {
      setLoading(true);
      const res = await switchRoleAPI(role);
      localStorage.setItem("token", res.data.access_token);

      // ✅ Update React state (NO reload)
      switchRole(role);
    } catch {
      alert("You do not have this role");
    } finally {
      setLoading(false);
    }
  };

  return (
    <select
      onChange={(e) => handleSwitch(e.target.value)}
      disabled={loading}
      defaultValue=""
      className="bg-gray-800 text-white border border-gray-600 rounded px-3 py-1.5 text-sm"
    >
      <option value="" disabled>
        Switch Role
      </option>

      {roles.map((r) => (
        <option key={r} value={r}>
          {r}
        </option>
      ))}
    </select>
  );
}
