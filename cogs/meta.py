from discord.ext import commands
from discord.ext.commands import guild_only, has_guild_permissions
from typing import Optional

# will work on this soon

class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='ping')
    async def _ping(self, ctx):
        await ctx.send("Pong!")


    @commands.group()
    async def prefix(self, ctx):
        pass


    @prefix.command(name='set')
    @has_guild_permissions(manage_guild=True)
    async def set_prefix(self, ctx, *, prefix: Optional[str]) -> None:
        '''Change the bot prefix'''
        if len(prefix) > 6:
            await ctx.send("prefix too long")
        else:
            query = "UPDATE prefixes SET prefix = $1 WHERE guild_id = $2"
            await self.bot.pool.execute(query, prefix, str(ctx.guild.id))
            await ctx.send(f"prefix updated to {prefix}")

    
    @prefix.command(name='reset')
    @has_guild_permissions(manage_guild=True)
    async def reset_prefix(self, ctx):
        '''Reset the prefix to the main one'''
        try:
            query = "UPDATE prefixes SET prefix = $1 WHERE guild_id = $2"
            await self.bot.pool.execute(query, self.bot.clean_prefix, str(ctx.guild.id))
            await ctx.send("Reset to main prefix `!`")
        except Exception as e:
            await ctx.send(e)



def setup(bot):
    bot.add_cog(Meta(bot))