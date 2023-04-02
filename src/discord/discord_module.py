import logging
from logging import handlers
import os
import sys
import zipfile

import discord
import mcstatus
from discord.ext import commands

from src.config.config_module import GENERAL_CHANNEL_ID, TOKEN
from src.server.ngrok_module import Ngrok
from src.tasks.task_module import BotTask


class DiscordBot(discord.Client):
    def __init__(self):
        super().__init__()

        # Configura i logger
        self.logger = logging.getLogger("minecraft-discord-bot")
        self.logger.setLevel(logging.INFO)

        # Formatter per i log
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s]: %(message)s')

        # Log su console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(log_formatter)
        self.logger.addHandler(console_handler)

        # Log su file
        log_folder = 'log'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        file_handler = logging.handlers.RotatingFileHandler(os.path.join(log_folder, "bot.log"), maxBytes=10485760,
                                                            backupCount=5, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(log_formatter)
        self.logger.addHandler(file_handler)

        # Register atexit function to compress log file
        import atexit

        def compress_log():
            log_file_name = os.path.join(log_folder, 'bot.log')
            if os.path.exists(log_file_name):
                with zipfile.ZipFile(os.path.join(log_folder, 'bot_log.zip'), 'w') as zip_file:
                    zip_file.write(log_file_name, os.path.basename(log_file_name), compress_type=zipfile.ZIP_DEFLATED)
                os.remove(log_file_name)

        atexit.register(compress_log)
        self.ngrok = Ngrok(self.logger)
        self.tasks = BotTask(self, self.logger)

    async def on_ready(self):
        self.logger.info(f"Logged in as {self.user.name} (ID: {self.user.id})")
        channel = self.get_channel(GENERAL_CHANNEL_ID)

        # Start the Ngrok tunnel on port 25565
        self.ngrok.start_tunnel(25565)

        # Get the server information using mcstatus
        try:
            server = mcstatus.JavaServer.lookup("localhost:25565")
            status = server.status()
        except ConnectionRefusedError:
            self.logger.error("Failed to connect to Minecraft server.")
            status = None

        # Send the server IP message to the general channel
        server_embed = await self.send_server_ip(channel, status)

        # Schedule the status update task
        self.loop.create_task(self.tasks.status_update_task(channel, server_embed.id))

    async def send_server_ip(self, channel, status):
        embed = discord.Embed(title="Minecraft Server Status", color=discord.Color.green())
        if status is not None:
            embed.add_field(name="Server Status", value="Online", inline=False)
            embed.add_field(name="Players", value=f"{status.players.online}/{status.players.max}", inline=False)
            embed.add_field(name="Version", value=status.version.name, inline=False)
            embed.add_field(name="Address", value=f"`{self.ngrok.url_tunnel}`", inline=False)
        else:
            embed.add_field(name="Server Status", value="Offline", inline=False)

        message = await channel.send(embed=embed)
        self.logger.info("Sent server IP message to Discord channel.")
        return message

    # Discord slash command: ping
    @commands.slash_command(name="ping", description="Test command to check bot response time")
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

    def start_bot(self):
        self.run(TOKEN)
