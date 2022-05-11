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
    

    @commands.command()
    async def weather(self, ctx, city):
        params = {"city":city}
        response = requests.request("GET", url, headers=headers, params=params)
        output = json.loads(response.text)
        await ctx.send(f"Location : {output[0]['location']['name']} \nTemperature: {output[0]['current']['temperature']}°C \nLow: {output[0]['forecast'][1]['low']}°C \nHigh: {output[0]['forecast'][1]['high']}°C ")

        
def setup(client):
    client.add_cog(weather(client))

