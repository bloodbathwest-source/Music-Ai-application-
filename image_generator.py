"""
Image Generator Module
Generates album art and pictures with customizable parameters.
"""

import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time

OUTPUT_DIR = Path("output/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class ImageGenerator:
    """Generate album art and images."""
    
    def __init__(self):
        self.color_schemes = {
            'happy': [(255, 223, 0), (255, 140, 0), (255, 69, 0)],  # Warm yellows/oranges
            'sad': [(70, 130, 180), (25, 25, 112), (72, 61, 139)],  # Blues/purples
            'energetic': [(255, 0, 0), (255, 165, 0), (255, 255, 0)],  # Bright reds/oranges
            'calm': [(173, 216, 230), (176, 224, 230), (135, 206, 235)],  # Light blues
            'romantic': [(255, 182, 193), (255, 105, 180), (219, 112, 147)],  # Pinks
            'dark': [(0, 0, 0), (50, 50, 50), (100, 100, 100)],  # Grays/blacks
            'uplifting': [(255, 215, 0), (255, 255, 255), (255, 228, 181)]  # Golds/whites
        }
        
        self.genre_patterns = {
            'pop': 'circles',
            'rock': 'angular',
            'jazz': 'waves',
            'classical': 'symmetrical',
            'electronic': 'grid',
            'hip-hop': 'graffiti',
            'country': 'organic',
            'blues': 'waves'
        }
    
    def generate(self, customization):
        """
        Generate an album art image.
        
        Args:
            customization: dict with genre, mood, style
            
        Returns:
            str: filename of generated image
        """
        genre = customization.get('genre', 'pop')
        mood = customization.get('mood', 'happy')
        
        # Create image
        width, height = 800, 800
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        
        # Get color scheme
        colors = self.color_schemes.get(mood, self.color_schemes['happy'])
        
        # Fill background with gradient
        for y in range(height):
            color_index = int((y / height) * (len(colors) - 1))
            color = colors[color_index]
            draw.line([(0, y), (width, y)], fill=color)
        
        # Add pattern based on genre
        pattern = self.genre_patterns.get(genre, 'circles')
        
        if pattern == 'circles':
            for _ in range(20):
                x = random.randint(0, width)
                y = random.randint(0, height)
                radius = random.randint(20, 100)
                color = random.choice(colors)
                draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                           fill=color, outline=None)
        
        elif pattern == 'angular':
            for _ in range(15):
                points = [
                    (random.randint(0, width), random.randint(0, height)),
                    (random.randint(0, width), random.randint(0, height)),
                    (random.randint(0, width), random.randint(0, height))
                ]
                color = random.choice(colors)
                draw.polygon(points, fill=color)
        
        elif pattern == 'waves':
            for i in range(0, height, 50):
                points = []
                for x in range(0, width, 20):
                    y = i + 25 * (1 + abs(hash(str(x+i)) % 100 - 50) / 50)
                    points.append((x, y))
                color = random.choice(colors)
                for j in range(len(points) - 1):
                    draw.line([points[j], points[j+1]], fill=color, width=3)
        
        elif pattern == 'grid':
            grid_size = 50
            for x in range(0, width, grid_size):
                for y in range(0, height, grid_size):
                    if random.random() > 0.5:
                        color = random.choice(colors)
                        draw.rectangle([x, y, x+grid_size, y+grid_size], 
                                     fill=color)
        
        else:  # default circles
            for _ in range(15):
                x = random.randint(0, width)
                y = random.randint(0, height)
                radius = random.randint(30, 80)
                color = random.choice(colors)
                draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                           fill=color, outline=None)
        
        # Add text overlay
        try:
            # Try to use default font, fallback to basic if not available
            font_size = 60
            text = genre.upper()
            text_bbox = draw.textbbox((0, 0), text)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (width - text_width) // 2
            text_y = height - text_height - 50
            
            # Draw text with shadow
            shadow_offset = 3
            draw.text((text_x + shadow_offset, text_y + shadow_offset), 
                     text, fill=(0, 0, 0, 128))
            draw.text((text_x, text_y), text, fill=(255, 255, 255))
        except:
            pass  # Skip text if font issues
        
        # Save image
        filename = f"art_{int(time.time())}_{genre}.png"
        filepath = OUTPUT_DIR / filename
        image.save(filepath, 'PNG')
        
        return f"images/{filename}"
