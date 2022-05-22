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

@bot.command()
async def test(ctx,startgame):
    pass

@bot.command()
async def test(ctx,help):
    pass

@bot.command()
async def test(ctx,savegame):
    pass

@bot.command()
async def test(ctx,loadgame):
    pass
@bot.command()
async def test(ctx,option1):
    pass
@bot.command()
async def test(ctx,option2):
    pass
@bot.command()
async def test(ctx,option3):
    pass
@bot.command()
async def test(ctx,option4):
    pass
@bot.command()
async def test(ctx,aboutbot):
    pass
@bot.command()
async def test(ctx,storysynposis):
    pass






client.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")