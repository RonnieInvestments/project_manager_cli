# tests/test_models.py
# Tests object creation and relationships.

from models.user import User
from models.project import Project
from models.task import Task


def test_user_creation():
    # Verifies attributes and empty relationship.
    user = User(name="Ronaldo", email="ronaldo@email.com")

    assert user.name == "Ronaldo"
    assert user.email == "ronaldo@email.com"
    assert user.projects == []


def test_add_project_to_user():
    # User → Project relationship.
    user = User(name="Ronaldo")
    project = Project(title="CLI Tool", description="Test")

    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0].title == "CLI Tool"


def test_add_task_to_project():
    # Project → Task relationship.
    project = Project(title="CLI Tool")
    task = Task(title="Implement feature")

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Implement feature"


def test_complete_task():
    # Status change demonstrates behavior.
    task = Task(title="Write tests")

    task.status = "Complete"

    assert task.status == "Complete"