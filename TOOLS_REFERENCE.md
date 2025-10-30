# 🔧 Tools Quick Reference

Fast reference guide for all MCP Music Server tools.

---

## Basic Search & Info

### `search_tracks`
**What:** Search Spotify for tracks  
**Input:** Query string, limit (optional)  
**Example:** *"Find songs by The Killers"*

### `get_audio_features`
**What:** Get audio features using track IDs  
**Input:** Array of Spotify track IDs  
**Example:** *"Get features for track IDs: [id1, id2]"*

### `get_recommendations`
**What:** Get song recommendations  
**Input:** Seed tracks/artists/genres, limit  
**Example:** *"Recommend songs similar to Mr. Brightside"*

### `analyze_playlist`
**What:** Analyze a Spotify playlist  
**Input:** Playlist ID  
**Example:** *"Analyze playlist 37i9dQZF1DX..."*

### `get_artist_info`
**What:** Get artist details and top tracks  
**Input:** Spotify artist ID  
**Example:** *"Tell me about artist ID: 0C0XlULifJtAgn6ZNCW2eu"*

---

## Single Song Analysis

### `analyze_song_by_name` ⭐
**What:** Search song + get features in one step  
**Input:** Song name, artist name (optional but recommended)  
**Output:** Track info + all audio features  
**Example:** *"Analyze 'Blinding Lights' by The Weeknd"*

---

## Multi-Song Analysis

### `compare_songs` ⭐
**What:** Compare multiple songs side-by-side  
**Input:** Array of {song_name, artist_name}  
**Output:** Side-by-side feature comparison  
**Example:** *"Compare Bohemian Rhapsody, Stairway to Heaven, and Hotel California"*

### `analyze_song_collection` ⭐
**What:** Aggregate stats on song collection  
**Input:** Array of {song_name, artist_name}  
**Output:** Average features + mood classification  
**Moods:** Happy & Energetic, Happy & Calm, Intense & Dark, Sad & Mellow, Neutral  
**Example:** *"Analyze these 10 songs and tell me the overall vibe"*

---

## Advanced Analysis 🎯

### `analyze_explicitness` 🎯
**What:** Check explicit content in collection  
**Input:** Array of {song_name, artist_name}  
**Output:**
- Explicit songs count & list
- Clean songs count & list
- Explicit percentage
- Rating: Family-Friendly, Mostly Clean, Mixed, Mostly Explicit, Explicit

**Example:** *"Is this playlist family-friendly?"*

---

### `analyze_collection_diversity` 🎯
**What:** Measure collection diversity  
**Input:** Array of {song_name, artist_name}  
**Output:**
- **Artist diversity:** Unique/total ratio (High/Medium/Low)
- **Genre diversity:** Count + list (Very Diverse/Diverse/Limited)
- **Popularity distribution:** Average + range (Mainstream/Popular/Mixed/Underground)
- **Era distribution:** Year span + range (Multi-era/Modern/Recent)
- **Overall level:** Very Diverse, Diverse, Moderately Diverse, Low

**Example:** *"How diverse is my music taste?"*

---

### `get_top_artists_from_collection` 🎯
**What:** Find most frequent artists  
**Input:** Array of {song_name, artist_name}, top_n (optional, default 10)  
**Output:**
- Artist name
- Song count
- Percentage contribution
- List of songs by that artist
- Distribution type: Focused (>40% one artist), Balanced, Varied

**Example:** *"Who are my top artists from these 30 songs?"*

---

### `analyze_genres_in_collection` 🎯
**What:** Complete genre breakdown  
**Input:** Array of {song_name, artist_name}  
**Output:**
- **Top 15 genres** with counts & percentages
- **Dominant style:** Pop-oriented, Rock-focused, Hip-Hop/Rap, Electronic, Indie/Alternative, R&B/Soul, Country, Jazz, Classical
- **Genre diversity:** Very Diverse (20+), Diverse (10-20), Moderately Diverse (5-10), Limited (<5)
- **Per-track genres:** All genres for each song

**Example:** *"What genres dominate my collection?"*

---

## Tool Selection Guide

### "I want to..."

**...find songs**  
→ `search_tracks`

**...analyze one song quickly**  
→ `analyze_song_by_name`

**...compare a few songs**  
→ `compare_songs` (2-10 songs)

**...understand my playlist's vibe**  
→ `analyze_song_collection`

