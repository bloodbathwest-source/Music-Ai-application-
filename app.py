# -*- coding: utf-8 -*-
"""
Music AI Application - Main Flask Application
A music AI that evolves after use, creating songs, pictures, videos, lyrics, and artist names.
"""

import os
import json
import random
import time
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory
from pathlib import Path

from music_generator import MusicGenerator
from image_generator import ImageGenerator
from lyrics_generator import LyricsGenerator
from artist_generator import ArtistGenerator
from evolution_engine import EvolutionEngine

app = Flask(__name__)

# Configuration
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Initialize generators
music_gen = MusicGenerator()
image_gen = ImageGenerator()
lyrics_gen = LyricsGenerator()
artist_gen = ArtistGenerator()
evolution_engine = EvolutionEngine()


@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def generate_content():
    """
    Generate music content based on user parameters.
    
    Expects JSON with:
    - quantity: number of items to generate
    - content_types: list of content types (song, picture, video, lyrics, artist)
    - customization: dict of customization options
    """
    try:
        data = request.json
        quantity = data.get('quantity', 1)
        content_types = data.get('content_types', ['song', 'lyrics', 'artist'])
        customization = data.get('customization', {})
        
        results = []
        
        for i in range(quantity):
            item_result = {
                'id': f"{int(time.time())}_{i}",
                'timestamp': datetime.now().isoformat(),
                'customization': customization
            }
            
            # Generate artist name
            if 'artist' in content_types:
                artist_name = artist_gen.generate(customization)
                item_result['artist'] = artist_name
            
            # Generate lyrics
            if 'lyrics' in content_types:
                lyrics = lyrics_gen.generate(customization)
                item_result['lyrics'] = lyrics
                item_result['lyrics_file'] = save_lyrics(lyrics, item_result['id'])
            
            # Generate song
            if 'song' in content_types:
                song_file = music_gen.generate(customization)
                item_result['song'] = song_file
            
            # Generate picture/album art
            if 'picture' in content_types:
                image_file = image_gen.generate(customization)
                item_result['picture'] = image_file
            
            # Generate video (placeholder for now)
            if 'video' in content_types:
                video_file = generate_video_placeholder(customization)
                item_result['video'] = video_file
            
            results.append(item_result)
            
            # Update evolution engine with generation data
            evolution_engine.record_generation(item_result)
        
        # Evolve the AI based on accumulated data
        evolution_engine.evolve()
        
        return jsonify({
            'success': True,
            'results': results,
            'evolution_score': evolution_engine.get_score()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/customization-options', methods=['GET'])
def get_customization_options():
    """Get available customization options."""
    return jsonify({
        'genres': ['pop', 'rock', 'jazz', 'classical', 'electronic', 'hip-hop', 'country', 'blues'],
        'moods': ['happy', 'sad', 'energetic', 'calm', 'romantic', 'dark', 'uplifting'],
        'tempos': ['slow', 'medium', 'fast', 'variable'],
        'keys': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
        'styles': ['acoustic', 'electric', 'orchestral', 'synthetic', 'mixed']
    })


@app.route('/api/evolution-stats', methods=['GET'])
def get_evolution_stats():
    """Get current evolution statistics."""
    return jsonify(evolution_engine.get_stats())


@app.route('/output/<path:filename>')
def serve_output(filename):
    """Serve generated output files."""
    return send_from_directory(OUTPUT_DIR, filename)


def save_lyrics(lyrics, item_id):
    """Save lyrics to a text file."""
    filename = f"lyrics_{item_id}.txt"
    filepath = OUTPUT_DIR / filename
    with open(filepath, 'w') as f:
        f.write(lyrics)
    return filename


def generate_video_placeholder(customization):
    """Generate video placeholder (to be implemented with actual video generation)."""
    # For now, return a placeholder
    return "video_placeholder.mp4"


if __name__ == '__main__':
    # Create necessary directories
    (OUTPUT_DIR / "songs").mkdir(exist_ok=True)
    (OUTPUT_DIR / "images").mkdir(exist_ok=True)
    (OUTPUT_DIR / "videos").mkdir(exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
