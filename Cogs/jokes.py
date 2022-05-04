import nextcord as discord
from nextcord.ext import commands
import json
import requests
from apikeys import jokekey


url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

querystring = {"format":"json","contains":"C%23","idRange":"0-150","blacklistFlags":"nsfw,racist"}

headers = {
	"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com",
	"X-RapidAPI-Key": jokekey
}





class Jokes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def joke(self, ctx):
        response = requests.request("GET", url, headers=headers, params=querystring)
        await ctx.send(json.loads(response.text)['setup'])
        await ctx.send(json.loads(response.text)['delivery'])




def setup(client):
    client.add_cog(Jokes(client))
