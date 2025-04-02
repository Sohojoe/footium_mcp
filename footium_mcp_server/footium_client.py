import httpx
from typing import Dict, Any, Optional


class FootiumClient:
    """Client for interacting with the Footium GraphQL API."""

    def __init__(self, api_url: str = "https://live.api.footium.club/api/graphql"):
        self.api_url = api_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def execute(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute a GraphQL query against the Footium API."""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url, json=payload, headers=self.headers, timeout=10.0
            )
            response.raise_for_status()
            return response.json()
