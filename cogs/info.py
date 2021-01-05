from discord.ext import commands
from discord import __version__


class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.send(f"Hey! i'm a bot made with discord.py {__version__} and Asyncpg!")



def setup(bot):
    bot.add_cog(info(bot))