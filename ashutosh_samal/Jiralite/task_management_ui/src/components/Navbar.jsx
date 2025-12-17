import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import RoleSwitch from "./RoleSwitch";

export default function Navbar() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();          // ✅ clears context + storage
    navigate("/");     // ✅ clean redirect
  };

  return (
    <div className="h-14 bg-gray-900 text-white flex items-center justify-between px-6 shadow">
      {/* Left */}
      <div className="text-lg font-semibold tracking-wide">
        Task Management
      </div>

      {/* Right */}
      <div className="flex items-center gap-4">
        {/* Role Switch */}
        <RoleSwitch />

        {/* Logout */}
        <button
          onClick={handleLogout}
          className="bg-red-600 hover:bg-red-700 px-4 py-1.5 rounded text-sm font-medium"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
