"""
Simple test script to verify Music AI Application functionality.
"""

import sys
from music_generator import MusicGenerator
from image_generator import ImageGenerator
from lyrics_generator import LyricsGenerator
from artist_generator import ArtistGenerator
from evolution_engine import EvolutionEngine


def test_generators():
    """Test all generators."""
    print("Testing Music AI Application Components...\n")
    
    # Test customization
    customization = {
        'genre': 'pop',
        'mood': 'happy',
        'tempo': 'medium',
        'key': 'C',
        'style': 'electric'
    }
    
    print("1. Testing Music Generator...")
    try:
        music_gen = MusicGenerator()
        song_file = music_gen.generate(customization)
        print(f"   ✓ Generated song: {song_file}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("\n2. Testing Image Generator...")
    try:
        image_gen = ImageGenerator()
        image_file = image_gen.generate(customization)
        print(f"   ✓ Generated image: {image_file}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("\n3. Testing Lyrics Generator...")
    try:
        lyrics_gen = LyricsGenerator()
        lyrics = lyrics_gen.generate(customization)
        print(f"   ✓ Generated lyrics ({len(lyrics)} characters)")
        print(f"   Preview: {lyrics[:100]}...")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("\n4. Testing Artist Generator...")
    try:
        artist_gen = ArtistGenerator()
        artist = artist_gen.generate(customization)
        print(f"   ✓ Generated artist name: {artist}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("\n5. Testing Evolution Engine...")
    try:
        evolution = EvolutionEngine()
        evolution.record_generation({
            'timestamp': '2023-01-01T00:00:00',
            'customization': customization
        })
        evolution.evolve()
        score = evolution.get_score()
        stats = evolution.get_stats()
        print(f"   ✓ Evolution score: {score}")
        print(f"   ✓ Total generations: {stats['total_generations']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("\n✅ All tests passed!")
    return True


if __name__ == '__main__':
    success = test_generators()
    sys.exit(0 if success else 1)
