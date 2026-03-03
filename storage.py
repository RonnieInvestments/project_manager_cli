import json
import os

from models.user import User
from models.project import Project
from models.task import Task

class Storage:
    # Handle loading and saving data to JSON
    # No business logic
    def __init__(self, filepath="data/storage.json"):
        self.filepath = filepath

    def load_data(self):
        # Load data from JSON
        # Missing file -> return empty structure/ None
        if not os.path.exists(self.filepath):
            return {
                "users": [],
                "projects": [], 
                "tasks": []
            }
        
        with open(self.filepath, "r") as file:
            return json.load(file)
        
        # Save data dictionary to JSON file
        # Create directory if missing
    def save_data(self, data):
        directory = os.path.dirname(self.filepath)

        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(self.filepath, "w") as file:
            json.dump(data, file, indent=4)
            file.write("\n")

    # Conversions
    # Serialize ->  converting an object into a format that can be easily stored or transmitted
    def serialize(self, users, projects):
        # objects -> dictionary
        users_list = []
        projects_list = []

        for user in users:
            users_list.append(user.to_dict())

        for project in projects:
            projects_list.append(project.to_dict())

        return {
            "users": users_list,
            "projects": projects_list
        }
    
    # deserialize -> reconstructing the object from its serialized form
    def deserialize(self, data):
        # dictionaries -> objects
        users = []
        projects = []

        # First create project objects
        for project_data in data.get("projects", []):
            projects.append(Project.from_dict(project_data))

        # Then create user objects and link projects
        for user_data in data.get("users", []):

            user = User.from_dict(user_data)

            # Link project IDs to project objects
            for project_id in user_data.get("projects", []):

                for project in projects:
                    if project.id == project_id:
                        user.add_project(project)

            users.append(user)

        return users, projects
