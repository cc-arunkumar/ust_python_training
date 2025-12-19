import React, { useState, useEffect } from 'react'
import { DndProvider, useDrag, useDrop } from 'react-dnd'
import { HTML5Backend } from 'react-dnd-html5-backend'
import { useAuth } from '../../context/AuthContext'
import { taskApi } from '../../services/taskApi'
import { toast } from 'react-toastify'
import TaskCard from './TaskCard'
import TaskDetailModal from './TaskDetailModal'
import LoadingSpinner from '../common/LoadingSpinner'
import { isValidStatusTransition, sortByPriority } from '../../utils/helpers'
import { STATUS_LABELS } from '../../utils/constants'

const ITEM_TYPE = 'TASK'

const DraggableTask = ({ task, canDrag, onClick }) => {
  const [, drag] = useDrag({
    type: ITEM_TYPE,
    item: { id: task.t_id, currentStatus: task.status },
    canDrag: () => canDrag,
  })

  return (
    <div ref={canDrag ? drag : null} className={canDrag ? 'cursor-move' : 'cursor-default'}>
      <TaskCard task={task} onClick={onClick} />
    </div>
  )
}

const KanbanColumn = ({ status, tasks, onDrop, label, bgColor, canDragTask, onTaskClick }) => {
  const [{ isOver }, drop] = useDrop({
    accept: ITEM_TYPE,
    drop: (item) => onDrop(item.id, status, item.currentStatus),
    collect: (monitor) => ({
      isOver: monitor.isOver(),
    }),
  })

  return (
    <div className="flex-1 min-w-[280px]">
      <div className={`${bgColor} p-3 rounded-t-lg border-b-2 border-gray-300`}>
        <h3 className="font-semibold text-gray-800 flex items-center justify-between">
          <span>{label}</span>
          <span className="text-sm bg-white px-2 py-1 rounded-full">
            {tasks.length}
          </span>
        </h3>
      </div>
      <div
        ref={drop}
        className={`
          min-h-[500px] p-3 bg-gray-50 rounded-b-lg border-2 border-dashed
          ${isOver ? 'border-primary-400 bg-primary-50' : 'border-gray-300'}
        `}
      >
        <div className="space-y-3">
          {tasks.map(task => (
            <DraggableTask
              key={task.t_id}
              task={task}
              canDrag={canDragTask(task)}
              onClick={() => onTaskClick(task)}
            />
          ))}
          {tasks.length === 0 && (
            <div className="text-center text-gray-400 py-8">
              No tasks
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

const KanbanBoard = () => {
  const { user } = useAuth()
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [selectedTask, setSelectedTask] = useState(null)

  const canDragTask = (task) => {
    if (task.status === 'completed') return false
    
    const userEmpId = String(user.emp_id)
    const isReviewer = String(task.reviewer) === userEmpId
    const isAssignee = String(task.assigned_to) === userEmpId
    
    if (isReviewer) {
      return task.status === 'in_review'
    }
    
    if (isAssignee) {
      return task.status === 'pending' || task.status === 'in_progress'
    }
    
    return false
  }

  const fetchTasks = async () => {
    try {
      setLoading(true)
      const data = await taskApi.getAllTasks()
      setTasks(data)
    } catch (error) {
      console.error('Error fetching tasks:', error)
      toast.error('Failed to load tasks')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchTasks()
  }, [])

  const handleDrop = async (taskId, newStatus, currentStatus) => {
    if (newStatus === currentStatus) return

    const task = tasks.find(t => t.t_id === taskId)
    if (!task) return

    const userEmpId = String(user.emp_id)
    const isReviewer = String(task.reviewer) === userEmpId
    const isAssignee = String(task.assigned_to) === userEmpId

    // Validate transition
    const userRoles = user.roles?.map(r => r.toLowerCase()) || []
    const valid = isValidStatusTransition(
      currentStatus, 
      newStatus, 
      userRoles[0], 
      isReviewer, 
      isAssignee
    )

    if (!valid) {
      toast.error('Invalid status transition')
      return
    }

    try {
      await taskApi.updateTaskStatus(taskId, newStatus)
      toast.success('Task status updated successfully')
      fetchTasks()
    } catch (error) {
      console.error('Error updating task status:', error)
      toast.error('Failed to update task status')
    }
  }

  const handleTaskClick = (task) => {
    setSelectedTask(task)
  }

  const groupedTasks = {
    pending: sortByPriority(tasks.filter(t => t.status === 'pending')),
    in_progress: sortByPriority(tasks.filter(t => t.status === 'in_progress')),
    in_review: sortByPriority(tasks.filter(t => t.status === 'in_review')),
    completed: sortByPriority(tasks.filter(t => t.status === 'completed')),
  }

  if (loading) {
    return <LoadingSpinner fullScreen text="Loading tasks..." />
  }

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="overflow-x-auto">
        <div className="flex gap-4 min-w-max pb-4">
          <KanbanColumn
            status="pending"
            tasks={groupedTasks.pending}
            onDrop={handleDrop}
            label={STATUS_LABELS.pending}
            bgColor="bg-gray-100"
            canDragTask={canDragTask}
            onTaskClick={handleTaskClick}
          />
          <KanbanColumn
            status="in_progress"
            tasks={groupedTasks.in_progress}
            onDrop={handleDrop}
            label={STATUS_LABELS.in_progress}
            bgColor="bg-blue-100"
            canDragTask={canDragTask}
            onTaskClick={handleTaskClick}
          />
          <KanbanColumn
            status="in_review"
            tasks={groupedTasks.in_review}
            onDrop={handleDrop}
            label={STATUS_LABELS.in_review}
            bgColor="bg-yellow-100"
            canDragTask={canDragTask}
            onTaskClick={handleTaskClick}
          />
          <KanbanColumn
            status="completed"
            tasks={groupedTasks.completed}
            onDrop={handleDrop}
            label={STATUS_LABELS.completed}
            bgColor="bg-green-100"
            canDragTask={canDragTask}
            onTaskClick={handleTaskClick}
          />
        </div>
      </div>

      {selectedTask && (
        <TaskDetailModal
          task={selectedTask}
          isOpen={!!selectedTask}
          onClose={() => setSelectedTask(null)}
          onUpdate={fetchTasks}
        />
      )}
    </DndProvider>
  )
}

export default KanbanBoard