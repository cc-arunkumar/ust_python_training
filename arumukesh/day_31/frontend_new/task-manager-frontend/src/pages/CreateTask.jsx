import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { taskApi } from '../services/taskApi'
import { toast } from 'react-toastify'
import TaskForm from '../components/tasks/TaskForm'
import Card from '../components/common/Card'
import { ArrowLeft } from 'lucide-react'
import Button from '../components/common/Button'

const CreateTask = () => {
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (taskData) => {
    try {
      setLoading(true)
      await taskApi.createTask(taskData)
      toast.success('Task created successfully!')
      navigate('/tasks')
    } catch (error) {
      console.error('Error creating task:', error)
      if (error.response?.data?.detail) {
        toast.error(error.response.data.detail)
      } else {
        toast.error('Failed to create task')
      }
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6 max-w-4xl">
      <div className="flex items-center gap-4">
        <Button
          variant="ghost"
          onClick={() => navigate('/tasks')}
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back
        </Button>
      </div>

      <div>
        <h1 className="text-3xl font-bold text-gray-900">Create New Task</h1>
        <p className="text-gray-600 mt-1">Fill in the details to create a new task</p>
      </div>

      <Card>
        <TaskForm onSubmit={handleSubmit} loading={loading} />
      </Card>
    </div>
  )
}

export default CreateTask