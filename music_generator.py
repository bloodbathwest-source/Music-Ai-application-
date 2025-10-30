"""
Music Generator Module
Generates MIDI music files with customizable parameters.
"""

import random
from pathlib import Path
from midiutil import MIDIFile

OUTPUT_DIR = Path("output/songs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class MusicGenerator:
    """Generate music using MIDI."""
    
    def __init__(self):
        self.genre_scales = {
            'pop': [0, 2, 4, 5, 7, 9, 11],  # Major scale
            'rock': [0, 2, 3, 5, 7, 8, 10],  # Minor scale
            'jazz': [0, 2, 3, 5, 7, 9, 10],  # Dorian mode
            'classical': [0, 2, 4, 5, 7, 9, 11],  # Major scale
            'electronic': [0, 2, 4, 7, 9],  # Pentatonic
            'hip-hop': [0, 3, 5, 7, 10],  # Minor pentatonic
            'country': [0, 2, 4, 5, 7, 9, 11],  # Major scale
            'blues': [0, 3, 5, 6, 7, 10]  # Blues scale
        }
        
        self.tempo_map = {
            'slow': 60,
            'medium': 120,
            'fast': 160,
            'variable': 120
        }
        
        self.key_map = {
            'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
            'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
        }
    
    def generate(self, customization):
        """
        Generate a MIDI music file.
        
        Args:
            customization: dict with genre, mood, tempo, key, style
            
        Returns:
            str: filename of generated MIDI file
        """
        genre = customization.get('genre', 'pop')
        mood = customization.get('mood', 'happy')
        tempo = customization.get('tempo', 'medium')
        key = customization.get('key', 'C')
        
        # Create MIDI file
        midi = MIDIFile(1)  # One track
        track = 0
        channel = 0
        time = 0
        
        # Set tempo
        tempo_bpm = self.tempo_map.get(tempo, 120)
        midi.addTempo(track, time, tempo_bpm)
        
        # Get scale for genre
        scale = self.genre_scales.get(genre, self.genre_scales['pop'])
        root_note = self.key_map.get(key, 0)
        
        # Generate melody
        duration = 32  # bars
        beats_per_bar = 4
        total_beats = duration * beats_per_bar
        
        current_time = 0
        octave = 5
        
        for _ in range(total_beats):
            # Choose note from scale
            scale_degree = random.choice(scale)
            pitch = root_note + scale_degree + (octave * 12)
            
            # Vary duration
            note_duration = random.choice([0.5, 1, 2])
            
            # Vary volume based on mood
            if mood in ['energetic', 'happy', 'uplifting']:
                volume = random.randint(90, 127)
            elif mood in ['calm', 'sad']:
                volume = random.randint(60, 90)
            else:
                volume = random.randint(70, 100)
            
            midi.addNote(track, channel, pitch, current_time, note_duration, volume)
            current_time += note_duration
        
        # Add bass line
        bass_channel = 1
        current_time = 0
        bass_octave = 3
        
        for i in range(duration):
            bass_note = root_note + (bass_octave * 12)
            midi.addNote(track, bass_channel, bass_note, current_time, 4, 80)
            current_time += 4
        
        # Save MIDI file
        import time as time_module
        filename = f"song_{int(time_module.time())}_{genre}.mid"
        filepath = OUTPUT_DIR / filename
        
        with open(filepath, "wb") as output_file:
            midi.writeFile(output_file)
        
        return f"songs/{filename}"
