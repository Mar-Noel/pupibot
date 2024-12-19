from discord.ext import commands
from comandos_generales import setup_general_commands
from rendimiento import setup_performance_commands
from discord_easy_commands import EasyBot
import discord
import subprocess
import os
import ctypes
import asyncio
import random
import pygetwindow as gw
from discord.ext import commands
from minecraft import setup_minecraft_commands

# Configuración inicial del bot
token = "token"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents)

# Registrar comandos
setup_general_commands(bot)
setup_minecraft_commands(bot)
setup_performance_commands(bot)
#setup_tf2_commands(bot)

# Eventos del bot NO TOCAR 
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



@bot.event
async def on_command_error(ctx, error):
    # Verificar si el error es porque el comando no existe
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"No entendi, Tu madre por si acaso")
    else:
        # Manejar otros errores (opcional)
        await ctx.send(f"❌**error**❌ =>: {str(error)}")

bot.run(token)

#FIN

##ejemplos de como agregar un archivito
#from tf2 import setup_tf2_commands
#setup_tf2_commands(bot)
