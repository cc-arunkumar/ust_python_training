import { useTheme } from "../context/ThemeContext";

export default function Topbar() {
  const { dark, setDark } = useTheme();

  const onLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  return (
    <div className="h-16 bg-white dark:bg-gray-900 shadow flex items-center justify-between px-6">
      {/* App title */}
      <div className="text-lg font-semibold text-gray-800 dark:text-gray-200">
        Jira Lite
      </div>

      {/* Right side controls */}
      <div className="flex items-center space-x-4">
        {/* Dark/Light toggle button */}
        <button
          onClick={() => setDark(!dark)}
          className="px-3 py-1 rounded bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        >
          {dark ? "☀️ Light" : "🌙 Dark"}
        </button>

        {/* Logout button */}
        <button
          onClick={onLogout}
          className="text-sm text-blue-600 dark:text-blue-400 hover:underline"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
