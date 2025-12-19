import React, { useState, useEffect } from 'react'
import { useAuth } from '../../context/AuthContext'
import { employeeApi } from '../../services/employeeApi'
import Input from '../common/Input'
import Select from '../common/Select'
import Button from '../common/Button'
import { TASK_PRIORITY, TASK_STATUS } from '../../utils/constants'

const TaskForm = ({ onSubmit, initialData = null, loading = false }) => {
  const { user } = useAuth()
  const [employees, setEmployees] = useState([])
  const [managers, setManagers] = useState([])
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    assigned_to: '',
    priority: 'medium',
    status: 'pending',
    reviewer: '',
    expected_closure: '',
    remarks: '',
  })
  const [errors, setErrors] = useState({})

  useEffect(() => {
    fetchEmployees()
  }, [])

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        description: initialData.description || '',
        assigned_to: initialData.assigned_to || '',
        priority: initialData.priority || 'medium',
        status: initialData.status || 'pending',
        reviewer: initialData.reviewer || '',
        expected_closure: initialData.expected_closure || '',
        remarks: initialData.remarks || '',
      })
    }
  }, [initialData])

  const fetchEmployees = async () => {
    try {
      const data = await employeeApi.getAllEmployees()
      setEmployees(data)
      
      // Filter managers (employees who have subordinates)
      const managerIds = [...new Set(data.filter(e => e.mgr_id).map(e => e.mgr_id))]
      const managerList = data.filter(e => managerIds.includes(e.emp_id))
      setManagers(managerList)
    } catch (error) {
      console.error('Error fetching employees:', error)
    }
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }))
    }
  }

  const validate = () => {
    const newErrors = {}
    
    if (!formData.title.trim()) newErrors.title = 'Title is required'
    if (!formData.description.trim()) newErrors.description = 'Description is required'
    if (!formData.assigned_to) newErrors.assigned_to = 'Assignee is required'
    if (!formData.reviewer) newErrors.reviewer = 'Reviewer is required'
    if (!formData.expected_closure) newErrors.expected_closure = 'Expected closure date is required'
    
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    
    if (!validate()) return
    
    const submitData = {
      ...formData,
      created_by: String(user.emp_id),
      assigned_by: String(user.emp_id),
      expected_closure: new Date(formData.expected_closure).toISOString(),
    }
    
    onSubmit(submitData)
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <Input
        label="Task Title"
        name="title"
        value={formData.title}
        onChange={handleChange}
        error={errors.title}
        required
        placeholder="Enter task title"
      />

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Description <span className="text-red-500">*</span>
        </label>
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          rows={4}
          className={`
            w-full px-3 py-2 border rounded-lg shadow-sm
            focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent
            ${errors.description ? 'border-red-500' : 'border-gray-300'}
          `}
          placeholder="Enter task description"
        />
        {errors.description && (
          <p className="mt-1 text-sm text-red-600">{errors.description}</p>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Select
          label="Assign To"
          name="assigned_to"
          value={formData.assigned_to}
          onChange={handleChange}
          error={errors.assigned_to}
          required
          options={[
            { value: '', label: 'Select employee' },
            ...employees.map(emp => ({
              value: emp.emp_id,
              label: `${emp.name} (${emp.emp_id})`
            }))
          ]}
        />

        <Select
          label="Reviewer"
          name="reviewer"
          value={formData.reviewer}
          onChange={handleChange}
          error={errors.reviewer}
          required
          options={[
            { value: '', label: 'Select reviewer' },
            ...managers.map(mgr => ({
              value: mgr.emp_id,
              label: `${mgr.name} (${mgr.emp_id})`
            }))
          ]}
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Select
          label="Priority"
          name="priority"
          value={formData.priority}
          onChange={handleChange}
          required
          options={Object.entries(TASK_PRIORITY).map(([key, value]) => ({
            value,
            label: key
          }))}
        />

        <Select
          label="Status"
          name="status"
          value={formData.status}
          onChange={handleChange}
          required
          options={[
            { value: TASK_STATUS.PENDING, label: 'Pending' },
            { value: TASK_STATUS.IN_PROGRESS, label: 'In Progress' },
            { value: TASK_STATUS.IN_REVIEW, label: 'In Review' },
            { value: TASK_STATUS.COMPLETED, label: 'Completed' },
          ]}
        />

        <Input
          label="Expected Closure"
          name="expected_closure"
          type="date"
          value={formData.expected_closure}
          onChange={handleChange}
          error={errors.expected_closure}
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Remarks
        </label>
        <textarea
          name="remarks"
          value={formData.remarks}
          onChange={handleChange}
          rows={3}
          className="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          placeholder="Add any additional notes (optional)"
        />
      </div>

      <div className="flex justify-end gap-3 pt-4">
        <Button type="submit" loading={loading}>
          {initialData ? 'Update Task' : 'Create Task'}
        </Button>
      </div>
    </form>
  )
}

export default TaskForm