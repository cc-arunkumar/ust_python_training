import { useAuth } from "../auth/AuthContext";

const Navbar = () => {
  const { user, logout } = useAuth();

  if (!user) return null;

  const roles = Array.isArray(user.roles) ? user.roles : [];

  return (
    <header className="flex justify-between items-center bg-white shadow px-6 py-4">
      <h1 className="text-xl font-semibold">
        Welcome, {roles.join(", ") || "User"}
      </h1>

      <button
        onClick={logout}
        className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
      >
        Logout
      </button>
    </header>
  );
};

export default Navbar;
