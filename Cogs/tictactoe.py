import nextcord as discord
from nextcord.ext import commands

board = [''*10]

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


