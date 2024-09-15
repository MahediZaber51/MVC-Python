from disnake import OptionType, OptionChoice
from disnake.ext import commands

class PingSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="ping",
        description="Check the bot's latency",
    )
    async def ping(self, ctx):
        """Command to check the bot's latency"""
        await ctx.send(f"Pong! Latency: {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(PingSlash(bot))