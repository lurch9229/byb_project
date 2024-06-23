import os

from models.task import Task
from dataclasses import dataclass


@dataclass
class Credentials:
    username: str
    password: str
    role: str


class TaskHandler:

    def __init__(self):
        self.unfinished_tasks = None
        self.tasks = []

        cur_dir = os.path.dirname(__file__)
        self.TASKS_FILE = os.path.join(cur_dir, "tasks.txt")

        self.load_tasks()

    """
    Load the tasks from the text file
    return tasks in the tasks list
    """
    def load_tasks(self):
        os.makedirs(os.path.dirname(self.TASKS_FILE), exist_ok=True)

        try:
            with open(self.TASKS_FILE, "r") as file:
                content = file.read()

                if content == "":
                    req_new_task = input(
                        "No tasks on record. Would you like to create one? y/n: "
                    )
                    if req_new_task == "y":
                        self.create_new_task()

                    elif req_new_task == "n":
                        return

                    else:
                        raise ValueError("Input Error. Please enter y or n")
                else:
                    file.seek(0)
                    for line in file.readlines():
                        task = Task.from_string(line.strip())

                        if task:
                            self.tasks.append(task)
                            Task.highest_task_id = max(
                                Task.highest_task_id, task.task_id
                            )

        except FileNotFoundError:
            print("Creating tasks.txt")
            with open(self.TASKS_FILE, "w"):
                self.create_new_task()

        return self.tasks

    """
    Diplays the tasks found in tasks list
    """
    def display_tasks(self):
        if not self.tasks:
            req_new_task = input(
                "No tasks on record. Would you like to create one? y/n: "
            )
            if req_new_task == "y":
                self.create_new_task()

            elif req_new_task == "n":
                return

            else:
                raise ValueError("Input Error. Please enter y or n")

        for task in self.tasks:
            print(task)
        print("\n")

    """
    Displays task based on task_id
    """
    def load_task_by_id(self, task_id: int):
        try:
            with open(self.TASKS_FILE, "r") as file:
                for line in file:
                    task = Task.from_string(line)
                    if task.task_id == task_id:
                        return task

        except FileNotFoundError:
            with open(self.TASKS_FILE, "w"):
                pass

        raise ValueError(f"Task with ID {task_id} not found")

    """
    Saves any changes made to the tasks into the text file
    """
    def save_tasks(self):
        with open(self.TASKS_FILE, "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    """
    Create a new task. Takes input from user for title and description
    The id and status are handled by the Task class
    """
    def create_new_task(self):
        title = input("Enter the task's title: ")
        description = input("Enter the task's description: ")
        self.add_task(Task(title=title, description=description))
        print("Task successfully added")

    def add_task(self, new_task):
        """
        Checks the current highest ID to set a new one for the new task
        Takes new task title and description in the new_task var
        Adds new task to text file and saves changes
        """
        try:
            if self.tasks:
                highest_task_id = max(task.task_id for task in self.tasks)
            else:
                highest_task_id = 0

            new_task_id = highest_task_id + 1
            new_task.assign_task_id(new_task_id)
            self.tasks.append(new_task)
            self.save_tasks()
            print("Task added successfully")

        except Exception as e:
            print(f"Error adding task: {e}")

    """
    Edit the task based on task_id.
    Can update the Title, Description and Status
    """
    def update_task(self, task_id):
        found_task = None

        for task in self.tasks:
            if task.task_id == task_id:
                found_task = task
                break

        if found_task:
            while True:
                print(f"How would you like to update task {task_id}?: ")
                print(
                    "1. Update Title\n"
                    "2. Update Description\n"
                    "3. Update Status\n"
                    "4. Return to Tasks Menu"
                )

                request_update = input("Please enter a number: ")

                if request_update == "1":
                    new_title = input(f"Please Enter a new title for task {task_id}: ")
                    found_task.title = new_title

                elif request_update == "2":
                    new_description = input(
                        f"Please Enter a new decription for task {task_id}: "
                    )
                    found_task.description = new_description

                elif request_update == "3":
                    new_status = input(
                        f"Please Enter a new status for task {task_id}: "
                        "Not Started/Ongoing/Finished: "
                    )
                    found_task.status = new_status

                elif request_update == "4":
                    print("Returning to Tasks Menu.\n")
                    break

                else:
                    print(f"Task with ID {task_id} not found \n")
                    return

            self.save_tasks()
            print(f"Task {task_id} Updated")

    """
    Delete a task based on task_id
    """
    def delete_task(self, task_id):
        found_task = None

        for task in self.tasks:
            if task.task_id == task_id:
                found_task = task
                break

        if found_task:
            print(
                f"{found_task.task_id}, {found_task.title}, {found_task.description}, {found_task.status}"
            )
            print("Enter 'yes' to delete this task")
            confirm_delete = input().lower()

            if confirm_delete == "yes":
                self.tasks.remove(found_task)
                self.save_tasks()
                print(f"Task {task_id} deleted")

            else:
                print("Cancelled task deletion")

        else:
            print(f"Task with ID {task_id} not found")
