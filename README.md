# 🎵 Workshop Music MCP Server

**AI @Princeton x CBC Workshop - October 30, 2025**

Build a real MCP server that connects Claude to Spotify! Search songs, analyze music collections, and create playlists using natural language.

---

## 🎯 What You'll Learn

- **MCP Fundamentals**: Build servers that give Claude new capabilities
- **API Integration**: Connect to real services (Spotify)
- **Tool Design**: Create intuitive interfaces for AI
- **Real-world Skills**: Handle API changes and deprecations (like we did with Spotify's 2025 update!)

## ⚡ Quick Start

### Prerequisites
- Python 3.10 or higher
- A Spotify account (free is fine!)
- Claude Desktop app installed
- Basic familiarity with terminal/command line

### Installation

1. **Clone this repository**
   ```bash
   git clone <your-repo-url>
   cd claude-mcp-workshop
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Spotify credentials**
   - Follow [SPOTIFY_SETUP.md](SPOTIFY_SETUP.md) to get your API keys
   - Copy `.env.example` to `.env` and fill in your credentials

4. **Configure Claude Desktop**
   - See [SETUP.md](SETUP.md) for detailed instructions
   - Add the MCP server to your Claude Desktop config

5. **Start the server and try it!**
   ```bash
   python music_server_updated_2025.py
   ```
   Then restart Claude Desktop and start chatting!

## 🎵 What Can It Do?

Once connected, you can ask Claude things like:

**Basic Discovery:**
- **"Find me some upbeat indie songs"** - Search tracks
- **"Tell me about Taylor Swift's most popular songs"** - Artist information
- **"Give me recommendations based on Blinding Lights"** - Get song recommendations

**Collection Analysis:**
- **"Is this playlist family-friendly?"** - Check explicit content
- **"How diverse is my music taste?"** - Artist, genre, and era diversity
- **"Which artists do I listen to most?"** - Artist frequency analysis
- **"What genres dominate my collection?"** - Genre breakdown and distribution
- **"Analyze this playlist"** - Get popularity stats and explicit content overview

**Playlist Creation:** 🎯
- **"Create a playlist from these 20 songs"** - Make actual Spotify playlists
- **"Balance this collection by genre and create a playlist"** - Smart playlist generation

## 🔧 Available Tools (10 Total)

### Discovery & Search

#### `search_tracks`
Search for songs on Spotify by name, artist, or keywords. Returns track details, popularity, and Spotify links.

#### `get_recommendations`
Get song recommendations based on seed tracks, artists, or genres. Great for discovering new music similar to what you already love.

#### `get_artist_info`
Get detailed information about artists including their top tracks, genres, popularity, and follower count.

### Playlist Tools ⭐ NEW!

#### `create_playlist`
Create a real Spotify playlist from a collection of songs! Provide song names and artists, and it'll search for them and create the playlist on your account.

#### `generate_balanced_playlist`
Create a balanced playlist from a larger collection. Balance by:
- **Genre** - Equal representation across genres
- **Artist** - Max 2 songs per artist for diversity
- **Era** - Even distribution across decades

#### `analyze_playlist`
Analyze any Spotify playlist to get popularity stats, explicit content percentage, and track details.

### Collection Analysis Tools 🎯

#### `analyze_explicitness`
Check explicit content in your song collection - find out what percentage has explicit lyrics and get a family-friendly rating.

#### `analyze_collection_diversity`
Analyze how diverse your music collection is:
- Artist variety and diversity score
- Genre spread and unique genres
- Popularity distribution (mainstream vs underground)
- Era range and distribution across decades

#### `get_top_artists_from_collection`
Find which artists appear most frequently in your collection and see their contribution percentages. Perfect for understanding your listening habits.

#### `analyze_genres_in_collection`
Get a complete genre breakdown - dominant styles, genre diversity score, and detailed distribution percentages with genre tags for each song.

## 🚨 What Changed in 2025?

**Important API Update:** Spotify deprecated their audio-features endpoint in November 2024. This MCP server has been updated to work without it!

**What's different:**
- ❌ **Removed**: Audio features like danceability, energy, valence, tempo are no longer accessible
- ✅ **Still Available**: Track info (name, artist, album, popularity, explicit flag), artist genres, release dates
- 🎯 **New Focus**: Playlist creation, genre analysis, explicitness checking, and collection diversity

**What this means for you:**
- You won't see "mood" analysis or "energy levels" anymore
- Focus shifted to practical tools: creating playlists and analyzing your collection's diversity
- The tools now use what's reliably available: popularity scores, genres, explicit flags, and release years

## 🏗️ Architecture

```
┌─────────────┐
│   Claude    │  Asks: "Find upbeat songs"
│  Desktop    │
└──────┬──────┘
       │ MCP Protocol
       │
┌──────▼──────────┐
│  MCP Server     │  Converts to: search_tracks("upbeat")
│  (This Code!)   │
└──────┬──────────┘
       │ Spotify API
       │
┌──────▼──────────┐
│  Spotify Web    │  Returns: Song data
│     API         │
└─────────────────┘
```

**How it works:**
1. You ask Claude a music question in natural language
2. Claude decides which MCP tool to use
3. Your MCP server calls Spotify's API
4. Results come back to Claude
5. Claude presents them in a friendly way

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get running in 10 minutes
- **[SETUP.md](SETUP.md)** - Detailed installation guide
- **[SPOTIFY_SETUP.md](SPOTIFY_SETUP.md)** - How to get API credentials
- **[TOOLS_REFERENCE.md](TOOLS_REFERENCE.md)** - 📄 Quick reference for all tools (print this!)
- **[EXAMPLES.md](EXAMPLES.md)** - ⭐ Example queries for bulk analysis tools!
- **[ADVANCED_ANALYSIS.md](ADVANCED_ANALYSIS.md)** - 🎯 Advanced analysis: explicitness, diversity, artists, genres!
- **[WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md)** - Full workshop walkthrough
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and fixes
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Build your own tools!

## 🎓 Learning Resources

### New to MCP?
- [Anthropic MCP Documentation](https://docs.anthropic.com/mcp)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

### Want to Learn More?
- [Spotify API Reference](https://developer.spotify.com/documentation/web-api)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [Python Async Programming](https://docs.python.org/3/library/asyncio.html)

## 🏆 48-Hour Challenge

After the workshop, try building your own MCP server! Some ideas:

- **📚 Book Recommendations** - Connect to Goodreads or Open Library
- **🎬 Movie Analysis** - Use TMDB API for film data
- **🍕 Recipe Finder** - Integrate with Spoonacular
- **⚡ Smart Home** - Control your lights or thermostat
- **📊 Data Viz** - Generate charts from your data

Join the AI@Princeton Discord for support during the challenge!

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'spotipy'"**
- Run: `pip install -r requirements.txt`

**"Can't connect to Spotify"**
- Check your `.env` file has the correct credentials
- Make sure you've created a Spotify app on their dashboard

**"Claude can't see the tools"**
- Restart Claude Desktop after adding the server to config
- Check that the server path in config is absolute (full path)

**More issues?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 🤝 Contributing

Want to add more features? Check out [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to add new tools
- Code style guidelines
- Testing your changes
- Submitting improvements

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built for AI@Princeton's MCP Workshop Series. Special thanks to:
- Anthropic for creating MCP
- Spotify for their excellent API
- The Princeton AI community

## 📧 Questions?

- **Workshop Questions**: Ask during the session or on Discord
- **Technical Issues**: Open an issue on GitHub
- **General MCP Help**: Check [docs.anthropic.com/mcp](https://docs.anthropic.com/mcp)

---

**Ready to build?** Start with [QUICKSTART.md](QUICKSTART.md) or jump into [SETUP.md](SETUP.md)!

⭐ If this helped you, give it a star on GitHub!
