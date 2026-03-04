# class Task represents a single task inside a project (stores task data, manages its status, convert itself
#   to/from dictionary-> for JSON storage)
# The class does not handle file I/O or CLI input  

class Task:

    # Id counter variable to help auto-generate id
    id_counter = 1

    # Constructor method to initialize the class
    def __init__(self, title, assigned_to=None, task_id=None, status="Incomplete"):

        self.title = title
        self._status = status
        self.assigned_to = assigned_to

        # Id logic
        if task_id is not None:
            self.id = task_id
        else:
            self.id = Task.id_counter
            Task.id_counter += 1
    
    # Encapsulation
    @property
    def status(self): # getter for task status (prevents direct modification)
        return self._status
    
    @status.setter
    def status(self, new_status):
        # setter with validation, only allows "Incomplete" or "Complete"
        if new_status in ["Incomplete", "Complete"]:
            self._status = new_status
        else:
            raise ValueError("Status must be 'Incomplete' or 'Complete'")
        
    # Business logic
    def mark_complete(self):
        # marks tasks as complete, uses property setter for validation
        self.status = "Complete"

    # Task storage
    def to_dict(self): # convert Task object to dictionary for JSON storage
        return {
            "id": self.id,
            "title": self.title,
            "status": self._status,
            "assigned_to": self.assigned_to
        }
    
    @classmethod
    def from_dict(cls, data):
        # recreates Task object from dictionary -> loading JSON
        task = cls(
            title = data["title"],
            assigned_to = data.get("assigned_to"),
            task_id = data["id"],
            status = data.get("status", "Incomplete")
        )

        # keep ID counter ahead of loaded IDs
        if data["id"] >= cls.id_counter:
            cls.id_counter = data["id"] + 1

        return task
    
    # String representation
    def __str__(self):
        
        assigned = "Unassigned"

        if self.assigned_to:
            assigned = self.assigned_to
            
        return f"[{self.id}] {self.title} - {self._status} (Assigned to: {assigned})"
