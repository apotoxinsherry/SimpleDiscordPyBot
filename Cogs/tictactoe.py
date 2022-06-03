import nextcord as discord
from nextcord.ext import commands
from random import randint

#to-do:
#ensure that misc input by the user don't get in the way of the game
#implement a users-in-game function which prevernts already existing users from re-running the command again. 
#implement the actual game logic


#general game logic:
#player calls for the game by using the playttt function and the ingame flag is set to true -- this is checked by checking if the player is on the players list.
# it checks if the command has already been run 
#also maybe create a function to obtain and verify user input
# the event on_message executes here only if ingame so as to avoid unnecessary triggers
# on_message then gets the symbol for the user




class player():
    def __init__(self, name):
        self.name = name
        self.uchoice = 'X'
        self.cchoice = 'O'
        self.gameboard = [' ']*10
    

    def display(self):
        return f'''
{self.gameboard[7]} | {self.gameboard[8]} | {self.gameboard[9]}
--|---|----
{self.gameboard[4]} | {self.gameboard[5]} | {self.gameboard[6]}
--|---|----
{self.gameboard[1]} | {self.gameboard[2]} | {self.gameboard[3]}'''










def checker(icon, board):
    if board[1]==board[2]==board[3]==icon:
        return 1
    elif board[1]==board[5]==board[9]==icon:
        return 1
    elif board[2]==board[5]==board[8]==icon:
        return 1
    elif board[3]==board[6]==board[9]==icon:
        return 1
    elif board[3]==board[5]==board[7]==icon:
        return 1
    elif board[4]==board[5]==board[6]==icon:
        return 1
    elif board[7]==board[8]==board[9]==icon:
        return 1
    else:
        return 0







def inputverify(input):
    return input in [x for x in range(1,10)]



class tictactoe(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.players = []
        


    async def gameplay(self, ctx,player):
        await ctx.send("Provide a number from 1 to 9")
        ingame = True
        inp = await self.bot.wait_for('message')
        correctInput =  inputverify(int(inp.content))
        while not correctInput:
            await ctx.send("Please enter a valid location")
            inp = await self.bot.wait_for('message')
            correctInput = inputverify(inp.content)
        else:
            ingame = True
            while ingame:
                await ctx.send(player.display())
                kek = await self.bot.wait_for('message')
                await ctx.send(kek)
                print("end of operation")
                break
    






    def alreadyPlaying(self,user):
        for item in self.players:
            if item.name == user:
                return True
        return False





    @commands.command()
    async def playttt(self, ctx):
        if not self.alreadyPlaying(ctx.author):
            self.players.append(player(ctx.author))
            await ctx.send(self.players[-1])
            await self.gameplay(ctx=ctx, player=self.players[-1])

        else:
            await ctx.send("Sorry, this user is already in game")





def setup(client):
    client.add_cog(tictactoe(client))