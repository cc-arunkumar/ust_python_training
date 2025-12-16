import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"
import axios from "axios"

const API_URL = "http://localhost:8000"

export function TaskTable({ token }) {
  const navigate = useNavigate()
  const [tasks, setTasks] = useState([])

  const fetchTasks = async () => {
    try {
      const res = await axios.get(`${API_URL}/tasks`, {
        headers: { Authorization: `Bearer ${token}` },
      })
      setTasks(res.data)
    } catch (err) {
      console.error("Error fetching tasks", err)
    }
  }

  useEffect(() => {
    if (token) {
      fetchTasks()
    }
  }, [token])

  const handleEdit = (task) => {
    navigate(`/create-task`, { state: task })
  }

  const handleDelete = async (taskId) => {
    try {
      await axios.delete(`${API_URL}/tasks/${taskId}`, {
        headers: { Authorization: `Bearer ${token}` },
      })
      fetchTasks()
    } catch (err) {
      console.error("Error deleting task", err)
    }
  }

  return (
    <Table>
      <TableCaption>A list of your tasks.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead className="w-16 text-left">ID</TableHead>
          <TableHead className="text-left">Title</TableHead>
          <TableHead className="text-left">Description</TableHead>
          <TableHead className="text-left">Status</TableHead>
          <TableHead className="text-right">Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {tasks.map((task) => (
          <TableRow key={task.id}>
            <TableCell className="w-16 text-left">{task.id}</TableCell>
            <TableCell className="text-left">{task.title}</TableCell>
            <TableCell className="text-left">{task.description}</TableCell>
            <TableCell className="text-left">
              {task.completed ? " Completed" : " Pending"}
            </TableCell>
            <TableCell className="text-right space-x-2">
              <Button variant="outline" size="sm" onClick={() => handleEdit(task)}>
                Edit
              </Button>
              <Button variant="destructive" size="sm" onClick={() => handleDelete(task.id)}>
                Delete
              </Button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
      <TableFooter>
        <TableRow>
          <TableCell colSpan={4} className="text-left">Total Tasks</TableCell>
          <TableCell className="text-right">{tasks.length}</TableCell>
        </TableRow>
      </TableFooter>
    </Table>
  )
}
