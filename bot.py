import discord
import json
import os
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

softy = commands.Bot(command_prefix=prefix)

softy.remove_command("help")

@softy.event
async def on_ready():
    print('Bot is ready')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        softy.load_extension(f'cogs.{filename[:-3]}')

softy.run(token)
