# Using subprocess -> allows one to spawn new processes, 
#                  -> connect to their input/output/error pipes, 
#                  -> and obtain their return codes. 
# subprocess.run(args, *, **other_popen_kwargs) -> python documentation
# This module intends to replace several older modules and functions
# Tests basic commands work and output is expected.

import subprocess
import os


def run(cmd):
    # Helper to run CLI command and return output.
    # The recommended approach to invoking subprocesses is to use the run() function for all use cases it can handle. 
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    # Captured stdout from the child process. 
    # A string if run() was called with an encoding, errors, or text=True. 
    # None if stdout was not captured.
    return result.stdout.strip()


def test_add_and_list_user():
    # Clean storage before test (simple isolation)
    if os.path.exists("data/storage.json"):
        os.remove("data/storage.json")

    # Add user
    run(["python3", "main.py", "add-user", "--name", "Ronaldo", "--email", "a@b.com"])

    # List users
    output = run(["python3", "main.py", "list-users"])

    assert "Ronaldo" in output


def test_add_project():
    if os.path.exists("data/storage.json"):
        os.remove("data/storage.json")

    run(["python3", "main.py", "add-user", "--name", "Alex"])

    # get user id (first user will be id=1)
    run(["python3", "main.py", "add-project", "--user-id", "1", "--title", "CLI"])

    output = run(["python3", "main.py", "list-projects", "--user-id", "1"])

    assert "CLI" in output