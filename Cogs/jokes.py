import nextcord as discord
from nextcord.ext import commands
import json
import requests
from apikeys import rapidapikey
from apikeys import randomstuffapikey


url = "https://random-stuff-api.p.rapidapi.com/joke"

querystring = {}

headers = {
    'authorization': randomstuffapikey,
    'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
    'x-rapidapi-key': rapidapikey
    }

response = requests.request("GET", url, headers=headers, params=querystring)






class Jokes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def joke(self, ctx):
        response = requests.request("GET", url, headers=headers, params=querystring)
        await ctx.send(json.loads(response.text)['joke'])




def setup(client):
    client.add_cog(Jokes(client))
