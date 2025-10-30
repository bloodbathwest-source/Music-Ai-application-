# Music AI Application 🎵

An evolving AI application that creates songs, pictures, videos, lyrics, and artist names with full customization options.

## Features

- 🎼 **Music Generation**: Creates MIDI songs with customizable parameters
- 🎨 **Album Art Generation**: Generates unique album artwork based on mood and genre
- 📝 **Lyrics Generation**: Creates song lyrics matching the selected mood and style
- 🎤 **Artist Name Generation**: Generates creative artist names appropriate for the genre
- 📹 **Video Support**: Placeholder for future video generation
- 🧠 **Evolution Engine**: AI learns from usage and improves over time
- ⚙️ **Full Customization**: Control genre, mood, tempo, key, and style
- 📦 **Batch Creation**: Generate multiple items at once
- 💾 **Auto-Save**: All generated content is saved for upload

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bloodbathwest-source/Music-Ai-application-.git
cd Music-Ai-application-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the interface to:
   - Select quantity of items to generate
   - Choose content types (song, lyrics, artist name, album art, video)
   - Customize genre, mood, tempo, key, and style
   - Click "Generate Content" to create your music
   - Download generated files from the results

## Customization Options

- **Genres**: Pop, Rock, Jazz, Classical, Electronic, Hip-Hop, Country, Blues
- **Moods**: Happy, Sad, Energetic, Calm, Romantic, Dark, Uplifting
- **Tempos**: Slow, Medium, Fast, Variable
- **Keys**: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
- **Styles**: Acoustic, Electric, Orchestral, Synthetic, Mixed

## Evolution System

The AI tracks your usage patterns and evolves:
- Learns preferred genres and moods
- Evolution score increases with usage
- Provides personalized recommendations
- Adapts to create better content over time

## Output

Generated files are saved in the `output/` directory:
- `output/songs/` - MIDI music files
- `output/images/` - Album art PNG files
- `output/` - Lyrics text files

## Requirements

- Python 3.7+
- Flask 3.0.0
- Pillow 10.1.0
- midiutil 1.2.1
- numpy 1.24.3

## License

See LICENSE file for details.