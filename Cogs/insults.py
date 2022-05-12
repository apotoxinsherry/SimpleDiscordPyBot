import nextcord as discord
from nextcord.ext import commands
import requests
import json

url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"



class insults(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def insult(self, ctx, user):
        result = requests.get(url)
        jsonread = json.loads(result.text)
        await ctx.send(f"{user} {jsonread['insult']}")
    
    @insult.error
    async def insult_error(self, ctx, error):
        result = requests.get(url)
        jsonread = json.loads(result.text)
        await ctx.send(f"{ctx.author.mention} {jsonread['insult']}")   

def setup(client):
    client.add_cog(insults(client))