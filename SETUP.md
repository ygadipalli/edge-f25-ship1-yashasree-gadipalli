# Setup Guide

**Detailed setup instructions for Edge Carolina Ship 1**

---

## Quick Git Setup (Do This First!)

**Skip this step if Git already works for you!**

Many students get stuck because Git isn't set up with the right name and email. Let's fix that:

### Check if Git is already configured:
```bash
git config --global user.name
git config --global user.email
```

### If you see nothing or wrong information, set it up:
```bash
# Use your real name
git config --global user.name "Your Full Name"

# Use your UNC email (like firstname_lastname@unc.edu)
git config --global user.email "yourname@unc.edu"
```

**Examples:**
```bash
git config --global user.name "Will Zellers"
git config --global user.email "willzellers@unc.edu"
```

### Verify it worked:
```bash
git config --global user.name
git config --global user.email
```

**You should see your name and UNC email!**

---

## Step 1: Get Your Own Copy (Using GitHub Template)

**IMPORTANT:** Follow these steps EXACTLY to avoid permission problems!

### Option A: Use GitHub Template (Recommended for beginners)

1. **Go to this repository on GitHub** (the link your instructor gave you)

2. **Click the green "Use this template" button** at the top of the page

3. **Create your repository:**
   - Repository name: `edge-f25-ship1-<your-firstname-lastname>`
     (Example: `edge-f25-ship1-john-smith`)
   - Make sure it's **Public** (not private!)
   - Click "Create repository"

4. **You now have your own copy!** GitHub will take you to YOUR new repository.

### Option B: Fork the Repository (Alternative)

1. Click the **"Fork"** button at the top-right of the template repository
2. This creates your own copy that you can push to
3. Name it: `edge-f25-ship1-<your-firstname-lastname>`

---

## Step 2: Download Your Copy to Your Computer Using Your IDE

**Don't know what these words mean?** Check the [GLOSSARY.md](GLOSSARY.md) file!

### Using VS Code (Recommended):
1. **Open VS Code**
2. **Go to File > Open Folder** and create/select a folder for your projects (like `Desktop/Projects`)
3. **Click the Source Control icon** on the left sidebar (looks like a branch)
4. **Click "Clone Repository"**
5. **Enter your repository URL:**
   ```
   https://github.com/YOUR-USERNAME/edge-f25-ship1-YOUR-FIRSTNAME-LASTNAME.git
   ```
   **Replace YOUR-USERNAME and YOUR-FIRSTNAME-LASTNAME with your actual info!**

6. **Choose where to save it** and click "Select Repository Location"
7. **VS Code will download your repository** and ask if you want to open it
8. **Click "Open"** to start working

### Using Cursor IDE:
1. **Open Cursor**
2. **Go to File > Clone Repository**
3. **Enter your repository URL:**
   ```
   https://github.com/YOUR-USERNAME/edge-f25-ship1-YOUR-FIRSTNAME-LASTNAME.git
   ```
   **Replace YOUR-USERNAME and YOUR-FIRSTNAME-LASTNAME with your actual info!**
4. **Choose where to save it** and click "Clone"
5. **Cursor will download and open your repository**

### After Cloning - Create Your Branch:
Once your repository is open in your IDE:

1. **Look for the Source Control panel** (usually on the left)
2. **Click the branch icon** or look for branch options
3. **Create a new branch** named `firstname-lastname`
   - **Use YOUR actual first and last name! (Example: `john-smith`)**
4. **Switch to your new branch**

**What's a branch?** Think of it like this:
- **main** (or master) = The "official" version of the code (don't touch this!)
- **your branch** (like `grace-zhang`) = Your personal workspace where you make changes
- You can experiment on your branch without breaking the main project
- When you're done, your branch gets merged back into main

**Tip:** Your IDE will show you which branch you're on in the bottom-left corner!

---

## Step 3: Set Up Your Coding Environment

**What's a virtual environment?** It's like a separate workspace for your project. Check [GLOSSARY.md](GLOSSARY.md) for more info!

1. **Create your virtual environment:**
   ```bash
   python3 -m venv .venv
   ```

2. **Activate it:**

   **On Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```

   **On Windows:**
   ```bash
   .\.venv\Scripts\activate
   ```

   **You should see `(.venv)` at the start of your terminal line now!**

3. **Install the packages you need:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test that everything works:**
   ```bash
   python -m src.ship1 --help
   ```

   **You should see help text appear!**

---

## Step 4: Save Your Work

**Save your changes to GitHub:**

1. **Check what you changed:**
   ```bash
   git status
   ```

2. **Add all your changes:**
   ```bash
   git add -A
   ```

3. **Save with a message:**
   ```bash
   git commit -m "Ship 1: Added timestamp feature"
   ```

   **Write a message that explains what you did!**

4. **Upload to GitHub:**
   ```bash
   git push origin firstname-lastname
   ```

   **Use YOUR actual branch name!**

---

## Need Help?

- Check the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) file for common issues
- Still stuck? Ask in the Edge Carolina Slack or come to office hours
- Remember: Every expert was once a beginner!

---

## Ready for Development?

Once setup is complete, head to [DEVELOPMENT.md](DEVELOPMENT.md) to start coding!

**Quick test to make sure everything works:**
```bash
python -m src.ship1 --help
```

If you see help text, you're all set!
