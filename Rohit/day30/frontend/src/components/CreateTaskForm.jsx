import { useForm } from "react-hook-form";
import axios from "axios";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { useNavigate, useLocation } from "react-router-dom"
import {
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
  SelectValue,
} from "@/components/ui/select";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";

export function CreateTaskForm() {
  const navigate = useNavigate();
  const location = useLocation();
  const task = location.state?.task;
   const form = useForm({
    defaultValues: task || {
      title: "",
      description: "",
      priority: "",
      status: "",
      expected_closure: "",
      actual_closure: "",
      created_by: "",
      assigned_to: "",
      assigned_by: "",
      remark: "",
      reviewer: "",
      updated_by: "",
      updated_at: "",
    },
  });

  const onSubmit = async (data) => {
    try {
      const token = localStorage.getItem("token");

      if (task) {
        // Editing existing task → PUT with JSON body
        await axios.put(
          `http://localhost:8000/api/tasks/${task.id}`,
          {
            title: data.title,
            description: data.description,
            priority: data.priority,
            status: data.status,
            remark: data.remark,
            assigned_to: Number(data.assigned_to),
          },
          { headers: { Authorization: `Bearer ${token}` } }
        );
        alert("Task updated successfully!");
      } else {
        // Creating new task → POST with query params
        await axios.post(
          "http://localhost:8000/api/tasks",
          null,
          {
            params: {
              title: data.title,
              description: data.description,
              priority: data.priority,
              assigned_to: Number(data.assigned_to),
            },
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        alert("Task created successfully!");
      }

      navigate("/show-task", { replace: true });
    } catch (error) {
      console.error("Error:", error.response?.data || error.message);
      alert(error.response?.data?.detail || "Something went wrong");
    }
  };

  return (
    <div>
      <h1 className="text-4xl font-bold mb-4">Create Task</h1>
      <div className="flex justify-center items-center min-h-screen">
        <Card className="w-full max-w-2xl shadow-lg">
          <CardHeader>
            <CardTitle>Create Task</CardTitle>
            <CardDescription>
              Fill all required fields (*) and optional ones if available.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Form {...form}>
              <form
                onSubmit={form.handleSubmit(onSubmit)}
                className="grid grid-cols-1 md:grid-cols-2 gap-6"
              >
                {/* Task ID */}
                

                {/* Title */}
                <FormField
                  control={form.control}
                  name="title"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Title</FormLabel>
                      <FormControl>
                        <Input placeholder="Enter task title" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Description */}
                <FormField
                  control={form.control}
                  name="description"
                  render={({ field }) => (
                    <FormItem className="md:col-span-2">
                      <FormLabel>* Description</FormLabel>
                      <FormControl>
                        <Textarea
                          placeholder="Enter task description"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Priority */}
                <FormField
                  control={form.control}
                  name="priority"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Priority</FormLabel>
                      <FormControl>
                        <Select
                          value={field.value}
                          onValueChange={field.onChange}
                        >
                          <SelectTrigger>
                            <SelectValue placeholder="Select priority" />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="HIGH">HIGH</SelectItem>
                            <SelectItem value="MEDIUM">MEDIUM</SelectItem>
                            <SelectItem value="LOW">LOW</SelectItem>
                          </SelectContent>
                        </Select>
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Status */}
                <FormField
                  control={form.control}
                  name="status"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Status</FormLabel>
                      <FormControl>
                        <Select
                          value={field.value}
                          onValueChange={field.onChange}
                        >
                          <SelectTrigger>
                            <SelectValue placeholder="Select status" />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="TO_DO">TO_DO</SelectItem>
                            <SelectItem value="IN_PROGRESS">
                              IN_PROGRESS
                            </SelectItem>
                            <SelectItem value="REVIEW">REVIEW</SelectItem>
                            <SelectItem value="DONE">DONE</SelectItem>
                          </SelectContent>
                        </Select>
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Expected Closure Date */}
                <FormField
                  control={form.control}
                  name="expected_closure"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Expected Closure Date</FormLabel>
                      <FormControl>
                        <Input type="date" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Actual Closure Date */}
                <FormField
                  control={form.control}
                  name="actual_closure"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Actual Closure Date</FormLabel>
                      <FormControl>
                        <Input type="date" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Created By */}
                <FormField
                  control={form.control}
                  name="created_by"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Created By</FormLabel>
                      <FormControl>
                        <Select
                          value={field.value}
                          onValueChange={field.onChange}
                        >
                          <SelectTrigger>
                            <SelectValue placeholder="Select role" />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="MANAGER">MANAGER</SelectItem>
                            <SelectItem value="ADMIN">ADMIN</SelectItem>
                          </SelectContent>
                        </Select>
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Assigned To */}
                <FormField
                  control={form.control}
                  name="assigned_to"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Assigned To</FormLabel>
                      <FormControl>
                        <Input placeholder="Assignee ID" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Assigned By */}
                <FormField
                  control={form.control}
                  name="assigned_by"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Assigned By</FormLabel>
                      <FormControl>
                        <Input placeholder="Assigner ID" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Reviewer */}
                <FormField
                  control={form.control}
                  name="reviewer"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Reviewer</FormLabel>
                      <FormControl>
                        <Input placeholder="Reviewer name" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Remark */}
                <FormField
                  control={form.control}
                  name="remark"
                  render={({ field }) => (
                    <FormItem className="md:col-span-2">
                      <FormLabel>Remark (max 500)</FormLabel>
                      <FormControl>
                        <Textarea
                          placeholder="Optional remarks"
                          maxLength={500}
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Updated By */}
                <FormField
                  control={form.control}
                  name="updated_by"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Updated By</FormLabel>
                      <FormControl>
                        <Input placeholder="Updater ID" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Updated At */}
                <FormField
                  control={form.control}
                  name="updated_at"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Updated At (date)</FormLabel>
                      <FormControl>
                        <Input type="date" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                <div className="md:col-span-2">
                  <Button type="submit" className="w-full">
                    Save Task
                  </Button>
                </div>
              </form>
            </Form>
          </CardContent>
          <CardFooter>
            <p className="text-sm text-muted-foreground">
              No backend connected — submission logs to console.
            </p>
          </CardFooter>
        </Card>
      </div>
    </div>
  );
}
