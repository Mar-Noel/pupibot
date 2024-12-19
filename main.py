from discord.ext import commands
from comandos_generales import setup_general_commands
#from funciones_minecraft import setup_minecraft_commands
from rendimiento import setup_performance_commands
#from tf2 import setup_tf2_commands
from discord_easy_commands import EasyBot
#import pyjokes  # Esto daba error, por eso está comentado
import discord
import subprocess
import os
import ctypes
import asyncio
import random
import pygetwindow as gw
from discord.ext import commands
#from mctools import RCONClient, QUERYClient
from minecraft import setup_minecraft_commands

# Configuración inicial del bot
token = "MTIxMDc4MjM4MjI3ODMyMDE3OA.Gv72yt.qt6Xwpgzee7SxRgmY9dmyMk6Yj8QI1cIcfIVrI"
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

bot.run(token)

#FIN

##ejemplos de como agregar un archivito
#from tf2 import setup_tf2_commands
#setup_tf2_commands(bot)