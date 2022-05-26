import logging

import discord
from discord.ext import commands


class BookShelf(commands.Bot):
    __version__ = '1.0.0ag'

    initial_extensions = (
        'cogs.share',
        'cogs.dbooks'
    )
    test_guild = discord.Object(id=878431847162466354)

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__('bk ', intents=intents)

        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

        logger = logging.getLogger('asyncio')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='logs/asyncio.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

    async def setup_hook(self) -> None:
        for extension in self.initial_extensions:
            await self.load_extension(extension)

    async def on_ready(self):
        await self.tree.sync()
        print(f'Logged in as {self.user} | {self.user.id}')
