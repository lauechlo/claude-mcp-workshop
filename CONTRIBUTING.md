# 🚀 Contributing Guide

Learn how to extend the MCP Music Server and build your own tools!

## Table of Contents

1. [Adding New Tools](#adding-new-tools)
2. [Adding New Resources](#adding-new-resources)
3. [Code Style](#code-style)
4. [Testing](#testing)
5. [Project Ideas](#project-ideas)
6. [Submitting Changes](#submitting-changes)

---

## Adding New Tools

Tools are functions that Claude can call. Here's how to add one.

### Step 1: Define the Tool

Add to the `list_tools()` function:

```python
@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        # ... existing tools ...
        
        Tool(
            name="get_playlist_genres",
            description="Analyze genres in a playlist and their distribution",
            inputSchema={
                "type": "object",
                "properties": {
                    "playlist_id": {
                        "type": "string",
                        "description": "Spotify playlist ID"
                    }
                },
                "required": ["playlist_id"]
            }
        )
    ]
```

### Step 2: Implement the Tool

Add to the `call_tool()` function:

```python
@app.call_tool()
async def call_tool(name: str, arguments: Any):
    # ... existing tool implementations ...
    
    elif name == "get_playlist_genres":
        playlist_id = arguments["playlist_id"]
        
        # Get playlist tracks
        playlist = sp.playlist(playlist_id)
        tracks = playlist["tracks"]["items"]
        
        # Collect all artists
        artist_ids = set()
        for item in tracks:
            if item["track"]:
                for artist in item["track"]["artists"]:
                    artist_ids.add(artist["id"])
        
        # Get genres from artists
        genres = {}
        for artist_id in artist_ids:
            artist = sp.artist(artist_id)
            for genre in artist["genres"]:
                genres[genre] = genres.get(genre, 0) + 1
        
        # Sort by frequency
        sorted_genres = sorted(
            genres.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        result = {
            "playlist_name": playlist["name"],
            "total_artists": len(artist_ids),
            "genres": [
                {"name": genre, "count": count}
                for genre, count in sorted_genres[:20]
            ]
        }
        
        return [TextContent(
            type="text",
            text=json.dumps(result, indent=2)
        )]
```

### Step 3: Test It!

1. Restart Claude Desktop
2. Try: "Analyze the genres in playlist [ID]"
3. Claude should use your new tool!

### Tool Design Best Practices

#### Good Tool Names

✅ **Clear and descriptive:**
- `search_tracks` - obvious what it does
- `get_audio_features` - clear input/output
- `analyze_playlist` - indicates analysis

❌ **Avoid vague names:**
- `do_thing` - what thing?
- `helper` - not descriptive
- `func1` - meaningless

#### Good Descriptions

✅ **Be specific:**
```python
description="Get detailed audio features for tracks including energy, danceability, tempo, valence, and acousticness"
```

❌ **Too vague:**
```python
description="Get data about songs"
```

#### Input Schemas

**Be explicit about parameters:**

```python
inputSchema={
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "Search query - can be song name, artist, or keywords",
            "examples": ["Bohemian Rhapsody", "Taylor Swift", "upbeat indie"]
        },
        "limit": {
            "type": "number",
            "description": "Number of results to return (1-50)",
            "default": 10,
            "minimum": 1,
            "maximum": 50
        },
        "market": {
            "type": "string",
            "description": "ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB')",
            "default": "US",
            "pattern": "^[A-Z]{2}$"
        }
    },
    "required": ["query"]
}
```

### Error Handling

Always handle errors gracefully:

```python
try:
    result = sp.track(track_id)
    return [TextContent(type="text", text=json.dumps(result))]
    
except spotipy.exceptions.SpotifyException as e:
    if e.http_status == 404:
        return [TextContent(
            type="text",
            text="Track not found. It may have been removed or is unavailable in your region."
        )]
    elif e.http_status == 401:
        return [TextContent(
            type="text",
            text="Authentication error. Please check your Spotify credentials."
        )]
    else:
        return [TextContent(
            type="text",
            text=f"Spotify API error: {str(e)}"
        )]
        
except Exception as e:
    logger.error(f"Unexpected error in get_track: {str(e)}")
    return [TextContent(
        type="text",
        text=f"An unexpected error occurred: {str(e)}"
    )]
```

---

## Adding New Resources

Resources are data that Claude can read directly.

### Step 1: Define the Resource

```python
@app.list_resources()
async def list_resources() -> list[Resource]:
    return [
        # ... existing resources ...
        
        Resource(
            uri=AnyUrl("music://user/recently-played"),
            name="Recently Played Tracks",
            mimeType="application/json",
            description="Your 50 most recently played tracks"
        )
    ]
```

### Step 2: Implement Resource Reading

```python
@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    uri_str = str(uri)
    
    # ... existing resource handlers ...
    
    if uri_str == "music://user/recently-played":
        recent = sp.current_user_recently_played(limit=50)
        
        formatted = []
        for item in recent["items"]:
            track = item["track"]
            formatted.append({
                "name": track["name"],
                "artists": [a["name"] for a in track["artists"]],
                "played_at": item["played_at"],
                "track_id": track["id"]
            })
        
        return json.dumps(formatted, indent=2)
```

### When to Use Resources vs Tools

**Use Resources when:**
- Data is relatively static
- User wants to browse/explore
- Data represents user's personal info
- Examples: profile, saved tracks, playlists

**Use Tools when:**
- Need to search or query
- Parameters affect output
- Operation has side effects
- Examples: search, recommendations, analysis

---

## Code Style

### Python Style Guide

Follow PEP 8 with these highlights:

```python
# Good naming
def get_audio_features(track_ids: list[str]) -> list[dict]:
    """
    Get audio features for multiple tracks.
    
    Args:
        track_ids: List of Spotify track IDs
        
    Returns:
        List of audio feature dictionaries
    """
    pass

# Use type hints
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    pass

# Descriptive variable names
playlist_tracks = []  # Good
pt = []               # Bad

# Constants in CAPS
MAX_TRACKS_PER_REQUEST = 100
DEFAULT_LIMIT = 20
```

### Documentation

Add docstrings to all functions:

```python
async def analyze_mood(track_ids: list[str]) -> dict:
    """
    Analyze the overall mood of a collection of tracks.
    
    Calculates average valence (happiness) and energy levels
    across all provided tracks to determine overall mood.
    
    Args:
        track_ids: List of Spotify track IDs (max 100)
        
    Returns:
        Dictionary containing:
            - average_valence: float (0-1)
            - average_energy: float (0-1)
            - mood_description: str
            
    Raises:
        ValueError: If track_ids list is empty or > 100 items
        SpotifyException: If API request fails
    """
```

### Comments

```python
# Good: Explain WHY, not WHAT
# Spotify's 2025 API change requires IDs instead of URIs
clean_id = track_uri.split(":")[-1]

# Bad: Obvious
# Get the last part of the string
clean_id = track_uri.split(":")[-1]
```

---

## Testing

### Manual Testing

Create test queries:

```python
# test_queries.py

test_cases = [
    {
        "query": "Search for Coldplay songs",
        "expected_tool": "search_tracks",
        "expected_success": True
    },
    {
        "query": "Get audio features for invalid_id_xyz",
        "expected_tool": "get_audio_features",
        "expected_success": False
    }
]
```

### Unit Tests

Add to `test_server.py`:

```python
import unittest
from music_server_updated_2025 import clean_track_id

class TestTrackIDCleaning(unittest.TestCase):
    def test_uri_format(self):
        uri = "spotify:track:abc123"
        self.assertEqual(clean_track_id(uri), "abc123")
    
    def test_url_format(self):
        url = "https://open.spotify.com/track/abc123"
        self.assertEqual(clean_track_id(url), "abc123")
    
    def test_id_only(self):
        id_only = "abc123"
        self.assertEqual(clean_track_id(id_only), "abc123")

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
python -m unittest test_server.py
```

### Integration Testing

Test with actual Spotify API:

```python
# integration_test.py

import os
from music_server_updated_2025 import get_spotify_client

def test_search():
    sp = get_spotify_client()
    results = sp.search(q="Bohemian Rhapsody", type="track", limit=1)
    assert len(results["tracks"]["items"]) > 0
    print("✅ Search test passed")

def test_audio_features():
    sp = get_spotify_client()
    # Known good track ID
    features = sp.audio_features(["3z8h0TU7ReDPLIbEnYhWZb"])
    assert features[0] is not None
    assert 0 <= features[0]["valence"] <= 1
    print("✅ Audio features test passed")

if __name__ == "__main__":
    test_search()
    test_audio_features()
    print("🎉 All tests passed!")
```

---

## Project Ideas

Want to build your own MCP server? Here are some ideas!

### Beginner Projects

#### 1. Weather MCP Server

**Tools:**
- `get_current_weather(location)` - Current conditions
- `get_forecast(location, days)` - Multi-day forecast
- `get_weather_alerts(location)` - Severe weather warnings

**APIs:** OpenWeatherMap, WeatherAPI

#### 2. Movie Database Server

**Tools:**
- `search_movies(query)` - Search films
- `get_movie_details(id)` - Full info on a movie
- `get_recommendations(movie_id)` - Similar films

**APIs:** TMDB, OMDb

#### 3. Recipe Finder

**Tools:**
- `search_recipes(ingredients)` - Find recipes
- `get_recipe(id)` - Detailed instructions
- `get_nutrition(recipe_id)` - Nutritional info

**APIs:** Spoonacular, Edamam

### Intermediate Projects

#### 4. GitHub Integration

**Tools:**
- `search_repositories(query)` - Find repos
- `get_repo_stats(owner, repo)` - Stars, forks, etc.
- `create_issue(repo, title, body)` - Create issues
- `get_user_activity(username)` - Recent activity

**APIs:** GitHub REST API

#### 5. News Aggregator

**Tools:**
- `search_news(query)` - Search articles
- `get_headlines(category, country)` - Top news
- `get_sources()` - Available news sources

**APIs:** NewsAPI, Guardian API

#### 6. Finance Tracker

**Tools:**
- `get_stock_price(symbol)` - Current price
- `get_stock_history(symbol, period)` - Historical data
- `get_crypto_prices()` - Cryptocurrency prices

**APIs:** Alpha Vantage, CoinGecko

### Advanced Projects

#### 7. Smart Home Controller

**Tools:**
- `list_devices()` - All smart devices
- `control_light(device_id, state)` - Turn lights on/off
- `set_temperature(degrees)` - Adjust thermostat
- `get_sensor_data()` - Temperature, motion, etc.

**APIs:** Home Assistant, Philips Hue, Nest

#### 8. Google Workspace Integration

**Tools:**
- `search_drive(query)` - Find files
- `read_document(file_id)` - Get doc contents
- `create_calendar_event(title, time)` - Schedule
- `send_gmail(to, subject, body)` - Send email

**APIs:** Google Drive, Calendar, Gmail

#### 9. Task Management System

**Tools:**
- `list_tasks(project)` - Get all tasks
- `create_task(title, description, due)` - New task
- `update_task(id, status)` - Mark complete
- `get_time_tracking()` - Time spent

**APIs:** Asana, Todoist, Trello

### Princeton-Specific Ideas

Perfect for the 48-hour challenge!

#### 10. Course Schedule Helper

**Tools:**
- `search_courses(query)` - Find Princeton courses
- `get_prerequisites(course_code)` - Required courses
- `check_schedule_conflicts(course_list)` - Time conflicts
- `get_course_reviews()` - Student reviews

**Data:** Registrar API, Student Assembly data

#### 11. Dining Hall Menu

**Tools:**
- `get_menu(dining_hall, meal)` - Today's menu
- `check_allergens(dining_hall, allergen)` - Safe options
- `get_hours(dining_hall)` - Opening hours
- `compare_menus()` - All halls today

**Data:** Princeton Dining scraper

#### 12. Campus Events

**Tools:**
- `list_events(date, category)` - Find events
- `get_event_details(id)` - Full information
- `search_organizations(name)` - Find clubs
- `check_room_availability(building, time)` - Book rooms

**Data:** PrincetonEvents, Student Activities

---

## Building Your Own Server Template

### Basic Structure

```python
#!/usr/bin/env python3
"""
My Custom MCP Server
Description of what it does
"""

import os
import json
import logging
from typing import Any, Sequence

from mcp.server import Server
from mcp.types import Resource, Tool, TextContent
from pydantic import AnyUrl
import mcp.server.stdio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my-server")

# Initialize your API client
# api_client = YourAPIClient(api_key=os.environ["YOUR_API_KEY"])

# Initialize MCP server
app = Server("my-server")


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    return [
        Resource(
            uri=AnyUrl("myserver://resource/example"),
            name="Example Resource",
            mimeType="application/json",
            description="Description of what this resource contains"
        )
    ]


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read resource data."""
    uri_str = str(uri)
    
    if uri_str == "myserver://resource/example":
        data = {"example": "data"}
        return json.dumps(data, indent=2)
    
    raise ValueError(f"Unknown resource: {uri}")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="example_tool",
            description="Description of what this tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Description of parameter"
                    }
                },
                "required": ["param1"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    """Execute tool."""
    try:
        if name == "example_tool":
            param1 = arguments["param1"]
            
            # Your tool logic here
            result = {"output": f"Processed: {param1}"}
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    except Exception as e:
        logger.error(f"Error executing tool {name}: {str(e)}")
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Submitting Changes

### Before Submitting

1. **Test thoroughly**
   - Manual testing with Claude
   - Unit tests pass
   - No new errors in logs

2. **Update documentation**
   - Add tool to README
   - Update relevant .md files
   - Add code comments

3. **Check code style**
   ```bash
   # Format code
   black music_server_updated_2025.py
   
   # Check style
   flake8 music_server_updated_2025.py
   ```

### Creating a Pull Request

1. **Fork the repository**

2. **Create a branch**
   ```bash
   git checkout -b feature/add-genre-analysis
   ```

3. **Make your changes**

4. **Commit with good messages**
   ```bash
   git add .
   git commit -m "Add genre analysis tool

   - Implements get_playlist_genres tool
   - Analyzes artist genres in playlists
   - Returns sorted genre distribution
   - Includes error handling and tests"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/add-genre-analysis
   ```

### PR Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Manual testing completed
- [ ] Unit tests added/updated
- [ ] Integration tests pass

## Screenshots (if applicable)
Paste screenshots of Claude using the new feature

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Tested on macOS/Windows/Linux
```

---

## Getting Help

### Resources

- **Workshop Discord** - Quick questions
- **GitHub Issues** - Bug reports, feature requests
- **MCP Documentation** - [docs.anthropic.com/mcp](https://docs.anthropic.com/mcp)
- **This Repository** - Check existing code for examples

### Code Review

We welcome contributions! When reviewing:
- Be respectful and constructive
- Explain reasoning behind suggestions
- Celebrate good additions

---

## Recognition

Contributors will be:
- Listed in README
- Mentioned in release notes
- Invited to future workshops

---

**Ready to build?** Start small, test often, and have fun! 🚀

For inspiration, check out the [MCP Servers Repository](https://github.com/anthropics/mcp-servers) for more examples!
