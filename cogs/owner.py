import discord
from discord.ext import commands
import time

class Owner(commands.Cog):
    def __init__(self, Client):
        self.client = Client

    @commands.command()
    @commands.is_owner()
    async def leave(self, ctx, server: discord.Guild = None):
        embed = discord.Embed(title="", description=f"> **Leaving {server}**", color=0xffffff)
        msg = await ctx.reply(embed=embed)
        embedleft = discord.Embed(title="", description=f"> **Left {server}**", color=0xffffff)
        time.sleep(1)
        await server.leave()
        await msg.edit(embed=embedleft)



async def setup(client):
    await client.add_cog(Owner(client))