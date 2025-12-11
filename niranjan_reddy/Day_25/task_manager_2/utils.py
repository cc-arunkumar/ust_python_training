from database import SessionLocal,Task


# Function to create a new task in the database
def create_task(title: str, description: str, user_id: int, completed: bool = False):
    session = SessionLocal()  # Create a new session for interacting with the database
    try:
        # Create a new task instance
        new_task = Task(title=title, description=description, completed=completed, user_id=user_id)
        session.add(new_task)  # Add the new task to the session
        session.commit()  # Commit the transaction to the database
        session.refresh(new_task)  # Refresh the task to load its ID from the database
        return new_task  # Return the created task
    
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of an error
        print("Exception:", e)  # Print the exception for debugging
        return None  # Return None if an error occurred
    finally:
        session.close()  # Ensure the session is closed after the operation

# Function to get all tasks for a specific user by user_id
def get_all_tasks(user_id: int):
    session = SessionLocal()  # Create a new session
    try:
        # Query all tasks that belong to the specified user
        tasks = session.query(Task).filter(Task.user_id == user_id).all()
        return tasks  # Return the list of tasks
    
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of an error
        print("Exception:", e)  # Print the exception for debugging
        return None  # Return None if an error occurred
    finally:
        session.close()  # Close the session after the operation

# Function to get a task by its ID and the user_id to ensure the task belongs to the user
def get_task_by_id(task_id: int, user_id: int):
    session = SessionLocal()  # Create a new session
    try:
        # Query for the task by task_id and user_id
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        return task  # Return the task if found, else None
    
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of an error
        print("Exception:", e)  # Print the exception for debugging
        return None  # Return None if an error occurred
    finally:
        session.close()  # Close the session after the operation

# Function to update a task's details
def update_task(task_id: int, title: str, description: str, completed: bool, user_id: int):
    session = SessionLocal()  # Create a new session
    try:
        # Query for the task by task_id and user_id
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        if not task:
            return None  # If the task doesn't exist, return None
        # Update the task details
        task.title = title
        task.description = description
        task.completed = completed
        session.commit()  # Commit the changes to the database
        session.refresh(task)  # Refresh the task object to get the updated data
        return task  # Return the updated task
    
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of an error
        print("Exception:", e)  # Print the exception for debugging
        return None  # Return None if an error occurred
    finally:
        session.close()  # Close the session after the operation

# Function to delete a task by its ID and user_id
def delete_task(task_id: int, user_id: int):
    session = SessionLocal()  # Create a new session
    try:
        # Query for the task by task_id and user_id
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        if not task:
            return None  # If the task doesn't exist, return None
        session.delete(task)  # Delete the task from the session
        session.commit()  # Commit the deletion to the database
        return True  # Return True if the task was successfully deleted
    
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of an error
        print("Exception:", e)  # Print the exception for debugging
        return None  # Return None if an error occurred
    finally:
        session.close()  # Close the session after the operation
