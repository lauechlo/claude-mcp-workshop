# ⚡ Quick Start Guide

Get your MCP music server running in **10 minutes**!

This guide assumes you're comfortable with terminals and have Python installed.

## Prerequisites

- Python 3.10+
- Spotify account
- Claude Desktop

## Step 1: Install Dependencies (2 min)

```bash
# Clone the repo
git clone <your-repo-url>
cd workshop-music-mcp

# Install Python packages
pip install -r requirements.txt
```

## Step 2: Get Spotify API Keys (3 min)

1. Go to [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Click **"Create app"**
3. Fill in:
   - **App name**: "My MCP Music Server"
   - **Redirect URI**: `http://127.0.0.1:8888/callback` (Spotify does not allow localhost addresses)
   - Check the box for Web API
4. Click **"Save"**
5. Click **"Settings"** → Copy your **Client ID** and **Client Secret**

## Step 3: Configure Environment (1 min)

```bash
# Copy the template
cp .env.example .env

# Edit .env and paste your credentials
# SPOTIFY_CLIENT_ID=your_actual_client_id
# SPOTIFY_CLIENT_SECRET=your_actual_client_secret
```

## Step 4: Add to Claude Desktop (3 min)

### macOS

```bash
# Open config file
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Windows

```bash
# Open config file
notepad %APPDATA%\Claude\claude_desktop_config.json
```

### Linux

```bash
# Open config file
code ~/.config/Claude/claude_desktop_config.json
```

Add this to the file (replace `/path/to/` with your actual path):

```json
{
  "mcpServers": {
    "music": {
      "command": "python",
      "args": [
        "/absolute/path/to/music_server_updated_2025.py"
      ],
      "env": {
        "SPOTIFY_CLIENT_ID": "your_client_id",
        "SPOTIFY_CLIENT_SECRET": "your_client_secret"
      }
    }
  }
}
```

**💡 Pro tip:** Get your absolute path with:
- macOS/Linux: `pwd`
- Windows: `cd`

## Step 5: Test It! (1 min)

1. **Restart Claude Desktop** (important!)
2. Open a new chat
3. Try: **"Search for songs by Taylor Swift"**
4. Claude should use the music tools! 🎉

## ✅ Success Checklist

- [ ] Python 3.10+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Spotify app created on developer dashboard
- [ ] `.env` file created with your credentials
- [ ] Config added to Claude Desktop
- [ ] Claude Desktop restarted
- [ ] Test query works!

## 🐛 Quick Troubleshooting

**"ModuleNotFoundError"**
```bash
pip install spotipy mcp pydantic python-dotenv
```

**"Can't find config file"**
- macOS: `~/Library/Application Support/Claude/`
- Windows: `%APPDATA%\Claude\`
- Linux: `~/.config/Claude/`

**"Claude doesn't see the tools"**
- Did you restart Claude Desktop?
- Is the path absolute (full path, not relative)?
- Check for typos in the config JSON

**Still stuck?** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 🎵 What to Try

Once it's working, ask Claude:

- "Find me some relaxing jazz songs"
- "What are the audio features of Bohemian Rhapsody?"
- "Recommend songs similar to [your favorite song]"
- "Analyze my workout playlist" (you'll need to give Claude a playlist ID)

## 📚 Want More Details?

- **[SETUP.md](SETUP.md)** - Step-by-step guide with screenshots
- **[SPOTIFY_SETUP.md](SPOTIFY_SETUP.md)** - Detailed Spotify configuration
- **[WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md)** - Full workshop tutorial

---

**Next Step:** Try building your own tools! See [CONTRIBUTING.md](CONTRIBUTING.md)
