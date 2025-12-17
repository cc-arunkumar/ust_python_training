import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import axios from "axios";
import { Input } from "@/components/ui/input";
import { useNavigate } from "react-router-dom";
import { Label } from "@/components/ui/label";
const API_URL = "http://localhost:8000/api/users";
export function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [empId, setEmpId] = useState("");
  const navigate = useNavigate();

 const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res;

      if (empId) {
        // Login by user_id (empId here)
        res = await axios.post(
          `${API_URL}/login/by-user?user_id=${empId}&password=${password}`
        );
      } else {
        alert("Please enter Employee ID");
        return;
      }

      // Save JWT + role
      localStorage.setItem("token", res.data.access_token);
      console.log(res.data.access_token)
      console.log(res.data.role)
      localStorage.setItem("role", res.data.role);

      // Redirect to home
      navigate("/");
    } catch (err) {
      alert("Invalid credentials");
    }
  };
  const handleGetUsers = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/users");
      console.log("All users:", res.data);
    } catch (err) {
      console.error("Error fetching users:", err);
    }
  };

  return (
    <div>
      <h1 className=" -mr-20 text-4xl font-bold mb-4">Welcome to Jira Lite </h1>
      <div className="flex -mr-20 justify-center items-center min-h-50 ">
        <Card className="w-full max-w-sm shadow-lg">
          <CardHeader>
            <CardTitle>Login to your account</CardTitle>
            <CardDescription>Enter your username and password</CardDescription>
            <CardAction />
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit}>
              <div className="flex flex-col gap-6">
                <div className="grid gap-1">
                  <Label htmlFor="emp_id">Employee id</Label>
                  <Input
                    id="emp_id"
                    type="text"
                    placeholder="your employee id"
                    value={empId}
                    onChange={(e) => setEmpId(e.target.value)}
                    required
                  />
                </div>
                <h3 className="m-0 p-0">or</h3>
                <div className="grid gap-1 ">
                  <Label htmlFor="email">Username</Label>
                  <Input
                    id="email"
                    type="text"
                    placeholder="your username"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>

                <div className="grid gap-2">
                  <Label htmlFor="password">Password</Label>
                  <Input
                    id="password"
                    type="password"
                    placeholder="your password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
              </div>
              <CardFooter className="flex-col gap-2 mt-4">
                <Button type="submit" className="w-full">
                  Login
                </Button>
              </CardFooter>
            </form>
          </CardContent>
        </Card>
        {/* <Button
          type="button"
          variant="outline"
          className="w-full mt-2"
          onClick={handleGetUsers}
        >
          Get All Users
        </Button> */}
      </div>
    </div>
  );
}
