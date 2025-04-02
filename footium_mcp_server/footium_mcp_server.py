#!/usr/bin/env python3
import asyncio
from typing import Dict, Any

from mcp.server.fastmcp import FastMCP
from footium_client import FootiumClient

# Initialize FastMCP server with name "footium"
mcp = FastMCP("footium")

# Initialize Footium GraphQL client
client = FootiumClient()

# Define example resources based on expected Footium GraphQL API
# Note: These are example implementations that should be updated after running schema introspection


@mcp.resource("footium://club/{club_id}")
async def get_club(club_id: str) -> Dict[str, Any]:
    """
    Get information about a specific Footium club.

    Args:
        club_id: The ID of the club to retrieve
    """
    query = """
    query GetClub($id: ClubWhereUniqueInput!) {
      club(where: $id) {
        id
        name
        city
        abbreviation
        description
        owner {
          id
          address
        }
        stadiumId
        stadium {
          id
          name
          capacity
        }
        players {
          id
          fullName
          nationality
          rarity
        }
        stats {
          points
          wins
          draws
          losses
          goals
          goalsAgainst
        }
      }
    }
    """
    variables = {"id": {"id": int(club_id)}}

    try:
        result = await client.execute(query, variables)
        return result.get("data", {}).get("club", {})
    except Exception as e:
        return {"error": f"Failed to fetch club data: {str(e)}"}


@mcp.resource("footium://clubs")
async def get_clubs() -> Dict[str, Any]:
    """Get a list of Footium clubs."""
    query = """
    query GetClubs {
      clubs(take: 10) {
        id
        name
        city
        abbreviation
        stadiumId
        owner {
          id
          address
        }
      }
    }
    """

    try:
        result = await client.execute(query)
        return result.get("data", {}).get("clubs", [])
    except Exception as e:
        return {"error": f"Failed to fetch clubs: {str(e)}"}


@mcp.resource("footium://player/{player_id}")
async def get_player(player_id: str) -> Dict[str, Any]:
    """
    Get information about a specific Footium player.

    Args:
        player_id: The ID of the player to retrieve
    """
    query = """
    query GetPlayer($id: PlayerWhereUniqueInput!) {
      player(where: $id) {
        id
        fullName
        firstName
        lastName
        nationality
        isAcademy
        rarity
        creationRating
        potential
        club {
          id
          name
        }
        playerAttributes(where: {isLatest: true}) {
          id
          age
          footedness
          condition
          stamina
          leadership
        }
        positionalRating(where: {isLatest: true}) {
          position
          rating
        }
      }
    }
    """
    variables = {"id": {"id": player_id}}

    try:
        result = await client.execute(query, variables)
        return result.get("data", {}).get("player", {})
    except Exception as e:
        return {"error": f"Failed to fetch player data: {str(e)}"}


@mcp.resource("footium://match/{match_id}")
async def get_match(match_id: str) -> Dict[str, Any]:
    """
    Get information about a specific Footium match.

    Args:
        match_id: The ID of the match to retrieve
    """
    query = """
    query GetMatch($id: MatchWhereUniqueInput!) {
      match(where: $id) {
        id
        seed
        startTimestamp
        state
        isResultProcessed
        timestamp
        homeTeam
        awayTeam
        fixture {
          id
          date
          isNeutralVenue
          state
          clubFixtures {
            club {
              id
              name
            }
            isHome
          }
        }
      }
    }
    """
    variables = {"id": {"id": match_id}}

    try:
        result = await client.execute(query, variables)
        return result.get("data", {}).get("match", {})
    except Exception as e:
        return {"error": f"Failed to fetch match data: {str(e)}"}


# No need for a separate async function - just run directly
if __name__ == "__main__":
    # Run the server with stdio transport
    mcp.run(transport="stdio")
