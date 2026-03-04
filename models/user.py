from models.project import Project

class User:

    id_counter = 1

    def __init__(self, name, email="", user_id=None):
        self.name = name
        self.email = email
        self.projects = []

        if user_id is not None:
            self.id = user_id
        else:
            self.id = User.id_counter
            User.id_counter += 1

    # Adds a project to this user
    def add_project(self, project):
        self.projects.append(project)

    # Listing projects
    def list_projects(self):
        return self.projects
    
    # JSON logic (dictionary conversions)
    # Convert user to dictionary 
    # Store projects by ID (not full object) -> avoids recursion
    def to_dict(self):
        projects_list = []

        for project in self.projects:
            projects_list.append(project.id)

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": projects_list
        }
    
    @classmethod
    def from_dict(cls, data):
        # recreates User from dictionary

        user = cls(
            name = data["name"],
            email = data.get("email", ""),
            user_id = data["id"]
        )

        # Keep ID counter ahead of loaded IDs -> Data integrity (prevent duplicate IDs)
        # Each new object increases counter
        if data["id"] >= cls.id_counter:
            cls.id_counter = data["id"] + 1

        return user
    
    # String representation
    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email})"
