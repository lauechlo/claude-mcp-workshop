# 🚀 GitHub Setup Guide for First-Time Users

This guide will walk you through creating your GitHub repository for this workshop project.

## Prerequisites

- A GitHub account (create one at [github.com](https://github.com/join) if you don't have one)
- Git installed on your computer
  - Check: `git --version`
  - Install: [git-scm.com/downloads](https://git-scm.com/downloads)

---

## Part 1: Create Your Repository on GitHub

### Step 1: Go to GitHub

1. Log in to [github.com](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**

### Step 2: Configure Your Repository

Fill in the form:

**Repository name:**
```
spotify-mcp-workshop
```
(or any name you prefer - use lowercase with hyphens)

**Description:**
```
MCP Music Server for Claude - AI@Princeton Workshop Demo
```

**Visibility:**
- ✅ Choose **Public** (so participants can access it)

**Initialize this repository:**
- ❌ **Do NOT check** "Add a README file"
- ❌ **Do NOT check** "Add .gitignore"
- ❌ **Do NOT check** "Choose a license"

(We'll add these from your local folder)

Click **"Create repository"**

### Step 3: Note Your Repository URL

After creation, you'll see a page with repository URLs. Note the HTTPS URL:
```
https://github.com/YOUR_USERNAME/spotify-mcp-workshop.git
```

---

## Part 2: Prepare Your Local Folder

### Step 1: Navigate to Your Repo Folder

Open Terminal (Mac/Linux) or PowerShell (Windows) and navigate to your new clean repository folder:

```bash
cd path/to/your/repo-folder
```

### Step 2: Verify Files

Make sure your repo folder contains ONLY the safe files:

**Should be present:**
- `.env.example`
- `.gitignore`
- `README.md`
- `SETUP.md`
- `QUICKSTART.md`
- `EXAMPLES.md`
- `ADVANCED_ANALYSIS.md`
- `CONTRIBUTING.md`
- `TOOLS_REFERENCE.md`
- `SPOTIFY_SETUP.md`
- `LICENSE`
- `requirements.txt`
- `music_server_updated_2025.py`
- `analyze_songs.py` (cleaned version)
- `spotify_cli.py` (cleaned version)
- `test_mcp_server.py` (cleaned version)
- `csv_to_json.py`
- `claude_desktop_config.json.example`
- `rsvp_songs.csv` (optional example data)

**Should NOT be present:**
- `.env` or `_env`
- `.cache` or `_cache`
- `claude_desktop_config.json` (with real credentials)
- Any versions with hardcoded credentials

---

## Part 3: Initialize Git and Push to GitHub

### Step 1: Initialize Git

```bash
# Initialize git in your folder
git init

# Check status (should show all your files as untracked)
git status
```

### Step 2: Stage Your Files

```bash
# Add all files (the .gitignore will automatically exclude sensitive files)
git add .

# Verify what will be committed
git status
```

**Important:** Make sure `.env`, `.cache`, and `claude_desktop_config.json` are NOT in the list!

### Step 3: Make Your First Commit

```bash
# Create your first commit
git commit -m "Initial commit: MCP Music Server for workshop"
```

### Step 4: Connect to GitHub

```bash
# Add your GitHub repository as the remote
git remote add origin https://github.com/YOUR_USERNAME/spotify-mcp-workshop.git

# Verify it was added
git remote -v
```

Replace `YOUR_USERNAME` with your actual GitHub username!

### Step 5: Push to GitHub

```bash
# Push your code to GitHub
git branch -M main
git push -u origin main
```

You may be prompted to enter your GitHub credentials:
- **Username:** Your GitHub username
- **Password:** Use a [Personal Access Token](https://github.com/settings/tokens), NOT your regular password

---

## Part 4: Verify Everything Worked

### Check on GitHub

1. Go to `https://github.com/YOUR_USERNAME/spotify-mcp-workshop`
2. You should see all your files
3. Click through a few to verify content looks correct
4. **IMPORTANT:** Check that `.env` and `.cache` files are NOT visible on GitHub

### Security Double-Check

Make sure these are NOT visible on GitHub:
- ❌ `.env` file
- ❌ `_env` file
- ❌ `.cache` file
- ❌ `_cache` file
- ❌ `claude_desktop_config.json` (without .example)
- ❌ Any files with your actual Spotify credentials

If you accidentally committed sensitive files:
1. **Immediately** revoke your Spotify credentials at [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Generate new credentials
3. Follow [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) to remove them from Git history

---

## Part 5: Share with Workshop Participants

### Update Your Workshop Instructions

Share this URL with participants:
```
https://github.com/YOUR_USERNAME/spotify-mcp-workshop
```

They can clone it with:
```bash
git clone https://github.com/YOUR_USERNAME/spotify-mcp-workshop.git
cd spotify-mcp-workshop
```

Then they'll follow the setup instructions in `QUICKSTART.md`.

---

## Making Updates Later

### When You Make Changes

```bash
# Check what changed
git status

# Add specific files or all changes
git add filename.py
# or
git add .

# Commit with a descriptive message
git commit -m "Add new feature: X"

# Push to GitHub
git push
```

### Common Git Commands

```bash
# See what changed
git status
git diff

# View commit history
git log --oneline

# Undo uncommitted changes to a file
git checkout -- filename.py

# Create a new branch for testing
git checkout -b test-feature
git checkout main  # switch back to main
```

---

## Troubleshooting

### "fatal: not a git repository"

Make sure you ran `git init` in the correct folder.

### "Permission denied (publickey)"

You need to set up SSH keys or use HTTPS with a Personal Access Token:
- HTTPS: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- SSH: [Adding a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

### "Updates were rejected because the remote contains work"

```bash
# Pull first, then push
git pull origin main --rebase
git push
```

### "I accidentally committed sensitive files!"

1. **Immediately** revoke those credentials
2. Generate new credentials
3. Remove from git history:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   git push origin --force --all
   ```
4. Or easier: Delete the repository and start fresh with a clean folder

---

## Additional Resources

- [GitHub Docs](https://docs.github.com)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Desktop](https://desktop.github.com/) - GUI alternative to command line
- [Oh My Git!](https://ohmygit.org/) - Fun way to learn Git

---

## Questions?

- Check the [GitHub Community](https://github.community/)
- Ask in the AI@Princeton Discord
- GitHub's [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

Good luck with your repository! 🎉
