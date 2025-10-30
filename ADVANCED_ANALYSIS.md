# 🎯 Advanced Analysis Tools

Complete guide to the advanced analysis features in the MCP Music Server!

## New Tools Overview

1. **analyze_explicitness** - Check explicit content and get family-friendly ratings
2. **analyze_collection_diversity** - Measure how diverse your music taste is
3. **get_top_artists_from_collection** - Find your most-played artists
4. **analyze_genres_in_collection** - Genre breakdown and distribution

---

## Tool 1: `analyze_explicitness`

### What It Does
Checks if songs contain explicit lyrics and provides a family-friendly rating for your collection.

### Perfect For
- Creating clean playlists for events
- Checking music before sharing with kids
- Understanding explicit content in your library
- Content moderation for public spaces

### Example Queries

**Check a playlist:**
```
Is my party playlist family-friendly? Here are the songs:
- Uptown Funk by Bruno Mars
- Happy by Pharrell Williams  
- Shut Up and Dance by Walk the Moon
- 24K Magic by Bruno Mars
- Can't Stop the Feeling by Justin Timberlake
```

**Compare playlists:**
```
Which playlist is cleaner:
Playlist A: [list songs]
Playlist B: [list songs]
```

**Find explicit songs:**
```
Check these songs for explicit content and tell me which ones are explicit:
- [list 10-15 songs from different genres]
```

### What You Get Back

```json
{
  "summary": {
    "total_songs_analyzed": 10,
    "explicit_songs_count": 3,
    "clean_songs_count": 7,
    "explicit_percentage": 30.0,
    "rating": "Mixed Content",
    "errors": null
  },
  "explicit_songs": [
    {
      "name": "Lose Yourself",
      "artists": ["Eminem"],
      "explicit": true,
      "popularity": 89
    }
    // ... more explicit songs
  ],
  "clean_songs": [
    {
      "name": "Eye of the Tiger",
      "artists": ["Survivor"],
      "explicit": false,
      "popularity": 83
    }
    // ... more clean songs
  ]
}
```

### Rating Categories

- **Family-Friendly** - 0% explicit (all clean)
- **Mostly Clean** - <25% explicit
- **Mixed Content** - 25-50% explicit
- **Mostly Explicit** - 50-75% explicit
- **Explicit** - >75% explicit

### Workshop Demo Idea

**"Clean Playlist Challenge":**
```
1. Students submit their top 10 songs
2. Analyze each collection for explicitness
3. See who has the cleanest playlist
4. Discuss music choices and content awareness
```

---

## Tool 2: `analyze_collection_diversity`

### What It Does
Measures how diverse your music collection is across multiple dimensions:
- **Artist diversity** - How many unique artists vs total
- **Genre diversity** - Number and variety of genres
- **Popularity distribution** - Mainstream vs underground
- **Era distribution** - Span of years covered

### Perfect For
- Understanding your music taste
- Discovering gaps in your listening
- Portfolio analysis for DJs
- Music discovery insights

### Example Queries

**Personal analysis:**
```
How diverse is my music taste? Analyze these 20 songs:
[list your favorite songs]
```

**Compare music tastes:**
```
My friend and I want to see who has more diverse taste. 
Compare our top 10 songs:
Me: [list]
Friend: [list]
```

**Playlist optimization:**
```
I'm making a party playlist. Check if it's diverse enough:
[list 15-20 songs]
```

### What You Get Back

```json
{
  "summary": {
    "diversity_level": "Very Diverse",
    "total_songs": 20,
    "errors": null
  },
  "artist_diversity": {
    "unique_artists": 18,
    "total_artist_appearances": 20,
    "diversity_score": 0.900,
    "interpretation": "High"
  },
  "genre_diversity": {
    "unique_genres": 12,
    "genres": [
      "indie rock",
      "alternative",
      "pop",
      "indie pop",
      "post-punk revival",
      "modern rock",
      // ... more
    ],
    "interpretation": "Very Diverse"
  },
  "popularity_distribution": {
    "average_popularity": 65.3,
    "range": 45,
    "interpretation": "Popular"
  },
  "era_distribution": {
    "year_range": 25,
    "earliest": 1998,
    "latest": 2023,
    "interpretation": "Multi-era"
  },
  "tracks": [
    {
      "name": "Mr. Brightside",
      "artists": ["The Killers"],
      "popularity": 87,
      "release_year": 2003
    }
    // ... more tracks
  ]
}
```

### Diversity Levels

**Overall:**
- **Very Diverse** - High artist variety + 10+ genres
- **Diverse** - Good artist variety + 5+ genres
- **Moderately Diverse** - Some artist variety
- **Low Diversity** - Repetitive artists/genres

**Artist Diversity Score:**
- **High** - >0.7 (mostly unique artists)
- **Medium** - 0.4-0.7 (some repetition)
- **Low** - <0.4 (same artists frequently)

**Popularity Interpretation:**
- **Mainstream** - Avg >70 (very popular)
- **Popular** - Avg 50-70 (well-known)
- **Mixed** - Avg 30-50 (varied)
- **Underground/Niche** - Avg <30 (obscure)

**Era Interpretation:**
- **Multi-era** - >20 year span
- **Modern** - All after 2010
- **Recent-focused** - Mostly recent songs

### Workshop Demo Ideas

**"Find Your Music Twin":**
```
1. Everyone analyzes their top 10 songs
2. Compare diversity scores
3. Find people with similar diversity patterns
4. Discover why you match!
```

**"Diversity Challenge":**
```
1. Analyze your current favorites
2. Identify weak spots (e.g., only pop, only 2020s)
3. Add songs to increase diversity
4. Re-analyze and see improvement
```

---

## Tool 3: `get_top_artists_from_collection`

### What It Does
Finds which artists appear most frequently in your collection and shows their contribution percentage.

### Perfect For
- Understanding your listening patterns
- Finding your favorite artists objectively
- Playlist balance checking
- Discovering artist obsessions

### Example Queries

**Personal favorites:**
```
Who are my top artists? Analyze these 30 songs:
[list songs from your library]
```

**Playlist balance:**
```
Does my workout playlist have too much of one artist? Here are the songs:
[list songs]
```

**Festival prep:**
```
I'm going to a music festival. Which artists should I prioritize 
based on my listening? Analyze my top 50 songs.
```

### What You Get Back

```json
{
  "summary": {
    "total_songs_analyzed": 30,
    "unique_artists": 18,
    "top_artist": "The Killers",
    "errors": null
  },
  "top_artists": [
    {
      "artist": "The Killers",
      "song_count": 5,
      "percentage": 16.7,
      "songs": [
        "Mr. Brightside",
        "Somebody Told Me",
        "When You Were Young",
        "Human",
        "All These Things That I've Done"
      ]
    },
    {
      "artist": "Arctic Monkeys",
      "song_count": 3,
      "percentage": 10.0,
      "songs": [
        "Do I Wanna Know?",
        "R U Mine?",
        "Why'd You Only Call Me When You're High?"
      ]
    }
    // ... more artists
  ],
  "distribution_type": "Varied"
}
```

### Distribution Types

- **Focused** - One artist dominates (>40%)
- **Balanced** - Even distribution
- **Varied** - Mix of frequencies

### Use Cases

**1. Playlist Curation:**
```
"My driving playlist has too much Foo Fighters (35%). 
Replace 2 songs with similar energy from other artists."
```

**2. Music Discovery:**
```
"I love The Killers (6 songs in my favorites). 
Recommend artists similar to them that I might not know."
```

**3. Event Planning:**
```
"My party playlist analysis shows:
- 25% Bruno Mars
- 20% Dua Lipa  
- 15% The Weeknd
Perfect mix for a dance party!"
```

### Workshop Demo Idea

**"Artist Obsession Detector":**
```
1. Everyone analyzes their Spotify wrapped playlist
2. Find the person most obsessed with one artist
3. That person presents why they love that artist
4. Everyone discovers the artist's best songs
```

---

## Tool 4: `analyze_genres_in_collection`

### What It Does
Provides complete genre analysis including dominant styles, genre diversity, and detailed distribution with percentages.

### Perfect For
- Understanding your musical identity
- Finding genre patterns
- Discovering music categories
- Playlist theme validation

### Example Queries

**Personal identity:**
```
What type of music do I actually listen to? Analyze these songs:
[list 25 favorite songs]
```

**Genre exploration:**
```
I think I like rock music, but I'm not sure. Analyze my collection 
and tell me my actual genre preferences:
[list songs]
```

**Playlist theming:**
```
Is my "chill vibes" playlist actually chill? Check the genres:
[list songs]
```

### What You Get Back

```json
{
  "summary": {
    "total_songs_analyzed": 20,
    "unique_genres": 15,
    "dominant_style": "Indie/Alternative",
    "genre_diversity": "Diverse",
    "errors": null
  },
  "top_genres": [
    {
      "genre": "indie rock",
      "count": 12,
      "percentage": 28.6
    },
    {
      "genre": "alternative",
      "count": 10,
      "percentage": 23.8
    },
    {
      "genre": "indie pop",
      "count": 8,
      "percentage": 19.0
    },
    {
      "genre": "post-punk revival",
      "count": 5,
      "percentage": 11.9
    },
    {
      "genre": "modern rock",
      "count": 4,
      "percentage": 9.5
    }
    // ... more genres (top 15 shown)
  ],
  "genre_distribution": {
    "total_genre_tags": 42,
    "average_genres_per_song": 2.1
  },
  "tracks_with_genres": [
    {
      "name": "Mr. Brightside",
      "artists": ["The Killers"],
      "genres": [
        "indie rock",
        "modern rock",
        "permanent wave",
        "rock"
      ]
    }
    // ... more tracks
  ]
}
```

### Genre Diversity Levels

- **Very Diverse** - 20+ unique genres
- **Diverse** - 10-20 unique genres
- **Moderately Diverse** - 5-10 unique genres
- **Limited** - <5 unique genres

### Dominant Style Categories

The tool automatically categorizes your collection:
- **Pop-oriented** - Pop dominates
- **Rock-focused** - Rock/alternative main
- **Hip-Hop/Rap** - Rap/hip-hop primary
- **Electronic** - EDM/electronic styles
- **Indie/Alternative** - Independent music
- **R&B/Soul** - R&B/soul focused
- **Country** - Country music
- **Jazz** - Jazz styles
- **Classical** - Classical music

### Advanced Use Cases

**1. Music Identity Discovery:**
```
"I always said I love 'everything' but my analysis shows:
- 40% indie rock
- 25% alternative
- 20% indie pop
I'm actually an indie music fan!"
```

**2. Mood vs Genre Analysis:**
```
"My 'sad songs' playlist genre analysis:
- 35% indie folk (makes sense)
- 30% singer-songwriter (expected)
- 20% dream pop (interesting!)
- 15% ambient (didn't realize)
"
```

**3. Genre Evolution:**
```
"Compare my 2020 favorites vs 2024 favorites:
2020: 60% pop, 30% hip-hop
2024: 45% indie, 30% alternative, 15% pop
My taste matured toward indie!"
```

### Workshop Demo Ideas

**"Musical Identity Crisis":**
```
1. Everyone predicts their top genre
2. Analyze 20 favorite songs
3. Compare prediction vs reality
4. Discuss surprising results
```

**"Genre Bingo":**
```
1. Create bingo card with 25 genres
2. Analyze class's combined music (100 songs)
3. Mark off genres as they appear
4. See how many we can find!
```

**"Build a Perfect Genre Mix":**
```
1. Goal: Create playlist with 5+ genres equally balanced
2. Each person contributes 3 songs
3. Analyze final collection
4. Discuss why diversity matters
```

---

## Combining Tools for Powerful Analysis

### Example 1: Complete Playlist Audit

```
Analyze my party playlist on all dimensions:
1. Check if it's family-friendly (explicitness)
2. Check artist variety (diversity)
3. Find most frequent artists (top artists)
4. Check genre balance (genres)

[list 20 songs]
```

**Result:** Complete report card for your playlist!

### Example 2: Music Taste Profile

```
Create a profile of my music taste:
1. Genre breakdown
2. Diversity score
3. Top artists
4. Explicit content percentage

[list 30 favorite songs]
```

**Result:** Your musical identity in data form!

### Example 3: Before/After Comparison

```
I'm trying to diversify my music taste.

BEFORE (last month):
[list 15 songs]

AFTER (this month):
[list 15 new songs]

Compare:
- Genre diversity change
- Artist variety improvement
- New styles explored
```

**Result:** Track your musical growth!

### Example 4: Curator Challenge

```
I'm curating a playlist for a coffee shop. Requirements:
- 100% family-friendly
- 5+ genres
- No artist appears more than twice
- Focus on chill vibes

Check this draft:
[list 20 songs]
```

**Result:** Validate your playlist meets all criteria!

---

## Pro Tips for Advanced Analysis

### 1. Sample Size Matters

- **10-15 songs**: Quick insights
- **20-30 songs**: Reliable patterns
- **50+ songs**: Comprehensive analysis

### 2. Mix Different Tools

Don't just use one! Combine:
```
- Explicitness + Genres = "Clean electronic playlist"
- Diversity + Top Artists = "Balanced favorites list"
- Genres + Collection Analysis = "Mood validation"
```

### 3. Use for Discovery

```
"My genres show 80% rock but only 3 subgenres.
Recommend more diverse rock subgenres to explore."
```

### 4. Seasonal Analysis

```
Compare:
- Summer playlist genres
- Winter playlist genres
Find: Seasonal preferences!
```

### 5. Social Comparisons

```
Friend A genres: 60% hip-hop, 30% R&B
Friend B genres: 50% indie, 40% alternative
Overlap: Find shared genres for collaborative playlist!
```

---

## Common Questions

### Q: How accurate is the genre classification?
**A:** Spotify assigns genres to artists (not individual songs). Multiple artists = multiple genre tags. Very accurate for most mainstream music!

### Q: Why do some songs have many genres?
**A:** Artists can fit multiple categories! A song by Coldplay might be tagged: "pop", "rock", "alternative", "british rock", etc.

### Q: Can I analyze a playlist link?
**A:** Not directly with these tools. Use `analyze_playlist` for Spotify playlist IDs, or manually list songs for advanced analysis.

### Q: What if a song isn't on Spotify?
**A:** It won't be found. Analysis continues with other songs and reports errors.

### Q: Is this data private?
**A:** Yes! All analysis happens locally through your Spotify account. Nothing is stored or shared.

### Q: Can I export the results?
**A:** Ask Claude to create a report or export to CSV! It can format the JSON nicely.

---

## Workshop Activities

### Activity 1: Music Taste Panel (30 min)

```
1. Split class into groups of 4
2. Each person analyzes their top 15 songs (all 4 tools)
3. Group compiles a "taste profile" for each person
4. Present findings to class
5. Vote on most diverse, most focused, biggest surprise
```

### Activity 2: Playlist Olympics (45 min)

```
Challenge: Create the "perfect" playlist

Requirements:
- 20 songs
- Family-friendly (0% explicit)
- 7+ genres
- No artist appears >2 times
- Average energy >0.7

Teams compete, analyze results, winner announced!
```

### Activity 3: Genre Exploration (20 min)

```
1. Everyone lists 10 favorites
2. Analyze combined collection (class genres)
3. Find rare genres (only 1-2 people have)
4. Those people play their song and explain why they love that genre
5. Class discovers new genres!
```

---

## Real-World Applications

### 1. Event Planning
```
Wedding playlist:
- 100% clean (families present)
- Diverse eras (all ages)
- 30% top artists (favorites)
- 5+ genres (variety)
```

### 2. Content Creation
```
Podcast background music:
- Check explicit content
- Ensure no single artist dominates
- Match genre to podcast theme
```

### 3. Music Journalism
```
Artist analysis:
"Taylor Swift's evolution:
Fearless era: 80% country
1989 era: 90% pop
Folklore era: 60% indie, 30% alternative"
```

### 4. DJ Preparation
```
Club night planning:
- 70% high-energy genres
- 5% explicit (late night okay)
- 20 unique artists
- Genre flow plan
```

---

## Take It Further

### Build Custom Analyzers

```
Want more? Add your own tools:
- Tempo progression analyzer
- Mood journey plotter
- Decade distribution chart
- Collaboration network mapper
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to extend the server!

---

**Master these tools and you'll understand your music taste better than ever!** 🎵

For more examples:
- [EXAMPLES.md](EXAMPLES.md) - Basic tool examples
- [README.md](README.md) - Overview
- [WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md) - Workshop materials
