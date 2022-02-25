import discord
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='uwu ',help_command=None)

@bot.command()
async def help(ctx):
    await ctx.send('Lista de Comandos\n <:Pablo0:782755700677541898>Random\n-hola: Appa te manda un saludote.\n<:UwU:801886649469632562>NSFW\n-traps\n<:gabobb:787384850922995732>Musica\n-trabajando en eso\nRecuerda usar estos comandos despues del prefijo "uwu " espero haberte ayudado <:like:783029416812609556>')

@bot.command()
async def hola(ctx):
    await ctx.reply('Hola \*Sonido de Appa\*')

@bot.command()
async def kill(ctx):
    await ctx.reply('Ciao')
    sys.exit("Appa has left the chat")
    
bot.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')
