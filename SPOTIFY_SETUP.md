# 🎵 Spotify API Setup Guide

Complete guide to getting your Spotify API credentials and understanding how they work.

## Table of Contents

1. [Overview](#overview)
2. [Creating a Spotify App](#creating-a-spotify-app)
3. [Understanding Credentials](#understanding-credentials)
4. [Security Best Practices](#security-best-practices)
5. [Authentication Flow](#authentication-flow)
6. [Troubleshooting](#troubleshooting)

---

## Overview

To use the Spotify API, you need to:
1. Have a Spotify account (free or premium, either works)
2. Create an "app" on Spotify's developer platform
3. Get your Client ID and Client Secret
4. Configure the redirect URI

Don't worry - it's easier than it sounds! This guide will walk you through everything.

---

## Creating a Spotify App

### Step 1: Access the Dashboard

1. Go to [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. If this is your first time:
   - You'll need to accept the Developer Terms of Service
   - Fill out a brief form about your intended use (select "I'm building something for personal use")

### Step 2: Create Your App

1. Click the green **"Create app"** button (top right)

2. Fill in the form:

   **App name**
   ```
   MCP Music Server
   ```
   (Or any name you prefer - this is just for your reference)

   **App description**
   ```
   MCP server that connects Claude to Spotify for music analysis and recommendations
   ```
   (This is also just for your reference)

   **Website** (optional)
   ```
   Leave blank or put your GitHub profile
   ```

   **Redirect URIs** ⚠️ **CRITICAL**
   ```
   http://localhost:8888/callback
   ```
   - Must be exactly this
   - Click "Add" after entering it
   - This tells Spotify where to send authentication responses

   **APIs used**
   - ✅ Check "Web API"
   - Don't check the others unless you plan to use them

3. Check the box: "I understand and agree with Spotify's Developer Terms of Service and Design Guidelines"

4. Click **"Save"**

### Step 3: Access Your App

After creation, you'll see your new app in the dashboard. Click on it to open the details page.

---

## Understanding Credentials

### Client ID

Your **Client ID** is visible immediately on your app's dashboard. It looks like:
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

This identifies your app to Spotify. It's not super secret, but don't share it publicly.

### Client Secret

Your **Client Secret** is hidden by default. To reveal it:

1. Click **"Settings"** button (top right of your app page)
2. Find the "Client secret" field
3. Click **"View client secret"**
4. It looks similar to the Client ID

**⚠️ This IS secret!** Treat it like a password:
- Don't commit it to git
- Don't share it in screenshots
- Don't post it in Discord/Slack
- Store it in `.env` file (which is in `.gitignore`)

### Scopes

Our server uses these Spotify scopes:
- `user-library-read` - Read your saved tracks
- `user-top-read` - Read your top artists and tracks
- `playlist-read-private` - Read your private playlists

These allow Claude to analyze your music but not modify anything.

---

## Security Best Practices

### DO ✅

- Store credentials in `.env` file
- Add `.env` to `.gitignore`
- Use different credentials for different projects
- Rotate credentials if you think they've been exposed
- Keep your Spotify account password secure

### DON'T ❌

- Commit `.env` to git
- Share credentials in chat or email
- Hardcode credentials in source files
- Screenshot credentials and share them
- Use production credentials for testing

### Environment Variables

Why we use `.env` files:

```python
# ❌ BAD - Hardcoded secrets
client_id = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

# ✅ GOOD - From environment
client_id = os.environ["SPOTIFY_CLIENT_ID"]
```

Benefits:
- Keeps secrets out of source code
- Easy to change without editing code
- Different credentials for different environments
- Protected by `.gitignore`

### If Credentials Are Compromised

If you accidentally expose your credentials:

1. **Immediately** go to your Spotify app settings
2. Click **"Rotate client secret"** to get a new secret
3. Update your `.env` file with the new secret
4. Old secret stops working instantly

---

## Authentication Flow

Understanding how authentication works in this project:

### First Run

1. You run the server with your credentials
2. The server tries to access Spotify
3. Spotify redirects you to a login page in your browser
4. You log in and approve the permissions
5. Spotify redirects back to `http://localhost:8888/callback`
6. The server receives an access token
7. Token is cached in `.cache` file (also in `.gitignore`)

### Subsequent Runs

1. Server checks for valid token in `.cache`
2. If token is valid, it's used directly
3. If expired, server automatically refreshes it
4. No browser login needed!

### Token Expiration

- Access tokens expire after 1 hour
- Refresh tokens last much longer
- Spotipy handles refresh automatically
- You rarely need to log in again

---

## Troubleshooting

### "Invalid client" Error

**Cause:** Wrong Client ID or Client Secret

**Fix:**
1. Double-check your credentials in `.env`
2. Make sure there are no extra spaces
3. Copy-paste directly from Spotify dashboard
4. Credentials should be just letters and numbers (no quotes!)

Example `.env`:
```env
# ❌ WRONG - Has quotes
SPOTIFY_CLIENT_ID="a1b2c3d4"

# ✅ CORRECT - No quotes
SPOTIFY_CLIENT_ID=a1b2c3d4e5f6g7h8
```

### "Invalid redirect URI" Error

**Cause:** Redirect URI doesn't match what's configured in Spotify

**Fix:**
1. Go to your app settings on Spotify dashboard
2. Under "Redirect URIs", make sure you have EXACTLY:
   ```
   http://localhost:8888/callback
   ```
3. It must match exactly:
   - Lowercase "http"
   - No "https"
   - Port number 8888
   - Path "/callback"
   - No trailing slash

### "Access denied" Error

**Cause:** You declined permissions during login

**Fix:**
1. Delete the `.cache` file in your project directory
2. Run the server again
3. When the browser opens, click "Agree" to grant permissions

### "Connection refused" on Redirect

**Cause:** The callback server isn't running on port 8888

**Fix:**
1. Make sure port 8888 isn't being used by another application
2. Try closing and restarting the server
3. Check if a firewall is blocking the port

### Can't Find Credentials

Make sure your `.env` file:
- Is named exactly `.env` (no extension)
- Is in the same directory as `music_server_updated_2025.py`
- Has no extra spaces around the `=` sign
- Has no quotes around the values

---

## Testing Your Setup

### Minimal Test Script

Create a file called `test_spotify.py`:

```python
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ["SPOTIFY_CLIENT_ID"],
    client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
    redirect_uri="http://localhost:8888/callback",
    scope="user-library-read"
))

# Test: Get current user's profile
user = sp.current_user()
print(f"Success! Logged in as: {user['display_name']}")
```

Run it:
```bash
python test_spotify.py
```

If it works, your credentials are set up correctly!

---

## API Limits

### Rate Limits

Spotify's API has rate limits:
- **Standard rate:** Most endpoints
- **User data:** Can access every few seconds
- **Search:** Higher limits

Our server stays well within these limits for normal use.

### What Counts as an API Call

- Each tool use = 1-3 API calls
- Batch operations are efficient
- Audio features: 100 tracks per call

Don't worry about limits for the workshop - you'd need to make thousands of requests to hit them!

---

## Advanced Configuration

### Custom Redirect URI

If port 8888 is taken, you can use a different port:

1. In Spotify dashboard, add a new redirect URI:
   ```
   http://localhost:3000/callback
   ```

2. Update the code in `music_server_updated_2025.py`:
   ```python
   redirect_uri="http://localhost:3000/callback"
   ```

### Additional Scopes

Want more capabilities? Add scopes:

```python
scope = "user-library-read user-top-read playlist-read-private playlist-modify-public"
```

Available scopes:
- `playlist-modify-public` - Modify public playlists
- `playlist-modify-private` - Modify private playlists
- `user-library-modify` - Add/remove saved tracks
- `user-read-playback-state` - Read playback state
- `user-modify-playback-state` - Control playback

See [Spotify's scope documentation](https://developer.spotify.com/documentation/web-api/concepts/scopes) for all options.

---

## Additional Resources

- [Spotify for Developers](https://developer.spotify.com/)
- [Web API Reference](https://developer.spotify.com/documentation/web-api)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [API Rate Limits](https://developer.spotify.com/documentation/web-api/concepts/rate-limits)

---

**Still having issues?** Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or ask during the workshop!
