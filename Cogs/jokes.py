import nextcord as discord
from nextcord.ext import commands
import json
import requests
from apikeys import jokekey


url = "https://joke3.p.rapidapi.com/v1/joke"

payload = {
	"content": "A joke here",
	"nsfw": "false"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Host": "joke3.p.rapidapi.com",
	"X-RapidAPI-Key": jokekey
}

response = requests.request("POST", url, json=payload, headers=headers)


class Jokes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def joke(self, ctx):
        await ctx.send(json.loads(response.text)['content'])




def setup(client):
    client.add_cog(Jokes(client))
