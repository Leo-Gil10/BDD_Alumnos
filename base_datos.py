import json
import os
from typing import List, Dict, Optional

DB_FILENAME = "datos.json"


def _db_path() -> str:
    """Return the absolute path to the JSON database file in the current folder."""
    return os.path.join(os.path.dirname(__file__), DB_FILENAME)


def load_data() -> List[Dict]:
    """Load the list of personas from the JSON file. Returns an empty list if the file
    doesn't exist or is invalid."""
    path = _db_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # if file is corrupted or unreadable, return empty list
        return []


def save_data(data: List[Dict]) -> None:
    """Write the given list of personas back to the JSON file."""
    path = _db_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_person(nombre: str, edad: int) -> None:
    """Add a new persona record. This appends the entry and persists the database."""
    data = load_data()
    data.append({"nombre": nombre, "edad": edad})
    save_data(data)


def find_person(nombre: str) -> Optional[Dict]:
    """Search for a persona by nombre. Returns the record or None if not found."""
    data = load_data()
    for p in data:
        if p.get("nombre") == nombre:
            return p
    return None


def list_people() -> List[Dict]:
    """Return all persona records."""
    return load_data()


__all__ = ["load_data", "save_data", "add_person", "find_person", "list_people"]
