#!/bin/bash
# Simple run script for Music AI Application

echo "Music AI Application - Starting..."
echo ""
echo "Installing dependencies (if needed)..."
pip install -r requirements.txt --quiet

echo ""
echo "Starting Flask application..."
echo "Access the app at: http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""

python3 app.py
