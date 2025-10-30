// Music AI Application - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const loadingDiv = document.getElementById('loading');
    const resultsDiv = document.getElementById('results');
    
    // Load evolution stats on page load
    loadEvolutionStats();
    
    // Generate button click handler
    generateBtn.addEventListener('click', generateContent);
    
    async function generateContent() {
        // Get form values
        const quantity = parseInt(document.getElementById('quantity').value);
        
        // Get selected content types
        const contentTypes = [];
        document.querySelectorAll('input[name="content_type"]:checked').forEach(checkbox => {
            contentTypes.push(checkbox.value);
        });
        
        if (contentTypes.length === 0) {
            alert('Please select at least one content type!');
            return;
        }
        
        // Get customization options
        const customization = {
            genre: document.getElementById('genre').value,
            mood: document.getElementById('mood').value,
            tempo: document.getElementById('tempo').value,
            key: document.getElementById('key').value,
            style: document.getElementById('style').value
        };
        
        // Prepare request
        const requestData = {
            quantity: quantity,
            content_types: contentTypes,
            customization: customization
        };
        
        // Show loading state
        generateBtn.disabled = true;
        loadingDiv.style.display = 'block';
        
        try {
            // Make API request
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Display results
                displayResults(data.results);
                
                // Update evolution score
                document.getElementById('evolution-score').textContent = data.evolution_score;
                
                // Reload stats
                loadEvolutionStats();
            } else {
                alert('Error generating content: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error generating content. Please try again.');
        } finally {
            // Hide loading state
            generateBtn.disabled = false;
            loadingDiv.style.display = 'none';
        }
    }
    
    function displayResults(results) {
        // Clear previous results
        resultsDiv.innerHTML = '';
        
        // Display each result
        results.forEach((result, index) => {
            const card = document.createElement('div');
            card.className = 'result-card';
            
            let html = `<h4>Generation ${index + 1}</h4>`;
            
            // Display artist name
            if (result.artist) {
                html += `<div class="artist-name">🎤 ${result.artist}</div>`;
            }
            
            // Display metadata
            html += `<div class="meta">
                Genre: ${result.customization.genre} | 
                Mood: ${result.customization.mood}
            </div>`;
            
            // Display album art
            if (result.picture) {
                html += `<div class="content">
                    <img src="/output/${result.picture}" alt="Album Art">
                </div>`;
            }
            
            // Display lyrics preview
            if (result.lyrics) {
                const lyricsPreview = result.lyrics.substring(0, 300) + '...';
                html += `<div class="content">
                    <div class="lyrics-preview">${escapeHtml(lyricsPreview)}</div>
                </div>`;
            }
            
            // Download links
            html += '<div class="content">';
            
            if (result.song) {
                html += `<a href="/output/${result.song}" class="download-link" download>⬇ Download Song</a>`;
            }
            
            if (result.lyrics_file) {
                html += `<a href="/output/${result.lyrics_file}" class="download-link" download>⬇ Download Lyrics</a>`;
            }
            
            if (result.picture) {
                html += `<a href="/output/${result.picture}" class="download-link" download>⬇ Download Art</a>`;
            }
            
            html += '</div>';
            
            card.innerHTML = html;
            resultsDiv.appendChild(card);
        });
    }
    
    async function loadEvolutionStats() {
        try {
            const response = await fetch('/api/evolution-stats');
            const stats = await response.json();
            
            // Update stats display
            document.getElementById('stat-total').textContent = stats.total_generations;
            document.getElementById('stat-genre').textContent = 
                stats.preferred_genre !== 'unknown' ? stats.preferred_genre : '-';
            document.getElementById('stat-mood').textContent = 
                stats.preferred_mood !== 'unknown' ? stats.preferred_mood : '-';
            document.getElementById('stat-evolution').textContent = stats.evolution_score;
            document.getElementById('evolution-score').textContent = stats.evolution_score;
        } catch (error) {
            console.error('Error loading stats:', error);
        }
    }
    
    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
});
