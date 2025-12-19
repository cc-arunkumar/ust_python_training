import React from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'
import { LogOut, User, Menu } from 'lucide-react'
import { toast } from 'react-toastify'

const Navbar = ({ onMenuClick }) => {
  const { user, logout } = useAuth()

  const handleLogout = () => {
    logout()
    toast.success('Logged out successfully')
  }

  return (
    <nav className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-40">
      <div className="px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <button
              onClick={onMenuClick}
              className="lg:hidden p-2 rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 focus:outline-none"
            >
              <Menu className="w-6 h-6" />
            </button>
            <Link to="/dashboard" className="flex items-center">
              <span className="text-2xl font-bold text-primary-600">TaskFlow</span>
            </Link>
          </div>

          <div className="flex items-center gap-4">
            <div className="hidden sm:block text-right">
              <p className="text-sm font-medium text-gray-900">Employee #{user?.emp_id}</p>
              <p className="text-xs text-gray-500 capitalize">
                {user?.roles?.join(', ') || 'User'}
              </p>
            </div>

            <div className="flex items-center gap-2">
              <Link
                to="/profile"
                className="p-2 rounded-full text-gray-600 hover:text-gray-900 hover:bg-gray-100 focus:outline-none"
              >
                <User className="w-5 h-5" />
              </Link>
              <button
                onClick={handleLogout}
                className="p-2 rounded-full text-gray-600 hover:text-red-600 hover:bg-red-50 focus:outline-none"
                title="Logout"
              >
                <LogOut className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar