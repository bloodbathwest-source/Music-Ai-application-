# Music AI Application - Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Web Browser (Client)                     │
│  ┌───────────────────────────────────────────────────────┐  │
│  │         HTML/CSS/JavaScript Interface                  │  │
│  │  - Customization Controls                             │  │
│  │  - Generation Button                                  │  │
│  │  - Results Display                                    │  │
│  │  - Statistics Dashboard                               │  │
│  └───────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/JSON
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   Flask Application Server                   │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                    app.py (Routes)                     │  │
│  │  - /                  (Main page)                      │  │
│  │  - /api/generate      (Content generation)            │  │
│  │  - /api/evolution-stats (Statistics)                  │  │
│  │  - /output/<file>     (File serving)                  │  │
│  └───────────────────────────────────────────────────────┘  │
│                           │                                  │
│           ┌───────────────┴───────────────┐                 │
│           ▼                               ▼                 │
│  ┌─────────────────┐           ┌─────────────────────┐     │
│  │   Generators    │           │  Evolution Engine   │     │
│  │                 │           │                     │     │
│  │ • Music         │           │ • Track usage       │     │
│  │ • Lyrics        │◄──────────┤ • Learn patterns    │     │
│  │ • Artist        │           │ • Calculate scores  │     │
│  │ • Image         │           │ • Store statistics  │     │
│  │ • Video         │           │                     │     │
│  └─────────────────┘           └─────────────────────┘     │
│           │                                │                │
│           ▼                                ▼                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              File System Storage                     │   │
│  │  - output/songs/      (MIDI files)                  │   │
│  │  - output/images/     (PNG files)                   │   │
│  │  - output/            (Lyrics TXT files)            │   │
│  │  - evolution_stats.json (AI learning data)          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### Content Generation Flow

```
User Input (Web UI)
    │
    ├─ Quantity: 1-10
    ├─ Content Types: [song, lyrics, artist, picture, video]
    └─ Customization:
        ├─ Genre
        ├─ Mood
        ├─ Tempo
        ├─ Key
        └─ Style
    │
    ▼
Flask API (/api/generate)
    │
    ├─ Validate input
    ├─ Loop for quantity
    │   │
    │   ├─ Call ArtistGenerator.generate()
    │   ├─ Call LyricsGenerator.generate()
    │   ├─ Call MusicGenerator.generate()
    │   ├─ Call ImageGenerator.generate()
    │   └─ Save files to output/
    │
    ├─ Record in EvolutionEngine
    └─ Return results
    │
    ▼
Response to Client
    │
    ├─ Generated files metadata
    ├─ Download links
    └─ Evolution score
    │
    ▼
Display Results & Update UI
```

### Evolution Learning Flow

```
Content Generated
    │
    ▼
EvolutionEngine.record_generation()
    │
    ├─ Increment total_generations
    ├─ Update genre_counts
    ├─ Update mood_counts
    ├─ Update tempo_counts
    └─ Add to generation_history
    │
    ▼
EvolutionEngine.evolve()
    │
    ├─ Calculate base_score (generations / 10)
    ├─ Calculate diversity_bonus
    ├─ Determine preferred_genre
    ├─ Determine preferred_mood
    └─ Save to evolution_stats.json
    │
    ▼
Updated Evolution Score Returned to UI
```

## Component Responsibilities

### Frontend (Web UI)
- **templates/index.html**: Structure and layout
- **static/css/style.css**: Visual styling, animations, responsive design
- **static/js/app.js**: User interactions, API calls, dynamic updates

### Backend (Python)
- **app.py**: Flask routes, request handling, response formatting
- **music_generator.py**: MIDI generation with scales, tempo, dynamics
- **image_generator.py**: PNG generation with color schemes and patterns
- **lyrics_generator.py**: Text generation with templates and themes
- **artist_generator.py**: Name generation based on genre conventions
- **evolution_engine.py**: Usage tracking, preference learning, scoring

### Storage
- **output/**: Generated content files (MIDI, PNG, TXT)
- **evolution_stats.json**: AI learning data persistence
- **config.json**: Application configuration (optional)

## Technology Stack

### Backend
- **Flask**: Web framework
- **Python 3.7+**: Programming language
- **midiutil**: MIDI file creation
- **Pillow (PIL)**: Image generation

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling (Flexbox, Grid, Gradients, Animations)
- **JavaScript (ES6+)**: Interactivity
- **Fetch API**: HTTP requests

### Data Format
- **JSON**: API communication, configuration, statistics
- **MIDI**: Music files
- **PNG**: Image files
- **TXT**: Lyrics files

## Extensibility Points

### Add New Generator
1. Create `new_generator.py` with `generate(customization)` method
2. Import and instantiate in `app.py`
3. Add to API endpoint logic
4. Update UI with new content type option

### Add Customization Option
1. Update relevant generator's logic
2. Add to `config.json`
3. Add UI control in `index.html`
4. Update JavaScript in `app.js`

### Enhance Evolution
1. Add new metrics to `evolution_engine.py`
2. Update `get_stats()` method
3. Display in UI statistics section

## Performance Characteristics

- **Generation Time**: 0.5-3 seconds per item
  - Songs: ~0.5s (MIDI generation)
  - Images: ~1-2s (PNG rendering)
  - Lyrics: ~0.1s (text generation)
  - Artist: ~0.01s (name generation)

- **Memory Usage**: ~50-100MB (depends on batch size)
- **Disk Usage**: ~1-5MB per generation set
  - MIDI: ~5-50KB
  - PNG: ~500KB-2MB
  - TXT: ~1-5KB

## Security Considerations

- Input validation on all API endpoints
- File path sanitization
- Limited file size for generated content
- No user authentication (local use)
- CORS not configured (local use)

## Future Enhancements

1. **Video Generation**: Implement actual video creation
2. **Audio Export**: WAV/MP3 generation from MIDI
3. **User Accounts**: Multi-user support with profiles
4. **Cloud Storage**: Integration with S3/GCS
5. **Advanced AI**: Neural network-based generation
6. **Collaboration**: Share and remix content
7. **Mobile App**: Native mobile applications
8. **Real-time Preview**: Play music/show images before saving
