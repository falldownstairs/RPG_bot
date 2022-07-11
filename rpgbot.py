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

class fightView(discord.ui.View):
    def __init__(self, player, enemy, playerHPdisplay, enemyHPdisplay, game):
        super().__init__(timeout=None) # timeout of the view must be set to None
        self.player = player
        self.enemy = enemy
        self.playerHPdisplay = playerHPdisplay
        self.enemyHPdisplay = enemyHPdisplay
        self.game = game

    @discord.ui.button(label="Attack", row=0,custom_id="button-1",  style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You attack")
        #insert code to attack here








        #after you atatck, enemy should also attack




        # after both attack, the displayed healths should be updated
        await self.playerHPdisplay.edit(content= "Your Health: " + str(self.game.player.health))
        await self.enemyHPdisplay.edit(content= self.enemy.name + "'s Health: " + str(self.enemy.health))

        # if either player or enemy reaches 0 HP;
        if self.player.health < 1:
            #end game    
            self.game.is_ok_to_continue = False
            await ctx.send("You have died.")
        elif self.enemy.health < 1:
               #continue with game
               self.game.is_ok_to_continue = True
               self.player.health = 100
               await ctx.send("you win! Now you can continue on with the continue command")

    @discord.ui.button(label="Use Item", row=1,custom_id="button-2", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("Not Implemented")

    @discord.ui.button(label="Enemy Info", row=2,custom_id="button-3", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message(self.enemy.name + "\n" + self.enemy.description)


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
    new_game_thread = await ctx.channel.create_thread(name= ctx.author.name + "'s" + "game", auto_archive_duration=60, type=discord.ChannelType.public_thread, reason = None)
    new_game = Game(new_game_thread.id, ctx.author.id, "a game")
    games.append(new_game)
    encounter = new_game.get_current_encounter()
    area = new_game.get_current_area()
    await new_game_thread.send("You are currently in: " + area.name + ".\n " + encounter.encounter_dialogue)
    
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
        curr_game = None
        for i in games:
            if i.getTid() == ctx.channel.id:
                curr_game = i
        encounter = curr_game.get_current_encounter()
        area = curr_game.get_current_area()
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
                curr_game.set_current_encounter(curr_game.current_area.get_next_encounter())
                encounter = curr_game.get_current_encounter()
                area = curr_game.get_current_area()
                curr_game.is_ok_to_continue = False
                await ctx.send("You are currently in: " + area.name + ".\n " + encounter.encounter_dialogue)
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
            if type(game.get_current_encounter()) is Combat_Encounter:
                enemy = game.get_current_encounter().interact()
                await ctx.send("You start to fight...")
                playerHPmsg = await ctx.send("Your Health: " + str(game.player.health) + "     " + "Attack: " + str(game.player.attack))
                enemyHPmsg = await ctx.send(enemy.name + "'s Health: " + str(enemy.health) + "     " + "Attack: " + str(enemy.attack))
                await ctx.send("You fight " + enemy.name, view = fightView(game.player , enemy, playerHPmsg, enemyHPmsg, game))
            else:
                enemy = game.get_current_encounter().interact()
            



        

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





bot.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")