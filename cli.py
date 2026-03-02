# cli.py
# Handles command-line interaction.
# Uses argparse to parse commands.
# Calls storage and model methods.
# Separation of concerns: no business logic here.

import argparse
from storage import Storage
from models.user import User
from models.project import Project


def main():
    '''
    CLI entry point.
    Uses argparse to define subcommands.
    '''

    # ArgumentParser handles CLI input and help messages.
    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    # Subparsers allow multiple commands.
    # Each command has its own arguments.
    subparsers = parser.add_subparsers(dest="command")

    # add-user command
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=False)

    # list-users command
    subparsers.add_parser("list-users")

    # add-project command
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user-id", type=int, required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", required=False)

    # list-projects command
    list_projects = subparsers.add_parser("list-projects")
    list_projects.add_argument("--user-id", type=int, required=False)

    # Parse CLI arguments into args object.
    # args.command tells us which subcommand was used.
    args = parser.parse_args()

    # Initialize storage and load existing data.
    # Persistence: data is loaded before modification.
    storage = Storage()
    data = storage.load_data()

    # Deserialize dictionaries into objects.
    # users and projects become Python objects.
    users, projects = storage.deserialize(data)

    # Command handling
    # Each branch handles a specific command.
    # After modification, data is serialized and saved.

    if args.command == "add-user":
        # Create User object from CLI input.
        user = User(name=args.name, email=args.email or "")

        # Add user to collection.
        users.append(user)

        # Save updated data.
        data = storage.serialize(users, projects)
        storage.save_data(data)

        print(f"User added: {user}")

    elif args.command == "list-users":
        # Display all users.
        # __str__ method of User is used for output.
        for user in users:
            print(user)

    elif args.command == "add-project":
        # Create Project object.
        project = Project(
            title=args.title,
            description=args.description or ""
        )

        # Link project to user (one-to-many relationship).
        # Find user by ID and add project.
        for user in users:
            if user.id == args.user_id:
                user.add_project(project)
                projects.append(project)
                break

        # Save changes.
        data = storage.serialize(users, projects)
        storage.save_data(data)

        print("Project added")

    elif args.command == "list-projects":
        # If user-id provided, list only that user's projects.
        # Otherwise, list all projects.
        if args.user_id:
            for user in users:
                if user.id == args.user_id:
                    for project in user.list_projects():
                        print(project)
        else:
            for project in projects:
                print(project)

    else:
        # No valid command → show help.
        parser.print_help()