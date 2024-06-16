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
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {filename[:-3]}: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nuh uh my friend.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("He doesn't exist.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid argument because of your spelling mistake.")
    else:
        await ctx.send(f"An error occurred: {error}")

bot.run(BOT_TOKEN)