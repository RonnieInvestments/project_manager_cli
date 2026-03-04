# Project Management CLI

### Learning Goals

    -> Apply object-oriented programming (OOP) principles to model users, projects, and tasks.
    -> Use argparse to build a structured command-line interface.
    -> Implement JSON file persistence for saving and loading application data.
    -> Write unit tests using pytest to validate functionality.
    -> Structure a Python application using modular design principles.

### Introduction

In this lab, you will build a Project Management CLI Tool that allows users to manage projects and tasks from the command line. The system enables users to:

    -> Create and manage users.
    -> Create projects linked to users.
    -> Add tasks to projects.
    -> Update task status.
    -> Persist application data using JSON storage.

This lab demonstrates how to combine object-oriented design, CLI interaction, and data persistence to build a structured and maintainable Python application.

### Set up instructions

Clone the Repository

Navigate to your project directory.

Ensure Python is installed:
    python3 --version

Install Dependencies

Install pytest for testing:
    sudo apt install python3-pytest

To run the test suite:
    python3 -m pytest

### Tasks

### Task 1: Define the Problem

The goal of this lab is to build a Project Management CLI Tool that allows users to manage projects and tasks through the command line. The system must provide the following capabilities:

    -> Manage users.
    -> Create and link projects to users.
    -> Add tasks to projects.
    -> Update task status.
    -> Persist data using JSON files.
    -> Validate functionality using unit tests.

The key challenge is structuring the application using object-oriented programming, while maintaining clean separation between CLI logic, business logic, and storage.

### Task 2: Determine the Design

The Project Management CLI Tool is built using modular architecture:

    Models Layer: Defines core classes (User, Project, Task).
    CLI Layer: Handles user input and command parsing using argparse.
    Storage Layer: Manages JSON serialization and deserialization.
    Testing Layer: Uses pytest to validate functionality.

Design Breakdown:

    User Class: Stores user details and associated projects.
    Project Class: Stores project details and associated tasks.
    Task Class: Tracks task title and completion status.
    Storage Module: Serializes and reconstructs objects from JSON.
    CLI Interface: Connects user commands to application logic.

This structured design ensures the system is maintainable, testable, and modular.

### Task 3: Code Development

### Step 1: Implement the Models

Create classes for:
    -> User
    -> Project
    -> Task

Each class should:
    -> Store relevant attributes.
    -> Provide methods for adding related objects.
    -> Support serialization (to_dict) and reconstruction (from_dict).

### Step 2: Implement Storage Logic

In storage.py, implement:
    -> serialize() to convert objects to dictionaries.
    -> deserialize() to reconstruct objects and restore relationships.
    -> save_data() to write JSON to file.
    -> load_data() to read JSON from file.

Ensure project relationships are restored during deserialization.

### Step 3: Build the CLI

In main.py, use argparse to implement commands:

    -> add-user
    -> list-users
    -> add-project
    -> list-projects
    -> add-task
    -> list-tasks
    -> complete-task

Each command should:
    -> Load stored data.
    -> Execute model logic.
    -> Save updated data.

### Step 4: Implement Unit Tests

Create tests in the tests/ directory:

    -> test_models.py
    -> test_storage.py
    -> test_cli.py

Use pytest to validate:
    -> Model behavior.
    -> JSON serialization/deserialization.
    -> CLI command execution.

Run tests using:
    python3 -m pytest

All tests should pass.

### Best Practices for Managing Projects and Tasks

    -> Use separation of concerns between CLI, models, and storage.
    -> Encapsulate business logic within model classes.
    -> Validate input where necessary.
    -> Keep CLI focused on user interaction only.
    -> Use unit tests to ensure reliability.
    -> Document functionality clearly in README.

### Conclusion

By mastering:

    -> Object-Oriented Programming
    -> Command-Line Interfaces
    -> JSON Persistence
    -> Unit Testing

Developers can build structured, scalable, and maintainable command-line applications.

This lab demonstrates how to combine software design principles with practical implementation to create a fully functional Project Management CLI Tool.