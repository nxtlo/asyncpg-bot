import discord
import asyncpg
from discord.ext import commands
from discord import Intents
from typing import Optional
from data import conf
import sys
import traceback


class MainBot(commands.Bot):
    def __init__(self):
        self.db = conf.Database()
        super().__init__(
            command_prefix=self.get_prefix, # We get the prefix from the `get_prefix` function
            intents=Intents.all(), # You don't really need all intents enabled.
            description="a cool bot made with discord.py and asyncpg",
            owner_id=int, # Change `int` to your discord ID
            case_insensitive=True # Allwoing commands to be case insensitive for an example "ping" and "PING" are the same
        )

    @property
    def owner(self):
        return self.get_user(self.owner_id)


    @property
    def clean_prefix(self):
        return "!"

    async def on_ready(self):
        with open('./data/schema.sql', 'r', encoding='utf8') as script:
            schema = script.read()
            await self.pool.execute(schema) # read the schema and make the tables if they don't exists
            print("Tables created...") # idk if i should have this in on_ready or else, if there's a better way tell me :)
        print("Connected to discord...")


    # Here we make the database pool so we can access it from any cog/file
    # example: await self.bot.pool.execute(...)
    
    async def pool_init(self) -> Optional[asyncpg.pool.Pool]:
        self.pool = await asyncpg.create_pool(
            database=self.db.db,
            user=self.db.user,
            password=self.db.password,
            host=self.db.host,
            port=self.db.port,
            max_inactive_connection_lifetime=0 # allow statements to be cached indefinitely.
        )

    # a custom per guild prefix
    async def get_prefix(self, msg):
        if not msg.guild:
            return self.clean_prefix # if the message not in a guild and in the DMs then we return this prefix
        else:
            query = '''SELECT prefix FROM prefixes WHERE guild_id = $1''' # Select the prefix from prefixes table.
            prefix = await self.pool.fetchval(query, str(msg.guild.id)) # fetch the table and return the first matching prefix and the guild.id
            
            if not prefix:
                return commands.when_mentioned_or('!')(self, msg) # if there's no custom prefix in the database return the main prefix
            return commands.when_mentioned_or(prefix)(self, msg) # return the prefix or when we mentioning the bot.


    def load_cogs(self):
        # load the cogs
        for cog in conf.COGS:
            try:
                self.load_extension(f"{cog}")
                print(f"Loaded {cog}")
            except Exception:
                print(f'\nFailed to load extension {cog}.', file=sys.stderr)
                traceback.print_exc()

    def run(self):
        try:
            self.load_cogs()
            super().run(conf.token, reconnect=True)
        except:
            raise

if __name__ == "__main__":
    bot = MainBot()
    bot.loop.run_until_complete(bot.pool_init()) # run the Pool
    bot.run() # run the bot