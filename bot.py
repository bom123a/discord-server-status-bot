import discord
import json
from discord.ext import tasks, commands

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
intents.members = True  # Enables access to server members

bot = commands.Bot(command_prefix="!", intents=intents)

# Task to update voice channel names with member counts
@tasks.loop(minutes=5)
async def update_voice_channels():
    guild = bot.get_guild(config["guild_id"])

    # Calculate total members (excluding bots)
    total_members = len([member for member in guild.members if not member.bot])
    
    # Calculate total bots
    bot_count = len([member for member in guild.members if member.bot])
    
    # Calculate members with the Staff role
    staff_role = guild.get_role(config["staff_role_id"])
    staff_count = len([member for member in guild.members if staff_role in member.roles])

    # Get each channel by ID and update the name
    total_channel = bot.get_channel(config["total_members_channel_id"])
    bot_channel = bot.get_channel(config["bot_count_channel_id"])
    staff_channel = bot.get_channel(config["staff_count_channel_id"])

    await total_channel.edit(name=f"Total Members: {total_members}")
    await bot_channel.edit(name=f"Bots: {bot_count}")
    await staff_channel.edit(name=f"Staff: {staff_count}")

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    update_voice_channels.start()  # Start the periodic update task

# Run the bot with the token from config.json
bot.run(config["token"])
