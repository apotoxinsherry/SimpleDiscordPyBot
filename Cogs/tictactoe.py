import nextcord as discord
from nextcord.ext import commands
from random import randint

#to-do:
#implement a users-in-game function which prevernts already existing users from re-running the command again. 
#implement the actual game logic
#create a tic-tac-toe player class for each player, which keeps track of each player's data
#this new class is inherited by or an instance of the class is declared within the class which has commands.Cog


board = ['','X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'X']

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





def clearboard():
    global board
    board = [""]*10


def inputverify(input):
    return input in range(1,10)



class tictactoe(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.choices = ['X', 'O']
        self.pchoice = ''
        self.cchoice = ''
        self.board = f'''
{board[7]} | {board[8]} | {board[9]}
---|------
{board[4]} | {board[5]} | {board[6]}
--|---|----
{board[1]} | {board[2]} | {board[3]}'''


    def initialize(self):
        clearboard()

    async def drawboard(self, ctx): 
        await ctx.send(self.board)

    

    @commands.Cog.listener()
    async def on_message(self, message):
        inp = await self.bot.wait_for('message')
        print(inp)


    async def gameplay(self, ctx):
        await ctx.send("Provide a number from 1 to 9")
        inp = await ctx.wait_for('message')
        correctInput = inputverify(inp)
        if correctInput:
            await ctx.send(inp)
        else:
            await ctx.send("Please provide a valid number")


    @commands.command()
    async def playttt(self, ctx, choice):
        self.player = ctx.author
        self.inGame = True
        if choice.capitalize() not in self.choices:
            await ctx.send("Please provide a valid choice and re-run the command")
        else:
            self.pchoice = choice.capitalize()
            self.choices.remove(self.pchoice)
            self.cchoice = self.choices[0]
            await self.drawboard(ctx=ctx)
            await ctx.send(f"User Choice: {self.pchoice}")
            await ctx.send(f"Computer Choice: {self.cchoice}") 
            await self.gameplay()
        

    
    


    

    @playttt.error
    async def playttt_error(self, ctx, error):
        await ctx.send("Please provide a kek")




    


        













def setup(client):
    client.add_cog(tictactoe(client))