**...check if playlist is clean**  
→ `analyze_explicitness`

**...see how diverse my taste is**  
→ `analyze_collection_diversity`

**...find my favorite artists**  
→ `get_top_artists_from_collection`

**...know what genres I like**  
→ `analyze_genres_in_collection`

**...get recommendations**  
→ `get_recommendations`

**...analyze a Spotify playlist**  
→ `analyze_playlist`

---

## Common Combinations

### Complete Playlist Audit
```
1. analyze_song_collection (mood & features)
2. analyze_explicitness (content rating)
3. analyze_collection_diversity (variety check)
4. get_top_artists_from_collection (balance check)
5. analyze_genres_in_collection (genre mix)
```

### Music Taste Profile
```
1. analyze_song_collection (overall stats)
2. get_top_artists_from_collection (favorites)
3. analyze_genres_in_collection (preferences)
4. analyze_collection_diversity (breadth)
```

### Playlist Optimization
```
1. analyze_explicitness (ensure clean if needed)
2. get_top_artists_from_collection (check balance)
3. analyze_genres_in_collection (check variety)
4. analyze_song_collection (validate mood)
```

---

## Input Format

All collection tools use this format:

```json
{
  "songs": [
    {
      "song_name": "Mr. Brightside",
      "artist_name": "The Killers"
    },
    {
      "song_name": "Take Me Out",
      "artist_name": "Franz Ferdinand"
    }
  ]
}
```

**Tips:**
- Artist name is optional but highly recommended for accuracy
- Songs with common names should always include artist
- Misspellings are usually okay (Spotify search is forgiving)

---

## Feature Definitions

### Audio Features (0-1 scale unless noted)

- **Danceability:** How suitable for dancing
- **Energy:** Intensity and activity level
- **Valence:** Musical positivity (happy vs sad)
- **Acousticness:** Likelihood of being acoustic
- **Instrumentalness:** Likelihood of no vocals
- **Speechiness:** Presence of spoken words
- **Liveness:** Likelihood of live performance
- **Tempo:** Beats per minute (BPM)
- **Loudness:** Average decibels (dB)
- **Key:** Musical key (0-11 = C, C#, D, ..., B)
- **Mode:** Major (1) or Minor (0)
- **Time Signature:** Beats per measure

---

## Performance Notes

### Recommended Collection Sizes

- **Quick test:** 5-10 songs
- **Good insights:** 15-25 songs
- **Comprehensive:** 30-50 songs
- **Maximum:** 100+ songs (slower but works)

### API Call Efficiency

Most efficient → Least efficient:
1. `analyze_song_collection` - Batch processing
2. `compare_songs` - Batch processing
3. `analyze_song_by_name` - One at a time
4. Multiple `search_tracks` + `get_audio_features` - Two calls per song

---

## Error Handling

All tools handle errors gracefully:
- Song not found → Skipped, noted in errors array
- No audio features → Skipped, noted in errors
- Invalid input → Clear error message
- Partial failures → Analysis continues with valid songs

---

## For Workshop Instructors

### Beginner-Friendly Order

1. `analyze_song_by_name` - Easy, instant results
2. `compare_songs` - Visual, educational
3. `analyze_song_collection` - Shows power of aggregation
4. `analyze_explicitness` - Practical use case
5. `analyze_genres_in_collection` - Fun discovery
6. `analyze_collection_diversity` - Advanced insights

### Demo Progression

**Minute 0-5:** Single song analysis  
**Minute 5-15:** Comparisons  
**Minute 15-25:** Collection analysis  
**Minute 25-40:** Advanced analysis  
**Minute 40-60:** Hands-on practice

---

## Quick Troubleshooting

**"Song not found"**  
→ Include artist name, check spelling

**"No features available"**  
→ Some very new/obscure songs lack features

**"Tools not showing in Claude"**  
→ Restart Claude Desktop after config changes

**"Slow responses"**  
→ Reduce collection size or wait for API

**"Empty results"**  
→ Check that songs are on Spotify

---

## More Information

- **[EXAMPLES.md](EXAMPLES.md)** - Detailed examples for basic tools
- **[ADVANCED_ANALYSIS.md](ADVANCED_ANALYSIS.md)** - Complete guide to advanced tools
- **[WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md)** - Full workshop walkthrough
- **[README.md](README.md)** - Main documentation

---

**Print this for quick reference during workshops!** 📄
