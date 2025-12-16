import { useForm } from "react-hook-form"
import { useLocation, useNavigate } from "react-router-dom"
import axios from "axios"
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Checkbox } from "@/components/ui/checkbox"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card"

const API_URL = "http://localhost:8000"

export function CreateTaskForm({ token }) {
  const location = useLocation()
  const navigate = useNavigate()
  const task = location.state
  console.log(task)

  const form = useForm({
    defaultValues: task || {
      title: "",
      description: "",
      completed: false,
    },
  })

  const onSubmit = async (data) => {
    try {
      if (task) {
        
        await axios.put(`${API_URL}/tasks/${task.id}`, data, {
          headers: { Authorization: `Bearer ${token}` },
        })
        
      } else {
        
        await axios.post(`${API_URL}/tasks`, data, {
          headers: { Authorization: `Bearer ${token}` },
        })
        
      }
      navigate("/tasks") 
    } catch (err) {
      alert("Error saving task")
      console.error(err)
    }
  }

  return (
    <Card className="w-full max-w-md mx-auto shadow-lg">
      <CardHeader>
        <CardTitle>{task ? "Edit Task" : "Create a New Task"}</CardTitle>
        <CardDescription>
          {task
            ? "Update the details below."
            : "Fill out the details below to add a new task."}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
            <FormField
              control={form.control}
              name="title"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Title</FormLabel>
                  <FormControl>
                    <Input placeholder="Enter task title" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="description"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Description</FormLabel>
                  <FormControl>
                    <Textarea
                      placeholder="Enter task description"
                      className="resize-none"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="completed"
              render={({ field }) => (
                <FormItem className="flex items-center space-x-2">
                  <FormControl>
                    <Checkbox
                      checked={field.value}
                      onCheckedChange={field.onChange}
                    />
                  </FormControl>
                  <FormLabel>Mark as Completed</FormLabel>
                </FormItem>
              )}
            />

            <Button type="submit" className="w-full">
              {task ? "Update Task" : "Create Task"}
            </Button>
          </form>
        </Form>
      </CardContent>
      <CardFooter>
        <p className="text-sm text-muted-foreground">
          {task
            ? "Your changes will be saved."
            : "Your task will be saved to the Task Manager."}
        </p>
      </CardFooter>
    </Card>
  )
}
