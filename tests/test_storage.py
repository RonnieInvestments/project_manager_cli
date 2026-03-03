# Tests JSON save/load and serialization.

import json
from storage import Storage
from models.user import User
from models.project import Project


def test_save_and_load(tmp_path):
    # Using tmp_path to avoid real filesystem side effects.
    # Isolate tests.

    filepath = tmp_path / "storage.json"
    storage = Storage(filepath=str(filepath))

    users = [User("Ronaldo", "ronaldo@email.com")]
    projects = [Project("CLI Tool", "Test")]

    data = storage.serialize(users, projects)
    storage.save_data(data)

    loaded = storage.load_data()

    assert "users" in loaded
    assert "projects" in loaded


def test_serialize_deserialize():
    # tests object → dict → object cycle.

    storage = Storage()

    users = [User("Ronaldo")]
    projects = [Project("CLI")]

    data = storage.serialize(users, projects)
    u, p = storage.deserialize(data) # Tuple unpacking
    # deserialize returns a tuple 
    # u -> users list
    # p -> projects list

    assert len(u) == 1
    assert len(p) == 1
    assert u[0].name == "Ronaldo"
    assert p[0].title == "CLI"