# Glossary - Simple Definitions for Edge Carolina

**New to coding?** Don't worry! This glossary explains all the confusing words you'll see in a simple way.

---

## GitHub & Git Terms

**Repository (Repo)**
Think of this like a folder on the internet that holds all your code files. Everyone can see it and work on it together.

**Clone**
Making a copy of someone else's repository on your computer so you can work on it.

**Branch**
Like making a separate copy of your work so you can try new things without breaking the original. Your branch name should be `firstname-lastname` (like `john-smith`).

**Commit**
Saving a checkpoint of your work with a message describing what you changed. Like saving a game at a specific point.

**Push**
Uploading your saved work (commits) from your computer to GitHub so others can see it.

**Pull**
Downloading the latest changes from GitHub to your computer.

**Template**
A pre-made starting point for your project. Like a form with some parts already filled out.

**Fork**
Making your own copy of someone else's repository that you can freely change and push to.

---

## Python Terms

**Virtual Environment (venv)**
A separate space for your Python project that keeps its packages isolated from other projects. Like having a separate toolbox for each project.

**pip**
A tool that downloads and installs Python packages (like downloading apps from an app store).

**Module**
A file containing Python code that you can use in other files. Like importing a tool into your project.

**CLI (Command Line Interface)**
A way to run your program by typing commands instead of clicking buttons.

---

## Development Terms

**IDE**
Integrated Development Environment - fancy text editor for writing code (like VS Code, PyCharm, or Cursor).

**Terminal/Command Line**
The black window where you type commands to make your computer do things.

**Directory**
Another word for "folder" on your computer.

**Path**
The "address" of a file or folder on your computer (like `Documents/Projects/my-project`).

---

## Data Terms

**JSON (JavaScript Object Notation)**
A way to store data that both humans and computers can read easily. Like a digital filing cabinet.

**JSON in Python:**
```python
import json

# Convert Python data to JSON string
data = {"name": "John", "age": 25}
json_string = json.dumps(data)  # '{"name": "John", "age": 25}'

# Convert JSON string back to Python
python_data = json.loads(json_string)  # {'name': 'John', 'age': 25}

# Save to file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Load from file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
```

**Array/List**
A collection of items in order. Like a shopping list or a queue of people.

**Dictionary/Object**
A collection of key-value pairs. Like a real dictionary where you look up a word (key) to find its meaning (value).

**Data Structure**
A way to organize and store data so it can be used efficiently.

---

## HTML/Web Terms

**HTML (HyperText Markup Language)**
The language used to create web pages. Like the skeleton/structure of a website.

**Escaped Quotes/Characters**
When special characters need to be "escaped" with a backslash so they don't break the code:

```html
<!-- WRONG - this will break -->
<img src="image"title.jpg" alt="My Image">

<!-- RIGHT - escaped quote -->
<img src="image\"title.jpg" alt="My Image">

<!-- Or use single quotes -->
<img src='image"title.jpg' alt="My Image">
```

**HTML Attributes**
Extra information you add to HTML tags. Like `src="image.jpg"` or `alt="Description"`.

**HTML Entities**
Special codes for characters that have meaning in HTML:

- `&lt;` instead of `<`
- `&gt;` instead of `>`
- `&amp;` instead of `&`
- `&quot;` instead of `"`
- `&apos;` instead of `'`

---

## Testing Terms

**pytest**
A tool that automatically checks if your code works correctly by running tests.

**Test**
Code that checks if your main code works as expected. Like a practice quiz for your program.

**CI (Continuous Integration)**
Automatic checking that happens when you upload code to GitHub. It runs your tests to make sure everything works.

**Debugging**
Finding and fixing problems in your code. Like being a detective solving a mystery.

**Syntax**
The rules for writing code correctly. Like grammar rules for a programming language.

**Syntax Error**
When you break the rules of the programming language. Like writing a sentence with bad grammar.

**Logic Error**
When your code runs but doesn't do what you want it to do. The syntax is correct, but the thinking is wrong.

**Print Statement**
A way to show information while your program is running. Like leaving notes for yourself to see what's happening.

---

## Git Status & Workflow

**git status**
Shows you what's changed in your project. Like checking your shopping list before going to the store.

**Staged Changes**
Files you've marked as ready to be saved. Like putting items in your shopping cart.

**Unstaged Changes**
Files you've changed but haven't marked as ready to save yet. Like items still on your shopping list.

**Working Directory**
Your local project folder where you make changes.

**Repository/Repo**
Your project's home - can be local (on your computer) or remote (on GitHub).

**git log**
Shows the history of commits in your project. Like a timeline of all the changes made.

---

## File Extensions

**.py**
Python code file

**.md**
Markdown file (like this glossary) - used for documentation and README files

**.json**
JSON file - stores data in a structured way

**.txt**
Plain text file

---

## Common Commands Explained

**`git clone <url>`** - Download a copy of the repository to your computer

**`git checkout -b <branch-name>`** - Create and switch to a new branch

**`git add -A`** - Prepare all your changes to be saved

**`git commit -m "message"`** - Save your changes with a description

**`git push origin <branch-name>`** - Upload your branch to GitHub

**`python -m venv .venv`** - Create a virtual environment

**`source .venv/bin/activate`** - Turn on your virtual environment (Mac/Linux)

**`pip install -r requirements.txt`** - Install all the packages your project needs

**`pytest -q`** - Run all tests quietly

---

## Still Confused?

If you see a word that's not in this glossary, ask in the Edge Carolina Slack or come to office hours! We're here to help, and there are no stupid questions.

Remember: Every expert was once a beginner!
