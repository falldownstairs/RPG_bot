import discord
import pickle
from game import Game
from discord.ext import commands
from discord.ui import Button
import os
from encounter import *

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
    games.append(Game(new_game.id, ctx.author.id, "a game"))
    
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
async def interact(ctx, choice):
    if verify_game(ctx):
        try:
            int(choice)
        except:
            await ctx.send("enter a number corresponding to the choice you want. If encounter has no choices, just type 0")
            return

        curr_game = None
        for game in games:
            if game.getTid() == ctx.channel.id:
                curr_game = game

            if curr_game == None:
                return

        if game.get_current_encounter() == None:
            await ctx.send("do the continue command first")

        if game.is_ok_to_continue == True:
            await ctx.send("You've already finished interacting with this encounter'")

        if type(game.get_current_encounter()) is Choice_Encounter: 
            game.get_current_encounter().interact(int(choice))
        else:
            game.get_current_encounter().interact()



        

@bot.command()
async def aboutbot(ctx):
    await ctx.send("Add info about bot")
@bot.command()
async def storysynposis(ctx):
    if verify_game():
        for game in games:
            if game.getTid() == ctx.channel.id:
                curr_game = game

            if curr_game == None:
                return
        
        await ctx.send(game.getDesc())

def verify_game(ctx):
    for game in games:
        if game.getTid() == ctx.channel.id and game.getPid() == ctx.author.id:
            return True
    return False

class fightView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # timeout of the view must be set to None

    @discord.ui.button(label="Attack", row=0,custom_id="button-1",  style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You attack")

    @discord.ui.button(label="Use Item", row=1,custom_id="button-2", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("Not Implemented")




bot.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")