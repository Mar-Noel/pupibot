from discord.ext import commands
import psutil
import subprocess
import speedtest
import cpuinfo
import wmi
import os
def get_ram_frequency():
    # Ejecuta el comando WMIC para obtener la velocidad de la RAM
    output = os.popen("wmic memorychip get speed").read()
    
    # Filtra y limpia los datos
    lines = output.strip().split("\n")
    if len(lines) > 1:
        frequencies = [line.strip() for line in lines[1:] if line.strip()]
        return frequencies
    else:
        return []
    
def get_first_ram_frequency():
    frequencies = get_ram_frequency()  # Obtiene las frecuencias de los módulos de RAM
    if frequencies:
        return frequencies[0]  # Retorna la frecuencia del primer módulo
    else:
        return "Desconocida"


def setup_performance_commands(bot):
    def get_cpu_temp(sensor_name='coretemp'):
        """Obtiene la temperatura del CPU utilizando psutil."""
        try:
            temps = psutil.sensors_temperatures()
            if sensor_name in temps:
                for entry in temps[sensor_name]:
                    if entry.label == 'Package id 0':  # Ajusta según tu sistema
                        return entry.current
            return "Sensor no encontrado"
        except AttributeError:
            return "Temperatura no soportada en este sistema."

    def get_motherboard_temp():
        """Obtiene la temperatura de la motherboard usando WMI en Windows."""
        try:
            c = wmi.WMI(namespace="root\wmi")
            for sensor in c.MSAcpi_ThermalZoneTemperature():
                # Convertir a grados Celsius
                return round((sensor.CurrentTemperature / 10.0) - 273.15, 2)
            return "No se detectaron sensores."
        except Exception:
            return "No se pudo obtener la temperatura de la motherboard."

    @bot.command()
    async def rendimiento(ctx):
        """Comando para obtener estadísticas de rendimiento del sistema."""
        try:
            # Información del CPU
            cpu_brand = cpuinfo.get_cpu_info()['brand_raw']
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_temp = get_cpu_temp()

            # Información de la RAM
            ram_info = psutil.virtual_memory()
            ram_total = ram_info.total / (1024 ** 3)  # Convertir a GB
            ram_used = ram_info.used / (1024 ** 3)  # Convertir a GB
            ram_percent = ram_info.percent
            ram_frequency = get_first_ram_frequency()
            ram_percent = ram_info.percent

            # Uso del disco 1
            disk_usage_c = psutil.disk_usage('C:/')
            disk_total = disk_usage_c.total / (1024 ** 3)  # Convertir a GB
            disk_used = disk_usage_c.used / (1024 ** 3)  # Convertir a GB
            disk_percent = disk_usage_c.percent
        
            # Uso del disco 2 (manejo de errores si no existe)
            try:
                disk_usage_d = psutil.disk_usage('D:/')
                disk_total2 = round(float(disk_usage_d.total / (1024 ** 3)),2)  # Convertir a GB
                disk_used2 = round(float(disk_usage_d.used / (1024 ** 3)),2)  # Convertir a GB
                disk_percent2 = disk_usage_d.percent
            except FileNotFoundError:
                disk_total2 = disk_used2 = disk_percent2 = "No disponible"        # Información del disco


            # Temperaturas
            motherboard_temp = get_motherboard_temp()

            # Velocidad de internet
            try:
                st = speedtest.Speedtest()
                st.get_best_server()
                download_speed = st.download() / (1024 ** 2)  # Convertir a Mbps
                upload_speed = st.upload() / (1024 ** 2)  # Convertir a Mbps
                ping = st.results.ping
            except:
                download_speed = "No disponible"
                upload_speed = "No disponible"
                ping = "No disponible"

            # Formatear mensaje
            mensaje = (
            f"**Rendimiento del servidor:**\n"
            f"**CPU:** *{cpu_brand}*, ({cpu_usage}%)\n"
            f"**RAM:** {ram_used:.2f}GB / {ram_total:.2f}GB *@{ram_frequency} MHz* , ({ram_percent}%)\n"
            f"**Disco C:** {disk_used:.2f}GB / {disk_total:.2f}GB ({disk_percent}%)\n"
            f"**Disco D:** {disk_used2}GB / {disk_total2}GB ({disk_percent2}%)\n"
            f"**Internet:** Ping: {ping}ms, Descarga: {download_speed if isinstance(download_speed, str) else f'{download_speed:.2f} Mbps'}, "
            f"Subida: {upload_speed if isinstance(upload_speed, str) else f'{upload_speed:.2f} Mbps'}\n"
            f"**Temperaturas:** CPU: {cpu_temp}°C, Motherboard: {motherboard_temp}°C\n"
            )
            await ctx.send(mensaje)

        except Exception as e:
            await ctx.send(f"Hubo un error al obtener el rendimiento: {str(e)}")
            
    @bot.command()
    async def sync(ctx):
        ruta_acceso_directo2 = r"C:\Program Files\Google\Drive File Stream\launch.bat"
        try:
            subprocess.Popen(ruta_acceso_directo2, shell=True)
            await ctx.send(":arrows_counterclockwise:")
        except Exception as e:
            await ctx.send(f"No se pudo abrir los programas, XD. Error: {str(e)}")

    @bot.command()
    async def nosync(ctx):
        try:
            subprocess.run(["taskkill", "/F", "/IM", "GoogleDriveFS.exe"], check=True)
            await ctx.send(":arrows_counterclockwise:n't")
        except subprocess.CalledProcessError:
            await ctx.send("No se detuvo ni bosta, ¿seguro que esta abierto rey?")