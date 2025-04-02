# Footium MCP Server

A Python-based Model Context Protocol (MCP) server that provides access to Footium's GraphQL API. This server enables Claude and other MCP-compatible AI assistants to fetch data from Footium.

## Features

- Connect to Footium's GraphQL API
- Expose Footium data as MCP resources
- Auto-generate resource templates based on GraphQL schema introspection
- Read-only access to Footium clubs, players, matches, and more

## Setup

### Prerequisites

- Python 3.7+
- pip or conda for package management

### Installation

1. Clone this repository or navigate to the project directory:

```bash
cd footium_mcp_server
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

#### Schema Introspection

Before running the server, you can use the schema introspection tool to discover what's available in the Footium GraphQL API:

```bash
python schema_introspection.py
```

This will:
- Fetch the GraphQL schema from Footium's API
- Save it as `schema.json` and `schema.graphql`
- Analyze available queries and generate template resources
- Output a `mcp_resources_template.py` file with generated resource code

#### Running the Server

To start the MCP server:

```bash
python footium_mcp_server.py
```

#### Integrating with Claude Desktop

To integrate with Claude Desktop:

1. Edit your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. Add the Footium MCP server configuration:

```json
{
    "mcpServers": {
        "footium": {
            "command": "python",
            "args": [
                "/absolute/path/to/footium_mcp_server/footium_mcp_server.py"
            ],
            "env": {},
            "disabled": false,
            "autoApprove": []
        }
    }
}
```

Replace `/absolute/path/to/` with the actual path to your server.

3. Restart Claude Desktop

## Available Resources

Once integrated, Claude will have access to these resources:

- `footium://club/{club_id}` - Get information about a specific club
- `footium://clubs` - Get a list of clubs
- `footium://player/{player_id}` - Get information about a specific player
- `footium://match/{match_id}` - Get information about a specific match

You can ask Claude to retrieve this information with natural language, for example:
- "What division is club 42 in Footium?"
- "Tell me about player 123 in Footium"

## Development

### Project Structure

- `footium_client.py` - GraphQL client for communicating with Footium's API
- `schema_introspection.py` - Tools for introspecting and analyzing the GraphQL schema
- `footium_mcp_server.py` - Main MCP server implementation

### Extending

To add new resources:

1. Run schema introspection to explore available queries
2. Implement additional resources in `footium_mcp_server.py`
3. Restart the server and Claude Desktop
