# Troubleshooting Guide

**Common issues and solutions for Edge Carolina Ship 1**

---

## Permission Denied Issues

### "Permission denied" when pushing
- **This is normal if you cloned the original template!**
- Use the "GitHub Template" method in [SETUP.md](SETUP.md) instead
- Or ask for help in Slack

### "remote: Permission to Edge-Carolina/ship0-template-python.git denied"
- You're trying to push to the original template (which you can't modify)
- Create your own repository using the GitHub template method
- Then push to your own repository

---

## Command Line Issues

### "Command not found" errors
- Make sure your virtual environment is active (you should see `(.venv)`)
- Try `python3` instead of `python`
- On Windows, try `py` instead of `python`

### "ModuleNotFoundError" or import errors
- Ensure your virtual environment is activated
- Try reinstalling packages: `pip install -r requirements.txt`
- Check that you're in the right directory (should contain `src/` folder)

---

## Git Issues

### Git is asking for wrong email/username
- Run the setup commands in [SETUP.md](SETUP.md)
- Check your Git config: `git config --global user.email`

### "fatal: not a git repository"
- Make sure you're inside your project folder
- Try `git status` to confirm you're in a Git repository

### Branch name issues
- Your branch should be `firstname-lastname` (no spaces)
- Example: `grace-zhang` not `grace zhang` or `Grace-Zhang`

---

## IDE Issues

### VS Code / IDE issues
- Make sure your virtual environment is selected in your IDE
- Try running commands in the terminal instead
- Close and reopen your IDE

### IDE Setup and Git Integration

**Setting up VS Code for this project:**
1. Open your project folder in VS Code
2. VS Code should ask if you want to select the Python interpreter - choose the one from your `.venv` folder
3. Install the Python extension if prompted
4. You should see `(.venv)` in the bottom-right corner

**Using Git in VS Code:**
1. Look for the "Source Control" icon on the left sidebar (looks like a branch)
2. Click it to see your changes
3. Click the `+` button next to changed files to stage them
4. Type a commit message at the top
5. Click the checkmark to commit
6. Click the "..." menu and choose "Push" to upload to GitHub

**Can't find the Git integration?**
- Make sure Git is installed on your computer
- Try running `git --version` in terminal to check
- Restart VS Code
- Look for "Git: Enabled" in VS Code settings

**Cursor IDE users:**
- Cursor has built-in AI help - ask it questions about your code!
- The Git integration works the same as VS Code

---

## Testing Issues

### Tests are failing
- Read the error message carefully
- Check that you filled in ALL the TODO comments
- Ask for help in Slack with a screenshot

### "pytest command not found"
- Make sure your virtual environment is activated
- Try `python -m pytest` instead of just `pytest`

---

## Debugging Your Code

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

## HTML Issues (For Node.js Track)

### Escaped quotes in HTML
```html
<!-- WRONG - this will break -->
<img src="image"title.jpg" alt="My Image">

<!-- RIGHT - escaped quote -->
<img src="image\"title.jpg" alt="My Image">

<!-- Or use single quotes -->
<img src='image"title.jpg' alt="My Image">
```

### HTML entities
- `&lt;` instead of `<`
- `&gt;` instead of `>`
- `&amp;` instead of `&`
- `&quot;` instead of `"`
- `&apos;` instead of `'`

---

## Still Having Issues?

### "I don't understand the code"
- Look at the [GLOSSARY.md](GLOSSARY.md) file for definitions
- Read the TODO comments carefully - they have hints
- Ask questions in Slack

### Git is confusing
- Check the [GLOSSARY.md](GLOSSARY.md) file
- Come to office hours - we're here to help!
- Remember: everyone struggles with Git at first!

### Need more help?
1. **Check the [GLOSSARY.md](GLOSSARY.md) file** - it explains confusing words
2. **Ask in Slack** - your labmates and Exec Team are there to help
3. **Come to office hours** - we love helping people debug their code
4. **Don't give up!** - every expert was once a beginner

---

## Get Help

**Quick ways to get help:**
- **Slack**: Ask in the Edge Carolina channel
- **Office Hours**: Come to instructor office hours
- **Classmates**: Many have solved the same issues

**Before asking for help, please include:**
- What error message you're seeing (copy/paste it)
- What command you were trying to run
- What operating system you're using (Mac/Windows)
- A screenshot if it's a visual issue

This helps us help you faster!
