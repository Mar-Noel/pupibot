from discord.ext import commands
import pygetwindow as gw
from discord.ext import commands

import discord
import subprocess



def setup_minecraft_commands(bot):
    # Comandos viejos
    @bot.command()
    async def pupi(ctx):
        await bot.change_presence(status=discord.Status.idle)