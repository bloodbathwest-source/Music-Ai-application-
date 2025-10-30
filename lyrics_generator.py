"""
Lyrics Generator Module
Generates song lyrics with customizable parameters.
"""

import random


class LyricsGenerator:
    """Generate song lyrics based on genre and mood."""
    
    def __init__(self):
        # Word banks for different genres and moods
        self.themes = {
            'happy': ['sunshine', 'dancing', 'love', 'summer', 'freedom', 'joy', 'laughter'],
            'sad': ['rain', 'tears', 'goodbye', 'alone', 'memories', 'lost', 'broken'],
            'energetic': ['fire', 'running', 'alive', 'power', 'thunder', 'wild', 'unstoppable'],
            'calm': ['peace', 'silence', 'stars', 'ocean', 'dream', 'gentle', 'whisper'],
            'romantic': ['heart', 'forever', 'together', 'kiss', 'soul', 'destiny', 'passion'],
            'dark': ['shadow', 'night', 'storm', 'chaos', 'abyss', 'fear', 'darkness'],
            'uplifting': ['rise', 'hope', 'believe', 'dream', 'courage', 'light', 'wings']
        }
        
        self.verbs = {
            'happy': ['dance', 'shine', 'smile', 'celebrate', 'fly', 'sing', 'laugh'],
            'sad': ['cry', 'fall', 'fade', 'break', 'miss', 'lose', 'wander'],
            'energetic': ['run', 'jump', 'shout', 'fight', 'burn', 'explode', 'race'],
            'calm': ['breathe', 'float', 'drift', 'rest', 'sleep', 'glide', 'flow'],
            'romantic': ['love', 'hold', 'kiss', 'embrace', 'cherish', 'adore', 'yearn'],
            'dark': ['crawl', 'hide', 'haunt', 'consume', 'fall', 'sink', 'spiral'],
            'uplifting': ['rise', 'soar', 'climb', 'reach', 'grow', 'shine', 'overcome']
        }
        
        self.templates = [
            "In the {theme}, I {verb}",
            "When the {theme} calls, we {verb}",
            "Through the {theme}, I'll {verb}",
            "Let the {theme} {verb} tonight",
            "We {verb} like {theme}",
            "Can you feel the {theme}? We {verb}",
            "Every {theme} makes me {verb}",
            "{theme} and {theme}, we {verb}"
        ]
        
        self.chorus_templates = [
            "Oh, {theme}, {theme}\nWe {verb} and {verb}\n{theme} forever\nTogether we {verb}",
            "{theme} in my heart\n{verb}ing from the start\nNever apart\nWe {verb} and {verb}",
            "Can't stop the {theme}\nWe {verb} all night\n{theme} feels so right\nWe {verb} into the light"
        ]
    
    def generate(self, customization):
        """
        Generate song lyrics.
        
        Args:
            customization: dict with genre, mood
            
        Returns:
            str: generated lyrics
        """
        mood = customization.get('mood', 'happy')
        genre = customization.get('genre', 'pop')
        
        # Get theme and verb lists for the mood
        theme_list = self.themes.get(mood, self.themes['happy'])
        verb_list = self.verbs.get(mood, self.verbs['happy'])
        
        lyrics_parts = []
        
        # Title
        title = f"{random.choice(theme_list).title()} {random.choice(['Dreams', 'Nights', 'Days', 'Hearts', 'Souls'])}"
        lyrics_parts.append(f"=== {title} ===\n")
        
        # Verse 1
        lyrics_parts.append("[Verse 1]")
        for _ in range(4):
            template = random.choice(self.templates)
            line = template.format(
                theme=random.choice(theme_list),
                verb=random.choice(verb_list)
            )
            lyrics_parts.append(line)
        
        lyrics_parts.append("")
        
        # Chorus
        lyrics_parts.append("[Chorus]")
        chorus_template = random.choice(self.chorus_templates)
        chorus = chorus_template.format(
            theme=random.choice(theme_list),
            verb=random.choice(verb_list)
        )
        lyrics_parts.append(chorus)
        
        lyrics_parts.append("")
        
        # Verse 2
        lyrics_parts.append("[Verse 2]")
        for _ in range(4):
            template = random.choice(self.templates)
            line = template.format(
                theme=random.choice(theme_list),
                verb=random.choice(verb_list)
            )
            lyrics_parts.append(line)
        
        lyrics_parts.append("")
        
        # Repeat Chorus
        lyrics_parts.append("[Chorus]")
        lyrics_parts.append(chorus)
        
        lyrics_parts.append("")
        
        # Bridge
        lyrics_parts.append("[Bridge]")
        for _ in range(2):
            template = random.choice(self.templates)
            line = template.format(
                theme=random.choice(theme_list),
                verb=random.choice(verb_list)
            )
            lyrics_parts.append(line)
        
        lyrics_parts.append("")
        
        # Final Chorus
        lyrics_parts.append("[Chorus]")
        lyrics_parts.append(chorus)
        
        return "\n".join(lyrics_parts)
