#!/usr/bin/env python3
"""
Quick test script to verify the MCP server works
"""

import asyncio
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the directory to path so we can import the server
sys.path.insert(0, os.path.dirname(__file__))

async def test_server():
    """Test basic server functionality"""
    print("Testing MCP Music Server...")
    print("-" * 50)

    # Verify credentials are loaded from environment
    if "SPOTIFY_CLIENT_ID" not in os.environ or "SPOTIFY_CLIENT_SECRET" not in os.environ:
        print("[ERROR] Missing Spotify credentials!")
        print("Please create a .env file with your Spotify credentials.")
        print("See .env.example for the template.")
        return False

    try:
        # Import the server
        import music_server_updated_2025 as server

        print("[OK] Server module loaded successfully")
        print(f"[OK] Server name: {server.app.name}")

        # Test listing tools
        tools = await server.list_tools()
        print(f"[OK] Found {len(tools)} tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description[:60]}...")

        # Test listing resources
        resources = await server.list_resources()
        print(f"\n[OK] Found {len(resources)} resources:")
        for resource in resources:
            print(f"  - {resource.name}: {resource.description}")

        print("\n" + "=" * 50)
        print("SUCCESS! Your MCP server is working correctly!")
        print("=" * 50)

    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

if __name__ == "__main__":
    result = asyncio.run(test_server())
    sys.exit(0 if result else 1)
