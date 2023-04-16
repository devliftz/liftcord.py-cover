# Requirements
import discord
from discord.ext import commands
import os
import asyncio
import json
import time

# Import liftcord.py-tools 
import liftcord.py_mobile

# Import Config
from config import cfg

def get_server_prefix(client, message):
    with open("settings/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("")
    await bot.change_presence(activity=discord.Game(name=F"liftcord.py 🐍"))

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")


@bot.event
async def on_guild_join(guild):
    with open("settings/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = "!"

    with open("settings/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("settings/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open("settings/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.command(aliases=["prefix", "changeprefix"])
async def setprefix(ctx, *, newprefix: str):

    if len(newprefix) > 2:
        embed_message = discord.Embed(
            color=(0xffffff),
            description=(f"> <:caution:1096425475590598836>  {ctx.author.mention}: Prefix is too large"),
        )
        await ctx.reply(embed = embed_message, mention_author=False)
    
    else:
        with open("settings/prefixes.json", "r") as f:
            prefix = json.load(f)

        prefix[str(ctx.guild.id)] = newprefix

        with open("settings/prefixes.json", "w") as f:
            json.dump(prefix, f, indent=4)

        embed_message = discord.Embed(
                color=(0xffffff),
                description=(f"> <:check:1096543207837421648>  {ctx.author.mention}: Guild prefix changed to `{newprefix}`"),
            )
        await ctx.reply(embed = embed_message, mention_author=False)

@bot.command(aliases=['restart', 'reboot'])
async def upd(ctx):
    embed_loading = discord.Embed(title="", description=f"""> **Restarting all cogs**
    
    **Cogs**
    *-* `ping.py` <a:loadingcircle:1097220809359110245>
    *-* `moderation.py` <a:loadingcircle:1097220809359110245>""", color=0xffffff)
    embed_done = discord.Embed(title="", description=f"""> **Restarting complete**
    
    **Cogs**
    *-* `ping.py` <:check:1097220806624432168>
    *-* `moderation.py` <:check:1097220806624432168>""", color=0xffffff)
    loading = await ctx.reply(embed=embed_loading)
    time.sleep(2)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.reload_extension(f"cogs.{filename[:-3]}")
    await loading.edit(embed=embed_done)
    time.sleep(5)
    await loading.delete()
    await ctx.message.delete()



bot.run(f"{cfg.token}")