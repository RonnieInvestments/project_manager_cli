# cli.py
# Handles command-line interaction.
# Uses argparse to parse commands.
# Calls storage and model methods.
# Separation of concerns: no business logic here.

import argparse
from storage import Storage
from models.user import User
from models.project import Project
from models.task import Task


def main():
    # CLI entry point.
    # Uses argparse to define subcommands.

    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # User commands
    # add-user
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=False)

    # list-users
    subparsers.add_parser("list-users")

    # Project command
    # add-project
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user-id", type=int, required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", required=False)

    # list-projects
    list_projects = subparsers.add_parser("list-projects")
    list_projects.add_argument("--user-id", type=int, required=False)

    # Task commands
    # add-task
    add_task = subparsers.add_parser("add-task")
    add_task.add_argument("--project-id", type=int, required=True)
    add_task.add_argument("--title", required=True)

    # list-tasks
    list_tasks = subparsers.add_parser("list-tasks")
    list_tasks.add_argument("--project-id", type=int, required=True)

    # complete-task
    complete_task = subparsers.add_parser("complete-task")
    complete_task.add_argument("--project-id", type=int, required=True)
    complete_task.add_argument("--task-id", type=int, required=True)

    args = parser.parse_args()

    storage = Storage()
    data = storage.load_data()
    users, projects = storage.deserialize(data)

    # Command logic
    if args.command == "add-user":
        user = User(name=args.name, email=args.email or "")
        users.append(user)

        data = storage.serialize(users, projects)
        storage.save_data(data)

        print(f"User added: {user}")

    elif args.command == "list-users":
        for user in users:
            print(user)

    elif args.command == "add-project":
        project = Project(
            title=args.title,
            description=args.description or ""
        )

        for user in users:
            if user.id == args.user_id:
                user.add_project(project)
                projects.append(project)
                break

        data = storage.serialize(users, projects)
        storage.save_data(data)

        print("Project added")

    elif args.command == "list-projects":
        if args.user_id:
            for user in users:
                if user.id == args.user_id:
                    for project in user.list_projects():
                        print(project)
        else:
            for project in projects:
                print(project)

    # Task logic
    elif args.command == "add-task":
        for project in projects:
            if project.id == args.project_id:
                task = Task(title=args.title)
                project.add_task(task)
                break

        data = storage.serialize(users, projects)
        storage.save_data(data)

        print("Task added")

    elif args.command == "list-tasks":
        for project in projects:
            if project.id == args.project_id:
                for task in project.list_tasks():
                    print(task)

    elif args.command == "complete-task":
        for project in projects:
            if project.id == args.project_id:
                for task in project.tasks:
                    if task.id == args.task_id:
                        task.status = "Completed"
                        break

        data = storage.serialize(users, projects)
        storage.save_data(data)

        print("Task marked as completed")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()