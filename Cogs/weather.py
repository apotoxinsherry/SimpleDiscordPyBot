import nextcord as discord
from nextcord.ext import commands
import asyncio
import json
import requests
from apikeys import randomstuffapikey
from apikeys import rapidapikey

url = "https://random-stuff-api.p.rapidapi.com/weather"



headers = {
    'authorization': randomstuffapikey,
    'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
    'x-rapidapi-key': rapidapikey
    }



class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Command()
    async def weather(ctx, city):
        params = {city: 'The city you want weather details for'}
        response = await requests.request("GET", url, headers=headers, params=params)
        output = json.loads(response)
        await ctx.send(f"The Weather is: {output['location']}")

        
def setup(client):
    client.add_cog(weather(client))

