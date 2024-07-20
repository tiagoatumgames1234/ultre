import discord
from discord.ext import commands
import os
from config import BOT_TOKEN

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the intent to receive message content
intents.members = True 

# Create bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await load_extensions()

async def load_extensions():
    print("Loading extensions...")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                print(f"Attempting to load extension: {filename[:-3]}")
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {filename[:-3]}: {e}")

bot.run(BOT_TOKEN)
