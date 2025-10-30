# Music AI Application - User Guide

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```
   Or use the convenience script:
   ```bash
   ./run.sh
   ```

3. **Access the Web Interface**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Using the Application

### Generating Content

1. **Choose Quantity**: Select how many items you want to generate (1-10)

2. **Select Content Types**: Check the boxes for what you want to create:
   - **Song (MIDI)**: Musical composition in MIDI format
   - **Lyrics**: Complete song lyrics with verses, chorus, and bridge
   - **Artist Name**: Creative artist/band name
   - **Album Art**: Unique album artwork
   - **Video**: (Placeholder for future implementation)

3. **Customize Your Music**:
   - **Genre**: Pop, Rock, Jazz, Classical, Electronic, Hip-Hop, Country, Blues
   - **Mood**: Happy, Sad, Energetic, Calm, Romantic, Dark, Uplifting
   - **Tempo**: Slow, Medium, Fast, Variable
   - **Key**: Choose from C to B (including sharps)
   - **Style**: Acoustic, Electric, Orchestral, Synthetic, Mixed

4. **Generate**: Click the "🎼 Generate Content" button

5. **Review & Download**: 
   - View generated content in the results section
   - Download any generated files (songs, lyrics, images)
   - All files are automatically saved in the `output/` directory

### Evolution System

The Music AI learns from your usage:

- **Evolution Score**: Increases as you use the application
- **Preferred Genre**: The AI tracks your most-used genre
- **Preferred Mood**: The AI tracks your most-used mood
- **Generation History**: Recent generations are tracked

The more you use the application, the higher your evolution score!

## File Structure

```
Music-Ai-application-/
├── app.py                    # Main Flask application
├── music_generator.py        # MIDI music generation
├── image_generator.py        # Album art generation
├── lyrics_generator.py       # Lyrics generation
├── artist_generator.py       # Artist name generation
├── evolution_engine.py       # AI learning system
├── templates/
│   └── index.html           # Web interface
├── static/
│   ├── css/
│   │   └── style.css        # Styling
│   └── js/
│       └── app.js           # Frontend JavaScript
├── output/                  # Generated files (auto-created)
│   ├── songs/              # MIDI files
│   ├── images/             # Album art
│   └── videos/             # Videos (future)
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## Generated Output

### Songs (MIDI)
- Format: `.mid` (MIDI file)
- Location: `output/songs/`
- Features: Genre-specific scales, tempo control, mood-based dynamics
- Can be opened in: Any MIDI player or DAW software

### Lyrics
- Format: `.txt` (text file)
- Location: `output/`
- Features: Structured with verses, chorus, bridge
- Includes: Title, verse markers, mood-appropriate themes

### Artist Names
- Generated based on genre and style
- Solo artists, bands, ensembles, and crews
- Contextually appropriate for the selected genre

### Album Art
- Format: `.png` (image file)
- Size: 800x800 pixels
- Location: `output/images/`
- Features: Mood-based color schemes, genre-specific patterns

## Customization Details

### Genres and Their Characteristics

- **Pop**: Major scale, catchy melodies, mainstream appeal
- **Rock**: Minor scale, powerful progressions
- **Jazz**: Dorian mode, complex harmonies
- **Classical**: Major scale, traditional structure
- **Electronic**: Pentatonic, synthetic sounds
- **Hip-Hop**: Minor pentatonic, rhythmic focus
- **Country**: Major scale, organic feel
- **Blues**: Blues scale, expressive notes

### Mood Effects

Moods affect:
- **Colors** in album art
- **Word choice** in lyrics
- **Volume dynamics** in music
- **Visual patterns** in images

### Performance Tips

- Generate multiple items at once for variety
- Experiment with different genre/mood combinations
- Use the evolution statistics to track your creative journey
- Download your favorites before generating new batches

## Troubleshooting

### Application won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: Python 3.7+ required
- Verify port 5000 is not in use

### Generated files not appearing
- Check the `output/` directory exists
- Verify write permissions in the application directory
- Look for error messages in the terminal

### Slow generation
- Generating multiple items takes longer
- Large batches (10 items) may take 30+ seconds
- Album art generation is the most time-intensive

## API Endpoints

For developers who want to integrate with the application:

### POST /api/generate
Generate content programmatically
```json
{
  "quantity": 1,
  "content_types": ["song", "lyrics", "artist", "picture"],
  "customization": {
    "genre": "pop",
    "mood": "happy",
    "tempo": "medium",
    "key": "C",
    "style": "electric"
  }
}
```

### GET /api/customization-options
Get available customization options

### GET /api/evolution-stats
Get evolution statistics

## Advanced Usage

### Batch Processing
Create multiple variations quickly by running multiple generations with different settings.

### Export Collections
Organize your generated files in the `output/` directory by creating subdirectories for different projects.

### Integration
The Flask API can be called from other applications for automated music generation.

## Future Enhancements

- Video generation (currently placeholder)
- More musical instruments and styles
- User-defined templates
- Export to additional formats (WAV, MP3)
- Advanced AI learning with neural networks
- Cloud storage integration
- Social sharing features

## Support

For issues, questions, or contributions, visit the GitHub repository:
https://github.com/bloodbathwest-source/Music-Ai-application-

## Credits

Created with Flask, Pillow, and MIDIUtil libraries.
