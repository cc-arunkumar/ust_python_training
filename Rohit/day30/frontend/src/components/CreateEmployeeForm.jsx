import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { EmployeeSchema } from "../schemas/taskSchema";

import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";

export function CreateEmployeeForm() {
  const form = useForm({
    resolver: zodResolver(EmployeeSchema),
    defaultValues: {
      E_id: 0,
      name: "",
      email: "",
      Designation: "",
      Managerid: 0,
    },
  });

  const onSubmit = (data) => {
    console.log("Validated Employee:", data);
  };

  return (
    <div>
      <h1 className=" mr-0 text-4xl font-bold mb-4">Create Employee</h1>
      <div className="flex justify-center items-center min-h-screen">
        <Card className="w-full max-w-md shadow-lg">
          <CardHeader>
            <CardTitle>Add Employee</CardTitle>
            <CardDescription>
              Fill all required fields (*) to add a new employee.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Form {...form}>
              <form
                onSubmit={form.handleSubmit(onSubmit)}
                className="space-y-6"
              >
                {/* Employee ID */}
                <FormField
                  control={form.control}
                  name="E_id"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Employee ID</FormLabel>
                      <FormControl>
                        <Input
                          type="e_id"
                          placeholder="e.g., 101"
                          {...field}
                          onChange={(e) =>
                            field.onChange(e.target.value)
                          }
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Name */}
                <FormField
                  control={form.control}
                  name="name"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Name</FormLabel>
                      <FormControl>
                        <Input placeholder="Enter employee name" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Email */}
                <FormField
                  control={form.control}
                  name="email"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Email</FormLabel>
                      <FormControl>
                        <Input
                          type="email"
                          placeholder="Enter email address"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Designation */}
                <FormField
                  control={form.control}
                  name="Designation"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Designation</FormLabel>
                      <FormControl>
                        <Input placeholder="Enter designation" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                {/* Manager ID */}
                <FormField
                  control={form.control}
                  name="Managerid"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>* Manager ID</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="e.g., 12"
                          {...field}
                          onChange={(e) =>
                            field.onChange(Number(e.target.value))
                          }
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                <Button type="submit" className="w-full">
                  Add Employee
                </Button>
              </form>
            </Form>
          </CardContent>
          <CardFooter>
            <p className="text-sm text-muted-foreground">
              Submission logs to console — no backend connected.
            </p>
          </CardFooter>
        </Card>
      </div>
    </div>
  );
}
