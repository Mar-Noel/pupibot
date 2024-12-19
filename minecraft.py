from discord.ext import commands
import pygetwindow as gw
from discord.ext import commands
from funciones_minecraft import setup_minecraft_commands

import discord
import subprocess


def servidor_activo(nombre_ventana):
    ventanas = gw.getAllTitles()
    for ventana in ventanas:
        if nombre_ventana.lower() in ventana.lower():
            return True
    return False

def setup_minecraft_commands(bot):
    
    @bot.command()
    async def parar(ctx):
        ruta_acceso_directo = r"C:\Users\Notebook\Desktop\ServerModeado\pararserver.bat"
        ruta_acceso_directo2 = r"C:\Users\Notebook\Desktop\ServerVanilla\pararserver.bat" #tengo que crear el bat para apagar el server modeado

        nombre_ventana_servidor = "Servidor_vanilla"
        nombre_ventana_servidor2 = "Servidor_modeado"

        # Verificar si ambos servidores están apagados
        if not servidor_activo(nombre_ventana_servidor) and not servidor_activo(nombre_ventana_servidor2):
            await ctx.send("Pero... Ningún servidor está prendido")
            return

        try:
            # Apagar servidores según su estado
            if servidor_activo(nombre_ventana_servidor)==True:
                subprocess.Popen(ruta_acceso_directo, shell=True)
                await ctx.send("Apagando servidor vanilla...")
            if servidor_activo(nombre_ventana_servidor2==True):
                subprocess.Popen(ruta_acceso_directo2, shell=True)
                await ctx.send("Apagando servidor modeado...")

            # Cambiar el estado del bot
            await bot.change_presence(status=discord.Status.online, activity=None)

        except subprocess.CalledProcessError:
            await ctx.send("Error al intentar apagar el servidor.")


    @bot.command()
    async def jugarmodeado(ctx):
        ruta_acceso_directo = r"C:\Users\Notebook\Desktop\ServerModeado\Iniciar server, ADMINISTRADOR.bat"
        nombre_ventana_servidor = "Servidor_modeado"
        
       
        if servidor_activo(nombre_ventana_servidor)==True:
            await ctx.send("Sos o te haces? El server ya esta prendido")
            return            
        
        serverID = 1123780717999034509
        canalID = 1211150474603008061
        server = bot.get_guild(serverID)
        channel = server.get_channel(canalID)

        if channel is not None:
            rolID = 1211138250849259571
            mensaje = f"<@&{rolID}>Server modeado abiertooo."
            await channel.send(mensaje)
        else:
            await ctx.send("No encontre el canal pipipi.")

        
        try:
            subprocess.Popen(ruta_acceso_directo, shell=True)
            await ctx.send("Un server modeado ha aparecido")
            actividad = discord.Game(name="Minecraft Modeado", type=2)
            await bot.change_presence(status=discord.Status.do_not_disturb, activity=actividad)
        except Exception as e:
            await ctx.send(f"No se pudo abrir el juego, XD. Error: {str(e)}")

    
    @bot.command()
    async def jugarvanilla(ctx):
        ruta_acceso_directo = r"C:\Users\Notebook\Desktop\ServerVanilla\Iniciar server, ADMINISTRADOR.bat"
        nombre_ventana_servidor = "Servidor_vanilla"

        if servidor_activo(nombre_ventana_servidor)==True:
            await ctx.send("Sos o te haces? El server ya esta prendido")
            return
        
        try:
            serverID = 1123780717999034509
            canalID = 1211150474603008061
            server = bot.get_guild(serverID)
            channel = server.get_channel(canalID)

            if channel is not None:
                rolID = 1211138250849259571
                mensaje = f"<@&{rolID}>Server vanilla abiertooo!!"
                await channel.send(mensaje)
            else:
                await ctx.send("No encontre el canal pipipi.")

            subprocess.Popen(ruta_acceso_directo, shell=True)
            await ctx.send("Un server salvaje ha aparecido")
            actividad = discord.Game(name="Minecraft 1.21.2", type=2)
            await bot.change_presence(status=discord.Status.do_not_disturb, activity=actividad)
        except Exception as e:
            await ctx.send(f"No se pudo abrir el juego. Error: {str(e)}")


    @bot.command()
    async def ip(ctx):
        await ctx.send("Ip del server vanilla => **26.106.92.84:25565**")
        await ctx.send("Ip del server modeado => **26.106.92.84:25560**")


    @bot.command()
    async def mods(ctx):
        await ctx.send("Aca tenes la carpeta mostro https://acortar.link/k3S2JJ (todos estan en forge)")


    @bot.command()
    async def version(ctx):
        await ctx.send("La version del servidor sin mods es la **1.21.2**")
        await ctx.send("La version con forge (server con mods) es la **1.19.2**")
        await ctx.send("Para ver los mods, usar el comando *mods")
