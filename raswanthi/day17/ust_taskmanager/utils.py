def next_id(current_max_id: int) -> int:
    """
    Generate the next task ID by incrementing the current maximum ID.
    Example:
      - If current_max_id = 0, this returns 1 (first task).
      - If current_max_id = 5, this returns 6 (next task).
    """
    return current_max_id + 1
