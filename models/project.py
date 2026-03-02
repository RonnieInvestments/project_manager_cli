from models.task import Task

class Project:

    id_counter = 1

    def __init__(self, title, description="", due_date=None, project_id=None):

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

        # project id logic
        if project_id is not None:
            self.id = project_id
        else:
            self.id = Project.id_counter
            Project.id_counter += 1

    # Adding task object to project
    def add_task(self, task):
        self.tasks.append(task)

    # Return lists of tasks -> useful for CLI display
    def list_tasks(self):
        return self.tasks
    
    # Convert project to dictionary for JSON storage
    def to_dict(self):
        
        tasks_list = []

        for task in self.tasks:
            tasks_list.append(task.to_dict())

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description, 
            "due_date": self.due_date,
            "tasks": tasks_list
        }
    
    # Recreating Project from dictionary -> used when loading JSON
    @classmethod
    def from_dict(cls, data):

        project = cls(
            title = data["title"],
            description = data.get("description", ""),
            due_date = data.get("due_date"),
            project_id = data["id"]
        )

        # Load tasks from dictionary
        for task_data in data.get("tasks", []):
            task = Task.from_dict(task_data)
            project.add_task(task)

        # Keep id counter ahead of loaded IDs
        if data["id"] >= cls.id_counter:
            cls.id_counter = data["id"] + 1

        return project
    
    # String representation
    def __str__(self):
        return f"[{self.id}] {self.title}: {self.description}"