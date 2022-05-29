from calendar import c
from unicodedata import name
from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(debug_guilds = [975186272823939112], command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("hello!")

@commands.command(name = "start", description = "starts a game")
async def startgame(ctx):
    await ctx.create_thread(name="game", auto_archive_duration=60, type=None, reason = None)
    

@bot.command()
async def info(ctx):
    pass

@bot.command()
async def savegame(ctx):
    pass

@bot.command()
async def loadgame(ctx):
    pass
@bot.command()
async def option1(ctx):
    pass
@bot.command()
async def option2(ctx):
    pass
@bot.command()
async def option3(ctx):
    pass
@bot.command()
async def option4(ctx):
    pass
@bot.command()
async def aboutbot(ctx):
    pass
@bot.command()
async def storysynposis(ctx):
    pass






bot.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")