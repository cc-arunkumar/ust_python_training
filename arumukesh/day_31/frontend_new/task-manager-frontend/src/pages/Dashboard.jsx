import React, { useState, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { taskApi } from '../services/taskApi'
import { Link } from 'react-router-dom'
import { 
  ListTodo, 
  Clock, 
  CheckCircle, 
  AlertCircle,
  TrendingUp,
  Users,
  PlusCircle
} from 'lucide-react'
import Card from '../components/common/Card'
import Badge from '../components/common/Badge'
import LoadingSpinner from '../components/common/LoadingSpinner'
import Button from '../components/common/Button'
import { formatDate, getDaysRemaining } from '../utils/helpers'

const Dashboard = () => {
  const { user, isAdmin, isManager } = useAuth()
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [stats, setStats] = useState({
    total: 0,
    pending: 0,
    inProgress: 0,
    inReview: 0,
    completed: 0,
    overdue: 0,
  })

  useEffect(() => {
    fetchTasks()
  }, [])

  const fetchTasks = async () => {
    try {
      setLoading(true)
      const data = await taskApi.getAllTasks()
      setTasks(data)
      calculateStats(data)
    } catch (error) {
      console.error('Error fetching tasks:', error)
    } finally {
      setLoading(false)
    }
  }

  const calculateStats = (tasksData) => {
    const now = new Date()
    setStats({
      total: tasksData.length,
      pending: tasksData.filter(t => t.status === 'pending').length,
      inProgress: tasksData.filter(t => t.status === 'in_progress').length,
      inReview: tasksData.filter(t => t.status === 'in_review').length,
      completed: tasksData.filter(t => t.status === 'completed').length,
      overdue: tasksData.filter(t => {
        if (t.status === 'completed') return false
        const daysInfo = getDaysRemaining(t.expected_closure)
        return daysInfo?.isOverdue
      }).length,
    })
  }

  const myTasks = tasks.filter(t => String(t.assigned_to) === String(user.emp_id))
  const reviewTasks = tasks.filter(t => String(t.reviewer) === String(user.emp_id) && t.status === 'in_review')

  if (loading) {
    return <LoadingSpinner fullScreen text="Loading dashboard..." />
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600 mt-1">Welcome back, Employee #{user?.emp_id}</p>
        </div>
        {(isAdmin() || isManager()) && (
          <Link to="/tasks/create">
            <Button>
              <PlusCircle className="w-4 h-4 mr-2" />
              Create Task
            </Button>
          </Link>
        )}
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card hover>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Total Tasks</p>
              <p className="text-3xl font-bold text-gray-900">{stats.total}</p>
            </div>
            <div className="bg-primary-100 p-3 rounded-full">
              <ListTodo className="w-6 h-6 text-primary-600" />
            </div>
          </div>
        </Card>

        <Card hover>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">In Progress</p>
              <p className="text-3xl font-bold text-blue-600">{stats.inProgress}</p>
            </div>
            <div className="bg-blue-100 p-3 rounded-full">
              <Clock className="w-6 h-6 text-blue-600" />
            </div>
          </div>
        </Card>

        <Card hover>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Completed</p>
              <p className="text-3xl font-bold text-green-600">{stats.completed}</p>
            </div>
            <div className="bg-green-100 p-3 rounded-full">
              <CheckCircle className="w-6 h-6 text-green-600" />
            </div>
          </div>
        </Card>

        <Card hover>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Overdue</p>
              <p className="text-3xl font-bold text-red-600">{stats.overdue}</p>
            </div>
            <div className="bg-red-100 p-3 rounded-full">
              <AlertCircle className="w-6 h-6 text-red-600" />
            </div>
          </div>
        </Card>
      </div>

      {/* Status Breakdown */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Status Overview</h2>
          <div className="space-y-3">
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded">
              <span className="text-gray-700">Pending</span>
              <Badge variant="default">{stats.pending}</Badge>
            </div>
            <div className="flex items-center justify-between p-3 bg-blue-50 rounded">
              <span className="text-gray-700">In Progress</span>
              <Badge variant="info">{stats.inProgress}</Badge>
            </div>
            <div className="flex items-center justify-between p-3 bg-yellow-50 rounded">
              <span className="text-gray-700">In Review</span>
              <Badge variant="warning">{stats.inReview}</Badge>
            </div>
            <div className="flex items-center justify-between p-3 bg-green-50 rounded">
              <span className="text-gray-700">Completed</span>
              <Badge variant="success">{stats.completed}</Badge>
            </div>
          </div>
        </Card>

        <Card>
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
          <div className="space-y-3">
            <Link to="/tasks">
              <button className="w-full flex items-center justify-between p-3 bg-primary-50 hover:bg-primary-100 rounded transition-colors">
                <span className="flex items-center gap-2 text-primary-700 font-medium">
                  <ListTodo className="w-5 h-5" />
                  View All Tasks
                </span>
                <span className="text-primary-600">→</span>
              </button>
            </Link>
            {(isAdmin() || isManager()) && (
              <Link to="/tasks/create">
                <button className="w-full flex items-center justify-between p-3 bg-green-50 hover:bg-green-100 rounded transition-colors">
                  <span className="flex items-center gap-2 text-green-700 font-medium">
                    <PlusCircle className="w-5 h-5" />
                    Create New Task
                  </span>
                  <span className="text-green-600">→</span>
                </button>
              </Link>
            )}
            {isAdmin() && (
              <>
                <Link to="/users">
                  <button className="w-full flex items-center justify-between p-3 bg-purple-50 hover:bg-purple-100 rounded transition-colors">
                    <span className="flex items-center gap-2 text-purple-700 font-medium">
                      <Users className="w-5 h-5" />
                      Manage Users
                    </span>
                    <span className="text-purple-600">→</span>
                  </button>
                </Link>
                <Link to="/employees">
                  <button className="w-full flex items-center justify-between p-3 bg-indigo-50 hover:bg-indigo-100 rounded transition-colors">
                    <span className="flex items-center gap-2 text-indigo-700 font-medium">
                      <Users className="w-5 h-5" />
                      Manage Employees
                    </span>
                    <span className="text-indigo-600">→</span>
                  </button>
                </Link>
              </>
            )}
          </div>
        </Card>
      </div>

      {/* My Tasks */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-semibold text-gray-900">My Tasks</h2>
            <Badge>{myTasks.length}</Badge>
          </div>
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {myTasks.length === 0 ? (
              <p className="text-gray-500 text-center py-8">No tasks assigned to you</p>
            ) : (
              myTasks.slice(0, 5).map(task => {
                const daysInfo = getDaysRemaining(task.expected_closure)
                return (
                  <div key={task.t_id} className="p-3 bg-gray-50 rounded hover:bg-gray-100 transition-colors">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <h4 className="font-medium text-gray-900">{task.title}</h4>
                        <p className="text-sm text-gray-600 mt-1">Due: {formatDate(task.expected_closure)}</p>
                      </div>
                      <Badge variant={task.status === 'completed' ? 'success' : 'default'}>
                        {task.status.replace('_', ' ')}
                      </Badge>
                    </div>
                    {daysInfo && (
                      <p className={`text-xs mt-2 ${daysInfo.isOverdue ? 'text-red-600' : 'text-gray-500'}`}>
                        {daysInfo.text}
                      </p>
                    )}
                  </div>
                )
              })
            )}
            {myTasks.length > 5 && (
              <Link to="/tasks" className="block text-center text-primary-600 hover:text-primary-700 text-sm font-medium pt-2">
                View all {myTasks.length} tasks →
              </Link>
            )}
          </div>
        </Card>

        {/* Tasks to Review */}
        <Card>
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-semibold text-gray-900">Tasks to Review</h2>
            <Badge variant="warning">{reviewTasks.length}</Badge>
          </div>
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {reviewTasks.length === 0 ? (
              <p className="text-gray-500 text-center py-8">No tasks pending review</p>
            ) : (
              reviewTasks.slice(0, 5).map(task => {
                const daysInfo = getDaysRemaining(task.expected_closure)
                return (
                  <div key={task.t_id} className="p-3 bg-yellow-50 rounded hover:bg-yellow-100 transition-colors">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <h4 className="font-medium text-gray-900">{task.title}</h4>
                        <p className="text-sm text-gray-600 mt-1">
                          Assigned to: {task.assigned_to}
                        </p>
                        <p className="text-sm text-gray-600">Due: {formatDate(task.expected_closure)}</p>
                      </div>
                      <Badge variant="warning">Review</Badge>
                    </div>
                    {daysInfo && (
                      <p className={`text-xs mt-2 ${daysInfo.isOverdue ? 'text-red-600' : 'text-gray-500'}`}>
                        {daysInfo.text}
                      </p>
                    )}
                  </div>
                )
              })
            )}
            {reviewTasks.length > 5 && (
              <Link to="/tasks" className="block text-center text-primary-600 hover:text-primary-700 text-sm font-medium pt-2">
                View all {reviewTasks.length} review tasks →
              </Link>
            )}
          </div>
        </Card>
      </div>
    </div>
  )
}

export default Dashboard