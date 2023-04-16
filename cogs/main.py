import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, Client):
        self.client = Client

    @commands.command(aliases=["about", "abt"])
    async def help(self, ctx):
        embed = discord.Embed(title="", description=f"""> **About Cover 👻**
        
        **Info:**
        *-* **Written In** [`liftcord.py`](https://github.com/devliftz/liftcord.py)
        *-* **Created:** `{self.client.user.created_at}`
        
        **About:**
        *-* **Owner** `.drmr#4677`
        *-* **Source Code** [`liftcord.py-cover`](https://github.com/devliftz/liftcord.py-cover)
        
        > **Use** `!cmds` **to get full command list**""", color=0xffffff)
        msg = await ctx.reply(embed=embed)

    @commands.command(aliases=['cmd', 'cmdz', 'commands'])
    async def cmds(seld, ctx):
        embed = discord.Embed(title="", description=f"""> **INDEV**""", color=0xffffff)
        await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(Main(client))