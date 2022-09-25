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
        self.ingame = False
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


def placeicon_user(location, icon, board):
    board[location]=icon

def placeicon_computer(icon, board):
    location = randint(1,9)
    board[location]=icon

def isTie(board):
    tie = True
    for i in range(1,10):
        if board[i]==' ':
            tie = False
            return tie
    
    return tie





class tictactoe(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.players = []


    async def getInput(self,ctx):
        await ctx.send("Enter a number from 1 to 9")
        inp = await self.bot.wait_for("message")
        validInput = [1,2,3,4,5,6,7,8,9, 'q']
        print(inp.content)
        while inp.content not in validInput: #check what kind of input are we getting from the user and find a way to convert it into int.
            await ctx.send("Please enter a valid input") # look into the nextcord docs, prolly
            inp = await self.bot.wait_for('message')
        
        return inp



    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return

        


    async def gameplay(self, ctx,player):
        player.ingame = True
        while player.ingame:
            await ctx.send(player.display())
            inp = await self.getInput(ctx=ctx)

            if(inp=='q'): # check for user to quit in middle of the game. 
                player.ingame=False
                self.removeplayer(player=player)


            if isTie(player.gameboard):
                await ctx.send("It's a Tie")
                self.removeplayer(player=player)
                break

            if checker(player.uchoice, player.gameboard):
                await ctx.send("Player has won!")
                self.removeplayer(player)
                break

            if checker(player.cchoice, player.gameboard):
                await ctx.send("Computer has won1")
                self.removeplayer(player)
                break
            
            await ctx.send("Enter the location of the icon to be placed:")

            
            

            while(True):    #loop to check if the position has already been filled. If filled, asks the user to enter a new position. If not, confinues with the loop. 

                loc = int(inp.content)

                if(player.board[loc]!=' '):
                    await ctx.send("This location has already been filled. Please enter another location")   
                    inp = await self.getInput(ctx=ctx)
                else:
                    break

            
            placeicon_user(loc, player.uchoice, player.gameboard)
            placeicon_computer(player.cchoice, player.gameboard)
            inp = await self.getInput(ctx=ctx)




    




    def removeplayer(self, player):
        for item in self.players:
            if item.name == player.name:
                player.ingame = False
                self.players.remove(player)




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
            #implement a check here to send the user back to gameplay





def setup(client):
    client.add_cog(tictactoe(client))