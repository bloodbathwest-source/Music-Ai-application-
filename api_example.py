#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example script demonstrating programmatic use of the Music AI Application API.

This script shows how to generate content using the REST API without the web interface.
Run the Flask app first with: python app.py
Then run this script: python api_example.py
"""

import requests
import json
import time


def generate_music(quantity=1, genres=None, moods=None):
    """
    Generate music content using the API.
    
    Args:
        quantity: Number of items to generate
        genres: List of genres to try (or None for default)
        moods: List of moods to try (or None for default)
    """
    api_url = "http://localhost:5000/api/generate"
    
    if genres is None:
        genres = ['pop']
    if moods is None:
        moods = ['happy']
    
    print(f"🎵 Music AI API Example")
    print(f"=" * 50)
    print()
    
    # Generate content for each genre/mood combination
    for genre in genres:
        for mood in moods:
            print(f"Generating {quantity} item(s) - Genre: {genre}, Mood: {mood}")
            
            # Prepare request data
            request_data = {
                "quantity": quantity,
                "content_types": ["song", "lyrics", "artist", "picture"],
                "customization": {
                    "genre": genre,
                    "mood": mood,
                    "tempo": "medium",
                    "key": "C",
                    "style": "electric"
                }
            }
            
            try:
                # Make API request
                response = requests.post(api_url, json=request_data)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if data.get('success'):
                        print(f"✓ Successfully generated {len(data['results'])} item(s)")
                        print(f"  Evolution Score: {data['evolution_score']}")
                        
                        # Display results
                        for i, result in enumerate(data['results'], 1):
                            print(f"\n  Item {i}:")
                            if 'artist' in result:
                                print(f"    Artist: {result['artist']}")
                            if 'song' in result:
                                print(f"    Song: {result['song']}")
                            if 'picture' in result:
                                print(f"    Picture: {result['picture']}")
                            if 'lyrics_file' in result:
                                print(f"    Lyrics: {result['lyrics_file']}")
                    else:
                        print(f"✗ Error: {data.get('error', 'Unknown error')}")
                else:
                    print(f"✗ HTTP Error {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                print("✗ Error: Cannot connect to API. Is the Flask app running?")
                return
            except Exception as e:
                print(f"✗ Error: {e}")
            
            print()
            time.sleep(1)  # Brief pause between requests


def get_evolution_stats():
    """Get and display evolution statistics."""
    stats_url = "http://localhost:5000/api/evolution-stats"
    
    try:
        response = requests.get(stats_url)
        
        if response.status_code == 200:
            stats = response.json()
            
            print("📊 Evolution Statistics")
            print("=" * 50)
            print(f"Total Generations: {stats['total_generations']}")
            print(f"Evolution Score: {stats['evolution_score']}")
            print(f"Preferred Genre: {stats['preferred_genre']}")
            print(f"Preferred Mood: {stats['preferred_mood']}")
            print()
            
            if stats.get('genre_counts'):
                print("Genre Distribution:")
                for genre, count in sorted(stats['genre_counts'].items(), 
                                          key=lambda x: x[1], reverse=True):
                    print(f"  {genre}: {count}")
                print()
            
            if stats.get('mood_counts'):
                print("Mood Distribution:")
                for mood, count in sorted(stats['mood_counts'].items(), 
                                         key=lambda x: x[1], reverse=True):
                    print(f"  {mood}: {count}")
                print()
                
        else:
            print(f"Error getting stats: HTTP {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to API. Is the Flask app running?")
    except Exception as e:
        print(f"Error: {e}")


def get_customization_options():
    """Get available customization options from the API."""
    options_url = "http://localhost:5000/api/customization-options"
    
    try:
        response = requests.get(options_url)
        
        if response.status_code == 200:
            options = response.json()
            
            print("⚙️  Available Customization Options")
            print("=" * 50)
            print(f"Genres: {', '.join(options['genres'])}")
            print(f"Moods: {', '.join(options['moods'])}")
            print(f"Tempos: {', '.join(options['tempos'])}")
            print(f"Keys: {', '.join(options['keys'])}")
            print(f"Styles: {', '.join(options['styles'])}")
            print()
            
        else:
            print(f"Error getting options: HTTP {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to API. Is the Flask app running?")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function demonstrating various API uses."""
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "Music AI Application - API Example" + " " * 13 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Get available options
    get_customization_options()
    
    # Example 1: Generate a single pop song
    print("Example 1: Single Pop Song")
    print("-" * 50)
    generate_music(quantity=1, genres=['pop'], moods=['happy'])
    
    # Example 2: Generate multiple items with different moods
    print("\nExample 2: Rock Songs with Different Moods")
    print("-" * 50)
    generate_music(quantity=2, genres=['rock'], moods=['energetic', 'dark'])
    
    # Example 3: Jazz variations
    print("\nExample 3: Jazz Variations")
    print("-" * 50)
    generate_music(quantity=1, genres=['jazz'], moods=['calm', 'romantic'])
    
    # Display evolution statistics
    print()
    get_evolution_stats()
    
    print("✅ API Example Complete!")
    print()
    print("Generated files are in the output/ directory:")
    print("  - output/songs/     (MIDI files)")
    print("  - output/images/    (Album art)")
    print("  - output/           (Lyrics)")
    print()


if __name__ == '__main__':
    main()
