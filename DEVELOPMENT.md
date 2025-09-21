# Development Guide

**How to code, test, and debug your Edge Labs Ship 1 project**

---

## What You're Building

You're going to add cool new features to a simple app that keeps track of your daily notes (like a diary for coders!).

**What you'll learn:**
- How to work with dates and times in Python
- How to add new features to existing code
- More practice with Git and GitHub

---

## What You Need to Build

Look for **TODO comments** in the code - these tell you exactly what to add!

### Baseline (Everyone Must Do This)

**Goal:** Add timestamps to your entries so you know when you wrote them.

**Files to change:**
- `src/ship1/storage.py` - Look for `# TODO:` comments
- `src/ship1/cli.py` - Look for `# TODO:` comments

**What it should do:**
1. When you add an entry, it automatically includes the current date/time
2. When you list entries, it shows the timestamp
3. Format: "2024-01-15 14:30:25"

**Test it:**
```bash
python -m src.ship1 add "My first entry!"
python -m src.ship1 list
```
You should see your entry with a timestamp!

### Hard Mode (Optional Challenge)

**Goal:** Add delete and search features.

**What to add:**
1. **Delete entries by number:**
   ```bash
   python -m src.ship1 delete 2  # Removes the 2nd entry
   ```

2. **Search for entries:**
   ```bash
   python -m src.ship1 search "python"  # Finds entries with "python" in them
   ```

---

## Testing Your Work

**Run the automatic tests:**
```bash
pytest -q
```

**All tests should pass!**

**Test your features manually:**
```bash
# Test adding with timestamp
python -m src.ship1 add "Test entry"
python -m src.ship1 list

# Test hard mode (if you did it)
python -m src.ship1 delete 1
python -m src.ship1 search "test"
```

---

## Understanding the Code Structure

### Project Layout
```
ship1-template-python/
- src/ship1/
  - __init__.py
  - __main__.py     # Entry point for the app
  - cli.py          # Command line interface
  - storage.py      # Data storage functions
  - stats.py        # Statistics functions
- tests/
  - test_storage.py # Tests for storage functions
  - test_stats.py   # Tests for stats functions
- data/
  - log.json        # Where your data is stored
```

### Key Files Explained

**storage.py**
- Handles saving and loading your ship log entries
- Contains functions like `add_entry()`, `get_entries()`, etc.
- Uses JSON to store data in `data/log.json`

**cli.py**
- Handles command line commands (`add`, `list`, `delete`, `search`)
- Connects user input to storage functions
- Formats output for display

**__main__.py**
- Entry point that runs when you type `python -m ship1`
- Starts the CLI application

---

## How to Debug and Test Your Code

**Running tests:**
```bash
pytest -q
```
This runs all the test files and shows you if your code works.

**Understanding test failures:**
- Look for the red text - it tells you exactly what's wrong
- Common issues: function not found, wrong return value, syntax error
- Check the line number in the error message

**Debugging your code:**
1. Add `print()` statements to see what your code is doing:
   ```python
   def add_entry(message):
       print(f"Debug: Adding message: {message}")  # Add this to see what's happening
       # ... rest of your code
   ```

2. Test small pieces first:
   ```bash
   python -c "from src.ship1.storage import add_entry; add_entry('test')"
   ```

**Implementing TODO functions:**
1. Find the TODO comment in the code
2. Read the hint that comes after it
3. Look at similar functions in the same file for examples
4. Start with a simple version that works, then improve it

**Common testing errors:**
- `NameError`: You forgot to define a variable or import something
- `TypeError`: You're using the wrong type of data (string instead of list, etc.)
- `AttributeError`: You're trying to use a method that doesn't exist on that object

---

## Working with JSON Data

**JSON (JavaScript Object Notation)**
A way to store data that both humans and computers can read easily.

**JSON in Python:**
```python
import json

# Convert Python data to JSON string
data = {"name": "John", "age": 25}
json_string = json.dumps(data)  # '{"name": "John", "age": 25}'

# Convert JSON string back to Python
python_data = json.loads(json_string)  # {'name': 'John', 'age': 25}

# Save to file
with open('data/log.json', 'w') as f:
    json.dump(data, f)

# Load from file
with open('data/log.json', 'r') as f:
    loaded_data = json.load(f)
```

**Data Structures:**
- **Array/List**: A collection of items in order
- **Dictionary/Object**: Key-value pairs (like a real dictionary)
- **String**: Text data
- **Number**: Numeric data

---

## Coding Tips

### Reading Code
1. Start with the main entry point (`__main__.py`)
2. Follow the flow: CLI -> Storage -> Data
3. Look for TODO comments that tell you what to implement
4. Read existing functions to understand the pattern

### Writing Code
1. **Start simple**: Make it work first, then make it better
2. **Test frequently**: Run `pytest -q` after each change
3. **Use print statements** for debugging
4. **Look at examples**: Similar functions show you the pattern

### Common Patterns
```python
# Function that takes input and returns output
def process_data(input_data):
    # Do something with input_data
    result = input_data.upper()  # Example processing
    return result

# Function that reads from file
def load_data():
    try:
        with open('data/log.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist

# Function that saves to file
def save_data(data):
    with open('data/log.json', 'w') as f:
        json.dump(data, f, indent=2)  # indent=2 makes it readable
```

---

## What to Submit

1. **Your repository URL** (should look like: `https://github.com/YOUR-USERNAME/edge-f25-ship1-YOUR-NAME`)
2. **Your branch name** (should be `firstname-lastname`)
3. **Whether you did Baseline or Hard Mode**
4. **Any problems you ran into**

**Submit here:** [Google Form Link](https://forms.gle/uoAQkv48QDkEM81m9)

---

## Related Files

- **[SETUP.md](SETUP.md)** - How to set up your development environment
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Solutions to common problems
- **[GLOSSARY.md](GLOSSARY.md)** - Definitions of technical terms

---

## Need Help Understanding Code?

1. **Read the TODO comments** - they have hints!
2. **Look at similar functions** in the same file
3. **Use print statements** to see what's happening
4. **Check the [GLOSSARY.md](GLOSSARY.md)** for term definitions
5. **Ask in Slack** - we're here to help!

Remember: Coding is about solving problems step by step!
