from discord.ext import commands
import speedtest

def setup_performance_commands(bot: commands.Bot):
    """Registra comandos de rendimiento en el bot."""
    
    @bot.command(name="velocidad")
    async def velocidad(ctx: commands.Context):
        """Comando para realizar un test de velocidad de internet."""
        try:
            # Realizar test de velocidad
            st = speedtest.Speedtest()
            await ctx.send("pera que lo realice wachin...")

            st.get_servers()  # Obtiene una lista de servidores
            st.get_best_server()  # Selecciona el mejor servidor
            download_speed = st.download() / (1024 ** 2)  # Convierte bytes a Mbps
            upload_speed = st.upload() / (1024 ** 2)  # Convierte bytes a Mbps
            ping = st.results.ping  # Obtiene el ping

            # Enviar resultados al canal
            mensaje = (
                f"**Resultados del Test de Velocidad:**\n"
                f"🔄 Ping: {ping:.2f} ms\n"
                f"📥 Descarga: {download_speed:.2f} Mbps\n"
                f"📤 Subida: {upload_speed:.2f} Mbps"
            )
            await ctx.send(mensaje)
        except speedtest.ConfigRetrievalError:
            await ctx.send("Hubo un problema al obtener la configuración del test de velocidad. Inténtalo más tarde.")
        except speedtest.SpeedtestException as e:
            await ctx.send(f"Error al realizar el test de velocidad: {str(e)}")
        except Exception as e:
            await ctx.send(f"Hubo un error inesperado: {str(e)}")
