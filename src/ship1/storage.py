"""Storage helpers for Ship Log with enhanced features.
Functions here should read/write JSON entries at data/log.json.
Each entry is a dict: { "t": ISO_TIMESTAMP, "v": TEXT }.
Newest entries should come first in the list.

Enhanced features:
- Better timestamp formatting
- Delete entries by index
- Search entries by text content

Tips:
- Create the parent folder if it doesn't exist.
- Keep writes idempotent: always write the full array to disk.
- Use environment variable SHIP1_DATA_PATH to override the default path.
"""
from __future__ import annotations
import json, os, time
from pathlib import Path
from typing import List, Dict

REPO_ROOT = Path(__file__).resolve().parents[2]

def _default_data_path() -> Path:
    env = os.environ.get("SHIP1_DATA_PATH")
    if env:
        return Path(env)
    return REPO_ROOT / "data" / "log.json"

def data_path() -> Path:
    """Return the Path to the JSON log file, creating the folder/file if needed."""
    p = _default_data_path()
    # Create parent folder if it doesn't exist
    p.parent.mkdir(parents=True, exist_ok=True)
    # Create file with empty array if it doesn't exist
    if not p.exists():
        p.write_text("[]", encoding="utf-8")
    return p

def load_entries() -> List[Dict]:
    """Return a list of entries (newest first)."""
    p = data_path()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_entries(data: List[Dict]) -> None:
    """Write the full list back to disk (pretty-printed JSON)."""
    p = data_path()
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")

def add_entry(text: str) -> None:
    """Insert a new entry at the start of the list with current timestamp."""
    # TODO: Implement enhanced timestamp formatting
    # - Use time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) for readable format
    # - Create new_entry dict with "t" (timestamp) and "v" (text) keys
    # - Insert at beginning of entries list (newest first)
    # - Save the updated entries
    raise NotImplementedError

def clear_entries() -> None:
    """Erase all entries (write an empty list)."""
    save_entries([])

def delete_entry(index: int) -> bool:
    """Delete an entry by its 1-based index. Returns True if successful."""
    # TODO: Implement delete functionality
    # - Load current entries
    # - Check if index is valid (1 <= index <= len(entries))
    # - If valid: remove entry at index-1 (convert to 0-based), save, return True
    # - If invalid: return False
    raise NotImplementedError

def search_entries(query: str) -> List[Dict]:
    """Search for entries containing the query text (case-insensitive)."""
    # TODO: Implement search functionality
    # - Load current entries
    # - Convert query to lowercase for case-insensitive search
    # - Filter entries where query appears in entry["v"] (also lowercase)
    # - Return list of matching entries
    raise NotImplementedError
