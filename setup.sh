#!/bin/bash

# Exit on error
set -e

echo "Setting up Python virtual environment for Weather MCP Server..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete!"
echo "To activate the environment manually, run: source .venv/bin/activate"
echo "To run the MCP server, you can use the debugger in VSCode or run: python weather_mcp_demo.py"
