import discord
import pickle
from game import Game
from discord.ext import commands
import os

cmd_intents = discord.Intents.default()
cmd_intents.message_content = True
bot = commands.Bot(command_prefix="!", intents = cmd_intents) # You can change the command prefix to whatever you want.

games = []

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
    #create games save file if one doesn't exist
    saves = open( "save.p", "wb+" )

    #load from save file
    games = pickle.load(saves)

# for debug purposes
@bot.command() 
async def ping(ctx):
    #print("working")
    await ctx.send("Pong!")

# stops bot
@bot.command() 
async def shutdown(ctx): 
    await ctx.send("Stopping bot") 
    pickle.dump(games, open( "save.p", "rb+" ))
    exit()

@bot.command(name = "start", description = "starts a game")
async def startgame(ctx):
    new_game = await ctx.channel.create_thread(name= ctx.author.name + "'s" + "game", auto_archive_duration=60, type=discord.ChannelType.public_thread, reason = None)
    games.append(Game(new_game.id, ctx.author.id))
    
# clears all game threads
@bot.command(name="clear", description= "clears all ongiong game threads")
async def clearGames(ctx):
    for game in games:
        thread = bot.get_channel(game.getTid())
        await thread.delete()
    games.clear()
    ctx.send("all games cleared")

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