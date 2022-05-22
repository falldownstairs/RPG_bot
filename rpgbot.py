import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("hello!")

@bot.startgame()
async def test(ctx):
    pass

@bot.help()
async def test(ctx):
    pass

@bot.savegame()
async def test(ctx):
    pass

@bot.loadgame()
async def test(ctx):
    pass
@bot.option1()
async def test(ctx):
    pass
@bot.option2()
async def test(ctx):
    pass
@bot.option3()
async def test(ctx):
    pass
@bot.option4()
async def test(ctx):
    pass
@bot.aboutbot()
async def test(ctx):
    pass
@bot.storysynposis()
async def test(ctx):
    pass






client.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")