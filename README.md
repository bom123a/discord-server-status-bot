# Discord Status Bot

This bot updates the names of voice channels in Discord to display current member statistics (total members, bots, and users with a specific role).

## Features
- Updates voice channel names every 5 minutes
- Displays total member and bot counts
- Counts users with a specific role (e.g., "Staff")

## Requirements
- Python 3.x
- discord.py library

Configuration
Create a file named config.json in the root directory of the project and add the following structure:

- Replace YOUR_BOT_TOKEN with the actual bot token from the Discord Developer Portal.
- Replace YOUR_GUILD_ID with the ID of your server (guild).
- Replace the other placeholders with the appropriate voice channel and role IDs for your server.
- Ensure the bot has permission to manage voice channels.
