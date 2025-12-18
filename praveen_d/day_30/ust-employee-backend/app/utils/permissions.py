ROLE_PERMISSIONS = {
    "ADMIN": {
        "employee:create",
        "employee:update",
        "employee:delete",
        "employee:assign",
        "employee:read_all",
        "employee:read_one",
        "task:read_all",
        "task:read_one",
        "user:create",
        "user:read",
        "user:update",
        "user:delete",
    },
    "MANAGER": {
        "employee:read_all",
        "employee:read_one",
        "task:create",
        "task:update",
        "task:review",
        "task:read_all",
        "task:read_one",
    },
    "EMPLOYEE": {
        "employee:read_one",
        "task:read_own",      # 🔑 IMPORTANT
        "task:update",
         "task:read_one",
        "file:upload",
    }
}

