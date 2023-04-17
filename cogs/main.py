import discord
from discord.ext import commands


class Main(commands.Cog):

  def __init__(self, Client):
    self.client = Client

  @commands.command(aliases=["about", "abt"])
  async def help(self, ctx):
    embed = discord.Embed(title="",
                          description=f"""> **About Cover 👻**
        
        **Info:**
        *-* **Written In** [`liftcord.py`](https://github.com/devliftz/liftcord.py)
        *-* **Created:** `{self.client.user.created_at}`
        
        **About:**
        *-* **Owner** `.drmr#4677`
        *-* **Source Code** [`liftcord.py-cover`](https://github.com/devliftz/liftcord.py-cover)
        
        > **Use** `!cmds` **to get full command list**""",
                          color=0xffffff)
    msg = await ctx.reply(embed=embed)

  @commands.command(aliases=['cmd', 'cmdz', 'commands'])
  async def cmds(seld, ctx):
    embed = discord.Embed(title="",
                          description=f"""> **INDEV**""",
                          color=0xffffff)
    await ctx.reply(embed=embed)

  @commands.command(aliases=['hi', 'abtus'])
  async def aboutus(self, ctx):
    embed = discord.Embed(title="",
                          description=f"""> @User **Hi, so first**

> **What is DEVLIFT?**
*-* **The abbreviation "dev" is a widely recognized and commonly used term in the tech industry to refer to developers, programmers, or software engineers who create software and applications. It's a term that is highly associated with the world of programming and tech.**

*-* **The term "lift" is a word that implies upward movement and progress. It suggests that the studio is focused on helping its clients achieve their goals and elevate their businesses or projects to the next level. The term "lift" also has connotations of empowerment and improvement, which align with the idea of progress.**

*-* **The name DevLift is concise and easy to remember, which can be a valuable asset for a company name. It's a name that can be easily recognized and associated with programming and development.**

*-* **The name DevLift has a positive and aspirational connotation that suggests a programming studio that is focused on empowering its clients and helping them achieve their goals. It's a name that is meant to inspire progress and forward movement.**

*-* **The name DevLift is a great choice for a programming studio that is focused on helping businesses and projects succeed through expert programming solutions. It's a name that suggests a studio that is committed to empowering its clients and helping them achieve their goals through cutting-edge development and programming.**

*-* **Overall, the name DevLift is a concise and powerful name that conveys a sense of empowerment, progress, and expertise in the world of programming and development. It's a name that is easy to remember and associated with the world of tech and programming, making it an excellent choice for a programming studio.**

> **Our links & more**
*-* **GitHub: https://github.com/devliftz**
*-* **Latest Project: https://github.com/devliftz/liftcord.py-cover**
*-* **Best Project: https://github.com/devliftz/liftstyle.css**

> **More at** `!hi`""",
                          color=0xffffff)


async def setup(client):
  await client.add_cog(Main(client))
