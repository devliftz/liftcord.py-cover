import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, Client):
        self.client = Client

    @commands.command(aliases=["test", "p"])
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        embed_message = discord.Embed(
            color=(0x758A85),
            description=(f"> **{bot_latency}ms**"),
        )
        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(Ping(client))