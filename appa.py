import discord
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='uwu ',help_command=None)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Lista de Comandos", description='<:Pablo0:782755700677541898>**Random**\nHola\n\n<:UwU:801886649469632562>**NSFW**\nTraps\n\n<:gabobb:787384850922995732>**Musica**\nTrabajando en eso\n\nRecuerda usar estos comandos despues del prefijo "uwu ". \nEspero haberte ayudado. <:like:783029416812609556>', color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def hola(ctx):
    await ctx.reply('Hola \*Sonido de Appa\*')

@bot.command()
async def kill(ctx):
    await ctx.reply('Ciao')
    sys.exit("Appa has left the chat")

@bot.command()
async def traps(ctx):
     embed=discord.Embed(title="Sike!", color=0xFF5733)
     embed.set_image(url="https://c.tenor.com/synaMy5G9VoAAAAC/appa-avatar.gif")
     await ctx.send(embed=embed)
    
    
bot.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')
