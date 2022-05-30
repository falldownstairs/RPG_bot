import discord
from discord.ext import commands # Import the commands extension
# discord.ext.commands are not the same as discord.commands!

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
async def stop(ctx): 
    await ctx.send("Stopping bot") 
    exit()



bot.run("OTc1MTg1OTkwMTY5ODA0ODIw.GtRKgx.GAOuK6l6gXK6QP9sIth33Qf2Z-vXo4EHBfrZcU")