import discord
from bot.config import Discord_Token
from discord.ext import commands
from modules import ticker 

TOKEN = Discord_Token
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')


@bot.command()
async def get(ctx, arg):

    response = await ticker.get_data(arg)
    await ctx.send(response)

bot.run(TOKEN)
