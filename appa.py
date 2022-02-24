from http import client
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='uwu')

client = discord.client()

@client.event 
async def on_ready():
    print('Appa is now logged in as (0.user)'.format(client))

@bot.command()
async def hola(ctx):
    await ctx.reply('Que pedo pinches puercas \*Sonido de Appa\*')
    
bot.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')