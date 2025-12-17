import { z } from "zod";

export const TaskSchema = z.object({
  task_id: z.number().int(),
  title: z.string().min(1),
  description: z.string().min(1),
  priority: z.enum(["HIGH", "MEDIUM", "LOW"]),
  status: z.enum(["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"]),
  expected_closure: z.string().datetime({ offset: true }), 
  actual_closure: z.string().datetime({ offset: true }).optional(),
  created_by: z.enum(["MANAGER", "ADMIN"]),
  assigned_to: z.number().int().optional(),
  assigned_by: z.number().int().optional(),
  remark: z.string().max(500).optional(),
  reviewer: z.string().optional(),
  updated_by: z.number().int().optional(),
  updated_at: z.string().datetime({ offset: true }).optional(),
});



export const EmployeeSchema = z.object({
  E_id: z.number().int(),                 
  name: z.string().min(1, "Name is required"), 
  email: z.string().email("Invalid email address"),    
  Designation: z.string().min(1, "Designation is required"), 
  Managerid: z.number().int(),             
});