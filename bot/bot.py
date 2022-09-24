import discord
from config import Discord_Token
from discord.ext import commands
from modules import ticker 

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

    response = ticker.get_data(arg)

    await ctx.send(response)


