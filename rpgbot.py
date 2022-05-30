import discord
from discord.ext import commands

cmd_intents = discord.Intents.default()
cmd_intents.message_content = True
bot = commands.Bot(command_prefix="!", intents = cmd_intents) # You can change the command prefix to whatever you want.

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# for debug purposes
@bot.command() 
async def ping(ctx):
    #print("working")
    await ctx.send("Pong!")

# stops bot
@bot.command() 
async def shutdown(ctx): 
    await ctx.send("Stopping bot") 
    exit()

@bot.command(name = "start", description = "starts a game")
async def startgame(ctx):
    await ctx.channel.create_thread(name= ctx.author.name + "'s" + "game", auto_archive_duration=60, type=discord.ChannelType.public_thread, reason = None)
    

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