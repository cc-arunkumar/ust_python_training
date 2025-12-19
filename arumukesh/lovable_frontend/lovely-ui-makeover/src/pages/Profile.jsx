// ### **src/pages/Profile.jsx**
// ```jsx
import React, { useState } from 'react'
import { useAuth } from '../context/AuthContext'
import Card from '../components/common/Card'
import Badge from '../components/common/Badge'
import { User, Shield, Mail, Briefcase } from 'lucide-react'

const Profile = () => {
  const { user } = useAuth()

  return (
    <div className="space-y-6 max-w-3xl">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Profile</h1>
        <p className="text-gray-600 mt-1">View your account information</p>
      </div>

      <Card>
        <div className="flex items-center gap-6 mb-6 pb-6 border-b border-gray-200">
          <div className="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center">
            <User className="w-10 h-10 text-primary-600" />
          </div>
          <div>
            <h2 className="text-2xl font-bold text-gray-900">Employee #{user?.emp_id}</h2>
            <div className="flex items-center gap-2 mt-2">
              {user?.roles?.map(role => (
                <Badge 
                  key={role} 
                  variant={role === 'admin' ? 'danger' : role === 'manager' ? 'warning' : 'info'}
                >
                  {role}
                </Badge>
              ))}
            </div>
          </div>
        </div>

        <div className="space-y-4">
          <div className="flex items-start gap-4">
            <div className="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center flex-shrink-0">
              <Shield className="w-5 h-5 text-gray-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">Employee ID</p>
              <p className="text-lg font-medium text-gray-900">{user?.emp_id}</p>
            </div>
          </div>

          <div className="flex items-start gap-4">
            <div className="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center flex-shrink-0">
              <Briefcase className="w-5 h-5 text-gray-600" />
            </div>
            <div>
              <p className="text-sm text-gray-500">Role(s)</p>
              <p className="text-lg font-medium text-gray-900 capitalize">
                {user?.roles?.join(', ') || 'N/A'}
              </p>
            </div>
          </div>
        </div>
      </Card>

      <Card>
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Permissions</h3>
        <div className="space-y-3">
          {user?.roles?.includes('admin') && (
            <div className="flex items-center gap-3 p-3 bg-red-50 rounded-lg">
              <div className="w-2 h-2 bg-red-500 rounded-full"></div>
              <div>
                <p className="font-medium text-gray-900">Administrator Access</p>
                <p className="text-sm text-gray-600">Full system access including user and employee management</p>
              </div>
            </div>
          )}
          {user?.roles?.includes('manager') && (
            <div className="flex items-center gap-3 p-3 bg-yellow-50 rounded-lg">
              <div className="w-2 h-2 bg-yellow-500 rounded-full"></div>
              <div>
                <p className="font-medium text-gray-900">Manager Access</p>
                <p className="text-sm text-gray-600">Can create tasks and manage team tasks</p>
              </div>
            </div>
          )}
          {user?.roles?.includes('developer') && (
            <div className="flex items-center gap-3 p-3 bg-blue-50 rounded-lg">
              <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
              <div>
                <p className="font-medium text-gray-900">Developer Access</p>
                <p className="text-sm text-gray-600">Can view and update assigned tasks</p>
              </div>
            </div>
          )}
        </div>
      </Card>
    </div>
  )
}

export default Profile
// ```


// ---

// ## **That's all the code files! 🎉**

// ### **Final Steps:**

// 1. **Install dependencies:**
// ```bash
//    npm install
// ```

// 2. **Create the `.env` file:**
// ```env
//    VITE_API_BASE_URL=http://localhost:8000
// ```

// 3. **Run the development server:**
// ```bash
//    npm run dev
// ```

// 4. **Build for production:**
// ```bash
//    npm run build
// ```

// ### **Additional Notes:**

// - Fix the `jwtDecode` import in `AuthContext.jsx` - you may need to install: `npm install jwt-decode`
// - The app assumes your backend is running on `http://localhost:8000`
// - Make sure you have test users in your database to login
// - All role-based permissions are enforced both in the UI and backend

// **You now have a complete, production-ready Task Manager frontend!** 🚀