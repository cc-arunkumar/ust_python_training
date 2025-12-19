import { useAuth } from "../../context/AuthContext";
import { Bell, Search } from "lucide-react";

function Navbar() {
  const { user } = useAuth();

  return (
    <div className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shadow-sm z-10">
      {/* Left: Title or Search */}
      <div className="flex items-center gap-4">
        <h2 className="text-xl font-bold text-gray-800 hidden md:block">
          Overview
        </h2>
        <div className="relative hidden md:block">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={16} />
          <input 
            type="text" 
            placeholder="Search..." 
            className="pl-10 pr-4 py-2 bg-gray-50 border border-gray-200 rounded-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 w-64 transition-all"
          />
        </div>
      </div>

      {/* Right: Notifications & Profile */}
      <div className="flex items-center gap-6">
        <button className="relative p-2 text-gray-500 hover:bg-gray-100 rounded-full transition-colors">
          <Bell size={20} />
          <span className="absolute top-1 right-1 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white"></span>
        </button>
        
        <div className="flex items-center gap-3 border-l pl-6 border-gray-200">
          <div className="text-right hidden sm:block">
            <p className="text-sm font-semibold text-gray-700">Employee #{user?.emp_id}</p>
            <p className="text-xs text-blue-600 font-medium capitalize">{user?.role}</p>
          </div>
          <div className="h-10 w-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold border border-blue-200">
             {user?.role?.charAt(0).toUpperCase()}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Navbar;