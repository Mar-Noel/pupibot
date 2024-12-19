from discord.ext import commands
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


def setup_general_commands(bot):
    @bot.command()
    async def hi(ctx):
        await ctx.send("oliwis")


    @bot.command()
    async def apagar(ctx):
        try:
            subprocess.run(["cmd", "/c", "shutdown", "/s"], check=True)
            await ctx.send("El equipo se apagará en breve.")
            await bot.change_presence(status=discord.Status.idle)
        except subprocess.CalledProcessError:
            await ctx.send("No se pudo apagar el equipo.")

    @bot.command()
    async def apagar_130(ctx):
        tiempo_segundos = 5400  # 1 hora y media en segundos
        try:
            subprocess.run(["shutdown", "/s", "/t", str(tiempo_segundos)], check=True)
            await ctx.send("||El equipo se autodestruira en hora y media💣||")
            await bot.change_presence(status=discord.Status.idle)
        except subprocess.CalledProcessError:
            await ctx.send("No funco mostro")

    @bot.command()
    async def reiniciar(ctx):
        tiempo_segundos = 60
        try:
            subprocess.run(["shutdown","/r","/t", str(tiempo_segundos)], check=True)
            await ctx.send("La workstation se reiniciara en breve")
            await bot.change_presence(status=discord.Status.idle)
        except subprocess.CalledProcessError:
            await ctx.send("Nao funco mostro")

    @bot.command()
    async def comandos(ctx):
        help_message = (
            "Te presento el bot superior.\n"
            "aca esta la lista de todos los comandos rey:\n\n"
            "**- hi:** Saluda al bot.\n"
            "**- lol:** Bañate.\n"
            "**- ip:** Muestra las IPs de los servidores.\n"
            "**- mods:** Proporciona el enlace a la carpeta de mods.\n"
            "**- version:** Muestra las versiones del servidor.\n"
            "**- ayuda:** Te da palabras de apoyo.\n"
            "**- parar:** Cierra el server.\n"
            "**- apagar:** Apaga la Workstation.\n"
            "**- apagar_130:** Apaga la Workstation pero en hora y media.\n"
            "**- jugarvanilla:** Abre el server vanilla.\n"
            # "**- JugarModeado:** Abre el server modeado.\n"
            # "**- jugartf2:** Abre un servidor de tf2.\n"
            # "**- parartf2:** Cierra el servidor de tf2\n"
            "**- Rendimiento:** muestra cuanto sufre la workstation por sus pecados\n"

        )
        await ctx.send(help_message)





    @bot.command()
    async def ayuda(ctx):
        respuestas = [
            "Ni siquiera dios puede ayudarte.",
            "No jodas, estoy de vacaciones.",
            "Arreglatelas solo maquina.",
            "¿Probaste a golpearlo y encenderlo de nuevo?",
            "No se que hacer flaco! soy nuevo en esto...",
            "Me temo que esta es una misión imposible para mí.",
            "¿Ya intentaste buscar en Google?",
            "Creo que necesitas un milagro más que ayuda en este momento.",
            "¡Uy! Esto parece un problemon. Te deseo suerte.",
            "Quizás deberías considerar consultar a mis superiores.",
            "Soy solo un humilde bot, no tengo las respuestas a todo.",
            "¡Oh no! ¡error 404!",
            "¡Eso suena complicado! Tal vez deberías tomar un descanso y volver a intentarlo más tarde.",
            "¡Parece que necesitas más que un bot para resolver este problema!","No puedo hacerlo, soy solo un bot solitario.",
            "No te enteraste pibe, hoy hay paro nacional, yo no laburo.",
            "¡Qué pregunta tan difícil! Yo solo soy un conejo pipipipi.",
            "Mi esfera mágica está en mantenimiento, perdon 👉👈.",
            "¡Ups! Creo que me quedé sin respuestas por el día.",
            "¡El universo está conspirando contra ti!",
            "Siento decir que estoy atrapado en un bucle infinito de preguntas sin respuestas.",
            "Creo que deberías lanzar una moneda al aire y esperar lo mejor.",
            "¡Perdón, pero no tengo suficiente poder de procesamiento para manejar eso!",
            "¿Sabías que los bots también necesitan vacaciones?, ¡No rompas la pija!",
            "*El conejo peronista está tomando un mate y comiendo sanguchitos de migas, no creo que pueda ayudarte ahora.*",
            "https://tenor.com/view/bunny-rabbit-chewing-lettuce-gif-12923124",
            'https://tenor.com/view/rabbit-cute-sweet-wallows-dirt-gif-26930807',
            'https://tenor.com/view/bunny-rabbit-cute-cute-bunny-cute-rabbit-gif-20807147',
            "https://tenor.com/view/black-bunny-gif-11030349",
            "https://tenor.com/view/bunny-black-gif-11030355",
            "https://tenor.com/view/thump-bunny-rabbit-cute-black-rabbit-gif-17706197",
            "https://tenor.com/view/flora-watch-bunny-gamer-fatefm-fablemaidens-gif-14286274",
            "https://tenor.com/view/bunny-steal-mine-rabbit-food-gif-11375225",
            "https://tenor.com/view/kikki-coniglio-bunny-cute-epic-gif-7747893",
            "https://tenor.com/view/bunny-rabbit-black-bunny-black-rabbit-black-lop-bunny-gif-27306002",
            "https://tenor.com/view/blackrabbit-gif-24743126",
            "https://tenor.com/view/bunny-black-bunny-gif-14975208602641646273",
            ]
        respuesta_aleatoria = random.choice(respuestas)
        await ctx.send(respuesta_aleatoria)



    @bot.command()
    async def lol(ctx):
        respuestas = [
            "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGlwbGQwcGZtMnJ1Y3lnc2Vvb2xyaW1yZ3QyaXMzY2FzMzc4bWN4MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13Hj3iy5HhfjGg/giphy.gif",
            "https://tenor.com/es/view/aitor-gif-7084060237011549479",
            "https://giphy.com/gifs/shower-Qo99TlytAvuww",
            "https://tenor.com/es/view/ratto-gif-27372910",
            "https://tenor.com/es/view/rat-shower-pet-gif-14307357",
            "https://tenor.com/es/view/cute-rat-gif-22881449",

            ]
        respuesta_aleatoria = random.choice(respuestas)
        await ctx.send(respuesta_aleatoria)