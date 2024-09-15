import disnake
from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)  # Calculate bot's latency in milliseconds
        await ctx.send(f'Pong! Latency: {latency}ms')

def setup(bot):
    bot.add_cog(Ping(bot))