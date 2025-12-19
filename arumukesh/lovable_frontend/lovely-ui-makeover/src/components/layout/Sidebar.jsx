import React from 'react'
import { NavLink } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'
import { 
  LayoutDashboard, 
  ListTodo, 
  PlusCircle, 
  Users, 
  UserCog,
  X 
} from 'lucide-react'

const Sidebar = ({ isOpen, onClose }) => {
  const { user, isAdmin, isManager } = useAuth()

  const navItems = [
    {
      name: 'Dashboard',
      path: '/dashboard',
      icon: LayoutDashboard,
      roles: ['admin', 'manager', 'developer'],
    },
    {
      name: 'Tasks',
      path: '/tasks',
      icon: ListTodo,
      roles: ['admin', 'manager', 'developer'],
    },
    {
      name: 'Create Task',
      path: '/tasks/create',
      icon: PlusCircle,
      roles: ['admin', 'manager'],
    },
    {
      name: 'Users',
      path: '/users',
      icon: UserCog,
      roles: ['admin'],
    },
    {
      name: 'Employees',
      path: '/employees',
      icon: Users,
      roles: ['admin'],
    },
  ]

  const filteredNavItems = navItems.filter(item => {
    return item.roles.some(role => user?.roles?.map(r => r.toLowerCase()).includes(role))
  })

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-gray-600 bg-opacity-75 z-40 lg:hidden"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`
          fixed lg:static inset-y-0 left-0 z-50
          w-64 bg-white border-r border-gray-200
          transform transition-transform duration-300 ease-in-out
          ${isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'}
        `}
      >
        <div className="flex items-center justify-between h-16 px-4 border-b border-gray-200 lg:hidden">
          <span className="text-xl font-bold text-primary-600">Menu</span>
          <button
            onClick={onClose}
            className="p-2 rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        <nav className="p-4 space-y-2">
          {filteredNavItems.map((item) => {
            const Icon = item.icon
            return (
              <NavLink
                key={item.path}
                to={item.path}
                onClick={() => onClose()}
                className={({ isActive }) =>
                  `flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                    isActive
                      ? 'bg-primary-50 text-primary-700 font-medium'
                      : 'text-gray-700 hover:bg-gray-100'
                  }`
                }
              >
                <Icon className="w-5 h-5" />
                <span>{item.name}</span>
              </NavLink>
            )
          })}
        </nav>

        <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-200">
          <div className="text-xs text-gray-500 text-center">
            <p>Logged in as</p>
            <p className="font-medium text-gray-700 mt-1">Employee #{user?.emp_id}</p>
            <p className="text-primary-600 capitalize mt-1">
              {user?.roles?.join(', ') || 'User'}
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}

export default Sidebar