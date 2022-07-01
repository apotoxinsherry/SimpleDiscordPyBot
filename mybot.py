import nextcord as discord
from nextcord.ext import commands
import asyncio
import os
from apikeys import discordkey


client = commands.Bot(command_prefix='!')

mycogs = []

for file in os.listdir("Cogs/"):
    if file.endswith(".py"):
        mycogs.append("Cogs." + file[:-3]) #Cogs should represent the directory where the cogs are stored


for extension in mycogs:
    client.load_extension(extension)


@client.event
async def on_ready():
    print("We're logged in!")


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

@client.command()
async def hello(ctx):
    await ctx.send("Hello " + str(ctx.author)[:-5])
    



client.run(discordkey)