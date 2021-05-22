import discord
import json
import datetime
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

prefix = config.get('prefix')

class Ping(commands.Cog):
    def __init__(self, softy):
        self.softy = softy

    @commands.Cog.listener()

    async def on_ready(self):
        print('Ping Cog Loaded Succesfully')
        
# Your command(s) here

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong!")

# End of your command(s) here

def setup(softy):
    softy.add_cog(Ping(softy))
