import discord
from config import Discord_Token
from discord.ext import commands

TOKEN = Discord_Token
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.event
async def on_error(event, *args):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@bot.command
async def get_ticker_data(ctx, arg):
    # arg will be ticker to query 
    try:
        response = "get data function here" # response data from ticker.py
    except:
        response = (f'{arg} is not a valid ticker')

    await ctx.send(response) # response 


