"""
Evolution Engine Module
Manages the AI's learning and evolution based on usage patterns.
"""

import json
from pathlib import Path
from datetime import datetime


class EvolutionEngine:
    """Track and evolve AI based on usage patterns."""
    
    def __init__(self):
        self.stats_file = Path("evolution_stats.json")
        self.stats = self._load_stats()
        
    def _load_stats(self):
        """Load evolution statistics from file."""
        if self.stats_file.exists():
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        else:
            return {
                'total_generations': 0,
                'genre_counts': {},
                'mood_counts': {},
                'tempo_counts': {},
                'evolution_score': 0,
                'generation_history': []
            }
    
    def _save_stats(self):
        """Save evolution statistics to file."""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def record_generation(self, generation_data):
        """
        Record a content generation event.
        
        Args:
            generation_data: dict with generation metadata
        """
        customization = generation_data.get('customization', {})
        
        # Increment total generations
        self.stats['total_generations'] += 1
        
        # Track genre preferences
        genre = customization.get('genre', 'unknown')
        self.stats['genre_counts'][genre] = self.stats['genre_counts'].get(genre, 0) + 1
        
        # Track mood preferences
        mood = customization.get('mood', 'unknown')
        self.stats['mood_counts'][mood] = self.stats['mood_counts'].get(mood, 0) + 1
        
        # Track tempo preferences
        tempo = customization.get('tempo', 'unknown')
        self.stats['tempo_counts'][tempo] = self.stats['tempo_counts'].get(tempo, 0) + 1
        
        # Add to history (keep last 100)
        self.stats['generation_history'].append({
            'timestamp': generation_data.get('timestamp'),
            'genre': genre,
            'mood': mood,
            'tempo': tempo
        })
        
        if len(self.stats['generation_history']) > 100:
            self.stats['generation_history'] = self.stats['generation_history'][-100:]
    
    def evolve(self):
        """
        Evolve the AI based on accumulated data.
        Updates evolution score and learns from patterns.
        """
        # Calculate evolution score based on generations
        total = self.stats['total_generations']
        
        # Evolution score increases with usage
        # Every 10 generations increases score by 1
        base_score = total // 10
        
        # Bonus for diversity - using multiple genres/moods
        genre_diversity = len(self.stats['genre_counts'])
        mood_diversity = len(self.stats['mood_counts'])
        diversity_bonus = (genre_diversity + mood_diversity) // 2
        
        # Calculate final score
        self.stats['evolution_score'] = base_score + diversity_bonus
        
        # Determine preferred styles for recommendations
        if self.stats['genre_counts']:
            most_common_genre = max(self.stats['genre_counts'].items(), 
                                   key=lambda x: x[1])[0]
            self.stats['preferred_genre'] = most_common_genre
        
        if self.stats['mood_counts']:
            most_common_mood = max(self.stats['mood_counts'].items(), 
                                  key=lambda x: x[1])[0]
            self.stats['preferred_mood'] = most_common_mood
        
        # Save updated stats
        self._save_stats()
    
    def get_score(self):
        """Get current evolution score."""
        return self.stats['evolution_score']
    
    def get_stats(self):
        """Get all evolution statistics."""
        return {
            'total_generations': self.stats['total_generations'],
            'evolution_score': self.stats['evolution_score'],
            'genre_counts': self.stats['genre_counts'],
            'mood_counts': self.stats['mood_counts'],
            'tempo_counts': self.stats['tempo_counts'],
            'preferred_genre': self.stats.get('preferred_genre', 'unknown'),
            'preferred_mood': self.stats.get('preferred_mood', 'unknown'),
            'recent_generations': self.stats['generation_history'][-10:]
        }
    
    def get_recommendations(self):
        """
        Get AI recommendations based on learned patterns.
        
        Returns:
            dict: recommended customization options
        """
        recommendations = {}
        
        if self.stats.get('preferred_genre'):
            recommendations['genre'] = self.stats['preferred_genre']
        
        if self.stats.get('preferred_mood'):
            recommendations['mood'] = self.stats['preferred_mood']
        
        # Suggest tempo based on most common choice
        if self.stats['tempo_counts']:
            most_common_tempo = max(self.stats['tempo_counts'].items(), 
                                   key=lambda x: x[1])[0]
            recommendations['tempo'] = most_common_tempo
        
        return recommendations
