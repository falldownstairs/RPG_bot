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
    await ctx.send("all games cleared")

@bot.command()
async def info(ctx):
    if verify_game(ctx):
        encounter = game.get_current_encounter()
        area = game.get_current_area()
        await ctx.send("You are currently in: " + area.name + ".\n " + encounter.encounter_dialogue)

@bot.command(name="continue", description= "continues game")
async def continue_play(ctx):
    if verify_game(ctx):
        curr_game = None
        for game in games:
            if game.getTid() == ctx.channel.id:
                curr_game = game

            if curr_game == None:
                return
            if curr_game.is_ok_to_continue:
                await ctx.send("Your Adventure Continues...")
                curr_game.current_area.get_next_encounter()
            else:
                await ctx.send("You have to deal with the situation on hand first...")

@bot.command(name="interact", description= "interacts with game")
async def interact(ctx):
    if verify_game(ctx):
        pass

@bot.command()
async def aboutbot(ctx):
    pass
@bot.command()
async def storysynposis(ctx):
    pass

def verify_game(ctx):
    for game in games:
        if game.getTid() == ctx.channel.id and game.getPid() == ctx.author.id:
            return True
    return False



bot.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")