import discord
from discord.ext import commands
import asyncio


class Moderation(commands.Cog):

  def __init__(self, Client):
    self.client = Client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None):  # type: ignore
    if member == None:
      embed_message = discord.Embed(
        color=(0xffffff),
        title="kick",
        description=(f"kicks the provided member"),
      ).set_author(
        icon_url=
        "https://cdn.discordapp.com/avatars/1092056353431887935/a6e3943b277ae77dc64136dceba314dd.webp?size=512&width=0&height=0",
        name="ghoul").add_field(name="usage", value="kick [user]")
      await ctx.reply(embed=embed_message, mention_author=False)
    else:
      await ctx.guild.kick(member)

      embed_message = discord.Embed(
        color=(0xffffff),
        description=(f"> kicked {member.mention}"),
      )
      await ctx.reply(embed=embed_message, mention_author=False)

  @commands.command(aliases=["purge"])
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, count: int):
    embed_message = discord.Embed(
      color=(0xffffff),
      description=(f"> deleted `{count}` messages"),
    )
    await ctx.channel.purge(limit=count + 1)
    msg = await ctx.reply(embed=embed_message, mention_author=False)
    await asyncio.sleep(3)
    await msg.delete()

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def clearchannels(self, ctx):
    for c in ctx.guild.channels:  # iterating through each guild channel
      await c.delete()

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def fillrole(self, ctx, role: discord.Role = None):
    for m in ctx.guild.members:
      await m.add_roles(role)


async def setup(client):
  await client.add_cog(Moderation(client))
