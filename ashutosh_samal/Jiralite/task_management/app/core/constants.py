TASK_STATUSES = {
    "TO_DO",
    "IN_PROGRESS",
    "REVIEW",
    "DONE",
}

# Allowed transitions by role
TASK_STATUS_FLOW = {
    "DEVELOPER": {
        "TO_DO": ["IN_PROGRESS"],
        "IN_PROGRESS": ["REVIEW"],
    },
    "MANAGER": {
        "REVIEW": ["DONE", "IN_PROGRESS"],
    },
}
