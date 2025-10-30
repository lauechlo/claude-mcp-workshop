# 📁 Quick File Copy Guide

## Step 1: Create Your Repo Folder

```bash
# Create a new folder for your clean repository
mkdir ~/spotify-mcp-workshop-repo
cd ~/spotify-mcp-workshop-repo
```

---

## Step 2: Copy Safe Files (Direct Copy)

Copy these files AS-IS from your working directory:

### Documentation
```bash
cp ~/path/to/working/dir/README.md .
cp ~/path/to/working/dir/QUICKSTART.md .
cp ~/path/to/working/dir/SETUP.md .
cp ~/path/to/working/dir/EXAMPLES.md .
cp ~/path/to/working/dir/ADVANCED_ANALYSIS.md .
cp ~/path/to/working/dir/CONTRIBUTING.md .
cp ~/path/to/working/dir/TOOLS_REFERENCE.md .
cp ~/path/to/working/dir/SPOTIFY_SETUP.md .
cp ~/path/to/working/dir/LICENSE .
```

### Safe Code Files
```bash
cp ~/path/to/working/dir/music_server_updated_2025.py .
cp ~/path/to/working/dir/csv_to_json.py .
cp ~/path/to/working/dir/requirements.txt .
```

### Optional Sample Data
```bash
cp ~/path/to/working/dir/rsvp_songs.csv .
```

---

## Step 3: Copy Cleaned Files

**IMPORTANT:** Use the cleaned versions, not the originals!

The cleaned files were created in `/home/claude/` (or download them from the files Claude provided):

```bash
# Copy cleaned Python files (renamed to remove _clean suffix)
cp /home/claude/analyze_songs_clean.py analyze_songs.py
cp /home/claude/spotify_cli_clean.py spotify_cli.py
cp /home/claude/test_mcp_server_clean.py test_mcp_server.py
```

---

## Step 4: Copy New Template Files

```bash
# Copy new files Claude created
cp /home/claude/.env.example .
cp /home/claude/.gitignore .
cp /home/claude/claude_desktop_config.json.example .
cp /home/claude/GITHUB_SETUP.md .
cp /home/claude/REPO_CHECKLIST.md .
```

---

## Step 5: Verify

```bash
# List all files
ls -la

# Search for any credentials (should find nothing!)
grep -r "406868b824c14165a7772b627f763e97" .
grep -r "636060ca87ef4c9782bcc687c03b6780" .
```

Expected result: **No matches found!**

---

## Files You Should Have

```
.env.example
.gitignore
ADVANCED_ANALYSIS.md
CONTRIBUTING.md
EXAMPLES.md
GITHUB_SETUP.md
LICENSE
QUICKSTART.md
README.md
REPO_CHECKLIST.md
SETUP.md
SPOTIFY_SETUP.md
TOOLS_REFERENCE.md
analyze_songs.py          ← Cleaned version
claude_desktop_config.json.example
csv_to_json.py
music_server_updated_2025.py
requirements.txt
rsvp_songs.csv           ← Optional
spotify_cli.py           ← Cleaned version
test_mcp_server.py       ← Cleaned version
```

---

## Next Steps

1. ✅ Files copied
2. ✅ Credentials verified (not found in any file)
3. ➡️ Follow `GITHUB_SETUP.md` to push to GitHub
4. ➡️ Use `REPO_CHECKLIST.md` for final verification

---

**Windows Users:** Replace `cp` with `copy` and use backslashes in paths.
