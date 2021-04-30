# discordcolorPY
Small color library for discord.py

# Use
```python

""" COLORS:
teal
dark_teal
green
dark_green
blue
dark_blue
purple
dark_purple
magenta
dark_magenta
old
dark_gold
orange
dark_orange
red
dark_red
lighter_grey
dark_grey
light_grey
darker_grey
blurple
treyple
"""

import dcolors
import discord

@bot.command()
async def test(ctx):
  embed = discord.Embed(color=blurple)
  embed.add_field(name="hey", value="colorful embeds")
  await ctx.send(embed=embed)

bot.run("token")
