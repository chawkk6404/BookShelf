from __future__ import annotations

from typing import TYPE_CHECKING, Type

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from bot import BookShelf


class ErrorHandler(commands.Cog):
    secret_perms: tuple[Type[commands.CheckFailure], ...] = (
        commands.MissingPermissions,
        commands.NotOwner
    )

    def __init__(self, bot: BookShelf):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send_help(ctx.command)
        elif isinstance(error, self.secret_perms):
            return
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'`{ctx.command.qualified_name} cannot be used in DMs.`')
        else:
            raise error


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
