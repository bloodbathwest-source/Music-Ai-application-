"""
Artist Generator Module
Generates artist names with customizable parameters.
"""

import random


class ArtistGenerator:
    """Generate artist names based on genre and style."""
    
    def __init__(self):
        self.prefixes = [
            'DJ', 'MC', 'Lil', 'Big', 'The', 'Young', 'Old', 'Major', 'Minor',
            'King', 'Queen', 'Prince', 'Lady', 'Sir', 'Captain', 'Professor'
        ]
        
        self.first_names = [
            'Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Avery',
            'Phoenix', 'Sage', 'River', 'Sky', 'Storm', 'Raven', 'Luna',
            'Nova', 'Atlas', 'Orion', 'Echo', 'Kai', 'Zara', 'Indie', 'Blaze'
        ]
        
        self.last_names = [
            'Steel', 'Stone', 'Fire', 'Ice', 'Storm', 'Rain', 'Thunder', 'Lightning',
            'Shadow', 'Light', 'Moon', 'Star', 'Sun', 'Wolf', 'Eagle', 'Lion',
            'Dragon', 'Phoenix', 'Raven', 'Fox', 'Bear', 'Hawk'
        ]
        
        self.band_words = [
            'Electric', 'Cosmic', 'Neon', 'Crystal', 'Velvet', 'Golden', 'Silver',
            'Midnight', 'Morning', 'Sunset', 'Sonic', 'Psychic', 'Magic', 'Wild',
            'Sacred', 'Ancient', 'Future', 'Digital', 'Analog', 'Retro'
        ]
        
        self.band_nouns = [
            'Dreams', 'Echoes', 'Voices', 'Souls', 'Hearts', 'Minds', 'Spirits',
            'Angels', 'Demons', 'Knights', 'Warriors', 'Prophets', 'Wanderers',
            'Rebels', 'Kings', 'Queens', 'Wizards', 'Legends', 'Heroes'
        ]
        
        self.genre_styles = {
            'pop': ['solo', 'duo'],
            'rock': ['band', 'solo'],
            'jazz': ['ensemble', 'solo', 'trio'],
            'classical': ['ensemble', 'solo'],
            'electronic': ['solo', 'duo'],
            'hip-hop': ['solo', 'crew'],
            'country': ['solo', 'band'],
            'blues': ['solo', 'band']
        }
    
    def generate(self, customization):
        """
        Generate an artist name.
        
        Args:
            customization: dict with genre, style
            
        Returns:
            str: generated artist name
        """
        genre = customization.get('genre', 'pop')
        
        # Determine artist type based on genre
        artist_types = self.genre_styles.get(genre, ['solo', 'band'])
        artist_type = random.choice(artist_types)
        
        if artist_type in ['solo', 'duo']:
            # Generate solo artist or duo name
            name_style = random.choice(['prefix_name', 'name_lastname', 'single_name'])
            
            if name_style == 'prefix_name':
                prefix = random.choice(self.prefixes)
                name = random.choice(self.first_names)
                return f"{prefix} {name}"
            
            elif name_style == 'name_lastname':
                first = random.choice(self.first_names)
                last = random.choice(self.last_names)
                return f"{first} {last}"
            
            else:  # single_name
                return random.choice(self.first_names)
        
        elif artist_type == 'trio':
            # Generate trio name
            first = random.choice(self.first_names)
            return f"The {first} Trio"
        
        elif artist_type == 'crew':
            # Generate hip-hop crew name
            word = random.choice(self.band_words)
            noun = random.choice(self.band_nouns)
            return f"{word} {noun} Crew"
        
        elif artist_type == 'ensemble':
            # Generate ensemble name
            word = random.choice(self.band_words)
            return f"{word} Ensemble"
        
        else:  # band
            # Generate band name
            style = random.choice(['adjective_noun', 'the_noun', 'compound'])
            
            if style == 'adjective_noun':
                adj = random.choice(self.band_words)
                noun = random.choice(self.band_nouns)
                return f"{adj} {noun}"
            
            elif style == 'the_noun':
                noun = random.choice(self.band_nouns)
                return f"The {noun}"
            
            else:  # compound
                word1 = random.choice(self.first_names)
                word2 = random.choice(self.last_names)
                return f"{word1}{word2}"
