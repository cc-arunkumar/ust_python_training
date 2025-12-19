import React, { useState, useEffect } from 'react'
import { userApi } from '../services/userApi'
import { toast } from 'react-toastify'
import Card from '../components/common/Card'
import Button from '../components/common/Button'
import Input from '../components/common/Input'
import Select from '../components/common/Select'
import Modal from '../components/common/Modal'
import LoadingSpinner from '../components/common/LoadingSpinner'
import Badge from '../components/common/Badge'
import { PlusCircle, Edit2, Trash2, UserPlus } from 'lucide-react'

const Users = () => {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [editingUser, setEditingUser] = useState(null)
  const [formData, setFormData] = useState({
    emp_id: '',
    password: '',
    role: 'developer',
  })
  const [submitting, setSubmitting] = useState(false)

  useEffect(() => {
    fetchUsers()
  }, [])

  const fetchUsers = async () => {
    try {
      setLoading(true)
      const data = await userApi.getAllUsers()
      setUsers(data)
    } catch (error) {
      console.error('Error fetching users:', error)
      toast.error('Failed to load users')
    } finally {
      setLoading(false)
    }
  }

  const handleOpenModal = (user = null) => {
    if (user) {
      setEditingUser(user)
      setFormData({
        emp_id: user.emp_id,
        password: '',
        role: user.role,
      })
    } else {
      setEditingUser(null)
      setFormData({
        emp_id: '',
        password: '',
        role: 'developer',
      })
    }
    setIsModalOpen(true)
  }

  const handleCloseModal = () => {
    setIsModalOpen(false)
    setEditingUser(null)
    setFormData({ emp_id: '', password: '', role: 'developer' })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    try {
      setSubmitting(true)
      if (editingUser) {
        // Update user
        const updateData = { role: formData.role }
        if (formData.password) {
          updateData.password = formData.password
        }
        await userApi.updateUser(editingUser.emp_id, updateData)
        toast.success('User updated successfully')
      } else {
        // Create user
        await userApi.createUser(formData)
        toast.success('User created successfully')
      }
      fetchUsers()
      handleCloseModal()
    } catch (error) {
      console.error('Error saving user:', error)
      if (error.response?.data?.detail) {
        toast.error(error.response.data.detail)
      } else {
        toast.error(`Failed to ${editingUser ? 'update' : 'create'} user`)
      }
    } finally {
      setSubmitting(false)
    }
  }

  const handleDelete = async (empId) => {
    if (!window.confirm('Are you sure you want to delete this user?')) return

    try {
      await userApi.deleteUser(empId)
      toast.success('User deleted successfully')
      fetchUsers()
    } catch (error) {
      console.error('Error deleting user:', error)
      toast.error('Failed to delete user')
    }
  }

  if (loading) {
    return <LoadingSpinner fullScreen text="Loading users..." />
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Users</h1>
          <p className="text-gray-600 mt-1">Manage system users and their roles</p>
        </div>
        <Button onClick={() => handleOpenModal()}>
          <PlusCircle className="w-4 h-4 mr-2" />
          Add User
        </Button>
      </div>

      <Card>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-200">
                <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Employee ID</th>
                <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Role</th>
                <th className="px-4 py-3 text-right text-sm font-semibold text-gray-900">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {users.length === 0 ? (
                <tr>
                  <td colSpan="3" className="px-4 py-8 text-center text-gray-500">
                    No users found
                  </td>
                </tr>
              ) : (
                users.map(user => (
                  <tr key={user.emp_id} className="hover:bg-gray-50">
                    <td className="px-4 py-3 text-sm text-gray-900">{user.emp_id}</td>
                    <td className="px-4 py-3 text-sm">
                      <Badge variant={user.role === 'admin' ? 'danger' : user.role === 'manager' ? 'warning' : 'info'}>
                        {user.role}
                      </Badge>
                    </td>
                    <td className="px-4 py-3 text-sm text-right">
                      <div className="flex items-center justify-end gap-2">
                        <button
                          onClick={() => handleOpenModal(user)}
                          className="p-2 text-blue-600 hover:bg-blue-50 rounded transition-colors"
                          title="Edit"
                        >
                          <Edit2 className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => handleDelete(user.emp_id)}
                          className="p-2 text-red-600 hover:bg-red-50 rounded transition-colors"
                          title="Delete"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </Card>

      {/* Create/Edit Modal */}
      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title={editingUser ? 'Edit User' : 'Create New User'}
        footer={
          <>
            <Button variant="secondary" onClick={handleCloseModal}>
              Cancel
            </Button>
            <Button onClick={handleSubmit} loading={submitting}>
              {editingUser ? 'Update' : 'Create'}
            </Button>
          </>
        }
      >
        <form onSubmit={handleSubmit} className="space-y-4">
          <Input
            label="Employee ID"
            name="emp_id"
            type="number"
            value={formData.emp_id}
            onChange={(e) => setFormData(prev => ({ ...prev, emp_id: e.target.value }))}
            required
            disabled={!!editingUser}
            placeholder="Enter employee ID"
          />

          <Input
            label="Password"
            name="password"
            type="password"
            value={formData.password}
            onChange={(e) => setFormData(prev => ({ ...prev, password: e.target.value }))}
            required={!editingUser}
            placeholder={editingUser ? 'Leave blank to keep current password' : 'Enter password'}
            helperText={editingUser ? 'Leave blank to keep current password' : 'Minimum 6 characters'}
          />

          <Select
            label="Role"
            name="role"
            value={formData.role}
            onChange={(e) => setFormData(prev => ({ ...prev, role: e.target.value }))}
            required
            options={[
              { value: 'developer', label: 'Developer' },
              { value: 'manager', label: 'Manager' },
              { value: 'admin', label: 'Admin' },
            ]}
          />
        </form>
      </Modal>
    </div>
  )
}

export default Users