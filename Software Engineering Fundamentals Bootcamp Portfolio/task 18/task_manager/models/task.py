
class Task:
    """
    Class representing a Task entity with attributes:
    task_id, title, description, status
    """

    highest_task_id = 0  # Class variable to keep track of the highest task ID

    def __init__(self, title: str, description: str):
        self.task_id = None
        self.title = title
        self.description = description
        self.status = "Not Started"

    def mark_completed(self):
        self.status = "Finished"

    def assign_task_id(self, new_id):
        self.task_id = new_id

    def __repr__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.status}"

    @classmethod
    def from_string(cls, task_string: str):
        task_id, title, description, completed = task_string.strip().split(', ')
        is_completed = (completed == 'True')
        task = cls(title=title, description=description)
        task.task_id = int(task_id)
        if is_completed:
            task.mark_completed()
        return task
