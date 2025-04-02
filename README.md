# Weather MCP Server

This is a Python implementation of a Model Context Protocol (MCP) server that provides weather information tools.

## Features

- `get_alerts`: Retrieve weather alerts for a US state
- `get_forecast`: Get weather forecast for a specific location using latitude and longitude

## Setup

1. Run the setup script to create a virtual environment and install dependencies:

```bash
./setup.sh
```

2. Open the project in VSCode, which will use the provided configuration:
   - `.vscode/launch.json`: Configures the debugger
   - `.vscode/settings.json`: Sets up Python linting and formatting

## Usage

### Running in VSCode

1. Open the project in VSCode
2. Select the "Run and Debug" tab (or press `Ctrl+Shift+D`)
3. Choose "Python: Weather MCP Server" from the dropdown
4. Click the play button or press F5 to start the server

### Running from Terminal

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the server
python weather_mcp_demo.py
```

## Integration with Claude or other MCP Clients

To use this server with Claude:

1. Add the server to Claude's MCP configuration
2. Configure the command to run the server
3. Use the provided tools through Claude's interface

## Available Tools

### get_alerts

Get weather alerts for a US state.

**Parameters:**
- `state`: Two-letter US state code (e.g., CA, NY)

### get_forecast

Get weather forecast for a location.

**Parameters:**
- `latitude`: Latitude of the location
- `longitude`: Longitude of the location
