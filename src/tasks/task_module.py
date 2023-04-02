import asyncio
from logging import Logger

import discord
import mcstatus

from config_module import MC_SERVER_IP, MC_SERVER_PORT


class BotTask:
    def __init__(self, bot, logger: Logger):
        self.logger = logger
        self.bot = bot

    # Function to update the server IP message with new server information
    async def status_update_task(self, channel, embed_id):
        while True:
            # Get the server information using mcstatus
            try:
                server = mcstatus.JavaServer.lookup(f"{MC_SERVER_IP}:{MC_SERVER_PORT}")
                status = server.status()
            except ConnectionRefusedError:
                self.logger.error("Failed to connect to Minecraft server.")
                status = None
            try:
                # Update the server IP message with new server information
                if status is not None:
                    server_embed = discord.Embed(title="Minecraft Server Status", color=discord.Color.green())
                    server_embed.add_field(name="Server Status", value="Online", inline=False)
                    server_embed.add_field(name="Players", value=f"{status.players.online}/{status.players.max}",
                                           inline=False)
                    server_embed.add_field(name="Version", value=status.version.name, inline=False)
                    server_embed.add_field(name="Address", value=f"`{self.bot.ngrok.url_tunnel}`", inline=False)

                else:
                    server_embed = discord.Embed(title="Minecraft Server Status", color=discord.Color.red())
                    server_embed.add_field(name="Server Status", value="Offline", inline=False)
            finally:
                pass
            message = await channel.fetch_message(embed_id)
            await message.edit(embed=server_embed)

            self.logger.info("Updated server IP message with new server information.")
            await asyncio.sleep(300)  # wait for 5 minutes
