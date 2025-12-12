# src/core/database.py
import json
import os
from threading import Lock

DB_DIR = "db"
_lock = Lock()

def _path(name):
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
    return os.path.join(DB_DIR, f"{name}.json")

def load_db(name):
    path = _path(name)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_db(name, data):
    path = _path(name)
    with _lock:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def next_id(name):
    items = load_db(name)
    return 1 if not items else max(item.get("id",0) for item in items) + 1
