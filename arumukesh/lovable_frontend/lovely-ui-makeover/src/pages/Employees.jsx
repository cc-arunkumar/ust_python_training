import React, { useState, useEffect } from 'react'
import { employeeApi } from '../services/employeeApi'
import { toast } from 'react-toastify'
import Card from '../components/common/Card'
import Button from '../components/common/Button'
import Input from '../components/common/Input'
import Select from '../components/common/Select'
import Modal from '../components/common/Modal'
import LoadingSpinner from '../components/common/LoadingSpinner'
import { PlusCircle, Edit2, Trash2, Mail, Briefcase } from 'lucide-react'

const Employees = () => {
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(true)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [editingEmployee, setEditingEmployee] = useState(null)
  const [formData, setFormData] = useState({
    emp_id: '',
    name: '',
    email: '',
    designation: '',
    mgr_id: '',
  })
  const [submitting, setSubmitting] = useState(false)

  useEffect(() => {
    fetchEmployees()
  }, [])

  const fetchEmployees = async () => {
    try {
      setLoading(true)
      const data = await employeeApi.getAllEmployees()
      setEmployees(data)
    } catch (error) {
      console.error('Error fetching employees:', error)
      toast.error('Failed to load employees')
} finally {
setLoading(false)
}
}
const handleOpenModal = (employee = null) => {
if (employee) {
setEditingEmployee(employee)
setFormData({
emp_id: employee.emp_id,
name: employee.name,
email: employee.email,
designation: employee.designation,
mgr_id: employee.mgr_id || '',
})
} else {
setEditingEmployee(null)
setFormData({
emp_id: '',
name: '',
email: '',
designation: '',
mgr_id: '',
})
}
setIsModalOpen(true)
}
const handleCloseModal = () => {
setIsModalOpen(false)
setEditingEmployee(null)
setFormData({ emp_id: '', name: '', email: '', designation: '', mgr_id: '' })
}
const handleSubmit = async (e) => {
e.preventDefault()
try {
  setSubmitting(true)
  if (editingEmployee) {
    const updateData = {
      name: formData.name,
      email: formData.email,
      designation: formData.designation,
      mgr_id: formData.mgr_id || null,
    }
    await employeeApi.updateEmployee(editingEmployee.emp_id, updateData)
    toast.success('Employee updated successfully')
  } else {
    await employeeApi.createEmployee(formData)
    toast.success('Employee created successfully')
  }
  fetchEmployees()
  handleCloseModal()
} catch (error) {
  console.error('Error saving employee:', error)
  if (error.response?.data?.detail) {
    toast.error(error.response.data.detail)
  } else {
    toast.error(`Failed to ${editingEmployee ? 'update' : 'create'} employee`)
  }
} finally {
  setSubmitting(false)
}
}
const handleDelete = async (empId) => {
if (!window.confirm('Are you sure you want to delete this employee?')) return
try {
  await employeeApi.deleteEmployee(empId)
  toast.success('Employee deleted successfully')
  fetchEmployees()
} catch (error) {
  console.error('Error deleting employee:', error)
  toast.error('Failed to delete employee')
}
}
const getManagerName = (mgrId) => {
const manager = employees.find(e => e.emp_id === mgrId)
return manager ? manager.name : 'N/A'
}
if (loading) {
return <LoadingSpinner fullScreen text="Loading employees..." />
}
return (
<div className="space-y-6">
<div className="flex items-center justify-between">
<div>
<h1 className="text-3xl font-bold text-gray-900">Employees</h1>
<p className="text-gray-600 mt-1">Manage employee records</p>
</div>
<Button onClick={() => handleOpenModal()}>
<PlusCircle className="w-4 h-4 mr-2" />
Add Employee
</Button>
</div>
<Card>
    <div className="overflow-x-auto">
      <table className="w-full">
        <thead>
          <tr className="border-b border-gray-200">
            <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Employee ID</th>
            <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Name</th>
            <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Email</th>
            <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Designation</th>
            <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">Manager</th>
            <th className="px-4 py-3 text-right text-sm font-semibold text-gray-900">Actions</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200">
          {employees.length === 0 ? (
            <tr>
              <td colSpan="6" className="px-4 py-8 text-center text-gray-500">
                No employees found
              </td>
            </tr>
          ) : (
            employees.map(employee => (
              <tr key={employee.emp_id} className="hover:bg-gray-50">
                <td className="px-4 py-3 text-sm font-medium text-gray-900">{employee.emp_id}</td>
                <td className="px-4 py-3 text-sm text-gray-900">{employee.name}</td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  <div className="flex items-center gap-2">
                    <Mail className="w-4 h-4 text-gray-400" />
                    {employee.email}
                  </div>
                </td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  <div className="flex items-center gap-2">
                    <Briefcase className="w-4 h-4 text-gray-400" />
                    {employee.designation}
                  </div>
                </td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  {employee.mgr_id ? getManagerName(employee.mgr_id) : 'N/A'}
                </td>
                <td className="px-4 py-3 text-sm text-right">
                  <div className="flex items-center justify-end gap-2">
                    <button
                      onClick={() => handleOpenModal(employee)}
                      className="p-2 text-blue-600 hover:bg-blue-50 rounded transition-colors"
                      title="Edit"
                    >
                      <Edit2 className="w-4 h-4" />
                    </button>
                    <button
                      onClick={() => handleDelete(employee.emp_id)}
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
    title={editingEmployee ? 'Edit Employee' : 'Create New Employee'}
    size="large"
    footer={
      <>
        <Button variant="secondary" onClick={handleCloseModal}>
          Cancel
        </Button>
        <Button onClick={handleSubmit} loading={submitting}>
          {editingEmployee ? 'Update' : 'Create'}
        </Button>
      </>
    }
  >
    <form onSubmit={handleSubmit} className="space-y-4">
      <Input
        label="Employee ID"
        name="emp_id"
        type="text"
        value={formData.emp_id}
        onChange={(e) => setFormData(prev => ({ ...prev, emp_id: e.target.value }))}
        required
        disabled={!!editingEmployee}
        placeholder="e.g., EMP001"
      />

      <Input
        label="Name"
        name="name"
        type="text"
        value={formData.name}
        onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
        required
        placeholder="Enter employee name"
      />

      <Input
        label="Email"
        name="email"
        type="email"
        value={formData.email}
        onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
        required
        placeholder="employee@company.com"
      />

      <Input
        label="Designation"
        name="designation"
        type="text"
        value={formData.designation}
        onChange={(e) => setFormData(prev => ({ ...prev, designation: e.target.value }))}
        required
        placeholder="e.g., Senior Developer"
      />

      <Select
        label="Manager"
        name="mgr_id"
        value={formData.mgr_id}
        onChange={(e) => setFormData(prev => ({ ...prev, mgr_id: e.target.value }))}
        options={[
          { value: '', label: 'No Manager' },
          ...employees
            .filter(e => e.emp_id !== formData.emp_id)
            .map(emp => ({
              value: emp.emp_id,
              label: `${emp.name} (${emp.emp_id})`
            }))
        ]}
      />
    </form>
  </Modal>
</div>
)
}
export default Employees