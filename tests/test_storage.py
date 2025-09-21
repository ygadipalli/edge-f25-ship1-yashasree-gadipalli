from pathlib import Path
from src.ship1.storage import add_entry, load_entries, clear_entries, data_path, delete_entry, search_entries
import os, json

def test_add_and_list(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("SHIP1_DATA_PATH", str(tmp_path / "log.json"))
    clear_entries()
    add_entry("alpha")
    add_entry("beta")
    entries = load_entries()
    assert len(entries) == 2
    assert entries[0]["v"] == "beta"  # newest first
    assert entries[1]["v"] == "alpha"

def test_clear(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("SHIP1_DATA_PATH", str(tmp_path / "log.json"))
    add_entry("x")
    assert load_entries()
    clear_entries()
    assert load_entries() == []

def test_delete_entry(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("SHIP1_DATA_PATH", str(tmp_path / "log.json"))
    clear_entries()
    add_entry("first")
    add_entry("second")
    add_entry("third")
    
    # Delete middle entry (index 2)
    assert delete_entry(2)
    entries = load_entries()
    assert len(entries) == 2
    assert entries[0]["v"] == "third"  # newest first
    assert entries[1]["v"] == "first"
    
    # Try to delete non-existent entry
    assert not delete_entry(5)

def test_search_entries(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("SHIP1_DATA_PATH", str(tmp_path / "log.json"))
    clear_entries()
    add_entry("Python programming")
    add_entry("JavaScript coding")
    add_entry("Python data science")
    
    # Search for Python entries
    results = search_entries("python")
    assert len(results) == 2
    assert all("python" in result["v"].lower() for result in results)
    
    # Search for non-existent term
    results = search_entries("java")
    assert len(results) == 1
    assert "JavaScript" in results[0]["v"]
