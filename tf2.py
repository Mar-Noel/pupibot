from discord.ext import commands
import subprocess
import discord

def setup_tf2_commands(bot):
    @bot.command()
    async def jugartf2(ctx):
        ruta_acceso_directo = r"C:\Users\Workstation\Desktop\tf2server.url"  # Cambiar acceso directo por url

        try:
            subprocess.run(ruta_acceso_directo, shell=True)  # Cambié la variable de Popen a run
            await ctx.send("Arrancando servidor TF2...")
            actividad = discord.Game(name="Team Fortress 2", type=2)
            await bot.change_presence(status=discord.Status.do_not_disturb, activity=actividad)
        except Exception as e:
            await ctx.send(f"No se pudo, XD. Error: {str(e)}")

    # Comando para actualizar TF2
    @bot.command()
    async def updatetf2(ctx):
        ruta_acceso_directo = r"C:\Users\Workstation\Desktop\actualizar - Acceso directo.lnk"
        try:
            subprocess.Popen(ruta_acceso_directo, shell=True)
            await ctx.send("A CASA MALOOOOOO")  # :(
        except Exception as e:
            await ctx.send(f"No se pudo abrir el juego. Error: {str(e)}")

    # Comando para parar TF2
    @bot.command()
    async def parartf2(ctx):
        try:
            subprocess.run(["taskkill", "/F", "/IM", "srcds_win64.exe"], check=True)
            await ctx.send("Apagao")
            await bot.change_presence(status=discord.Status.online, activity=None)
        except subprocess.CalledProcessError:
            await ctx.send("No se detuvo ni bosta, ¿seguro que esta abierto rey?")

