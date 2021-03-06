import nextcord as discord
from nextcord.ext import commands

from AnilistPython import Anilist

from apikeys import anilistid
from apikeys import anilistsecret

from bs4 import BeautifulSoup

my_client = Anilist(cid=anilistid, csecret=anilistsecret)

class anidata(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def anime(self, ctx, name):
        animedata = my_client.get_anime(name)
        animeid = my_client.get_anime_id(name)
        mydesc = BeautifulSoup(animedata['desc'], "lxml").text
        my_embed = discord.Embed(title=animedata['name_english'], url=f"https://anilist.co/anime/{animeid}", description=mydesc, color=0x323834)
        my_embed.set_thumbnail(url=animedata['cover_image'])
        try:
            my_embed.add_field(name='Episodes', value=animedata['airing_episodes'], inline=True)
        except KeyError:
            my_embed.add_field(name='Episodes', value=animedata['next_airing_ep'], inline=True)
        
        my_embed.add_field(name="Rating", value=animedata['average_score'], inline=True)
        my_embed.add_field(name='Genres', value=animedata['genres'], inline=False)
        await ctx.send(embed=my_embed)

    @commands.command()
    async def manga(self, ctx, name):
        mangadata = my_client.get_manga(name)
        mangaid = my_client.get_manga_id(name)
        description = BeautifulSoup(mangadata['desc'], "lxml").text
        my_embed = discord.Embed(title=mangadata['name_english'], url=f"https://anilist.co/anime/{mangaid}", description=description, color=0x323834)
        my_embed.set_thumbnail(url=mangadata['cover_image'])
        my_embed.add_field(name='Chapters', value=mangadata['chapters'], inline=True)
        my_embed.add_field(name="Rating", value=mangadata['average_score'], inline=True)
        my_embed.add_field(name='Genres', value=mangadata['genres'], inline=False)
        await ctx.send(embed=my_embed)

    
    @anime.error
    async def anime_error(self,ctx,error):
        await ctx.send("Please provide an anime.")
    
    @manga.error
    async def manga_error(self, ctx, error):
        await ctx.send("Please provide a manga")



def setup(client):
    client.add_cog(anidata(client))
        