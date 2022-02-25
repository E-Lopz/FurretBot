## This bot needs a previous installation of FFMPEG.
import discord
import sys
from discord.ext import commands
import youtube_dl

client = commands.Bot(command_prefix='uwu ',help_command=None)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Lista de Comandos", description='<:Pablo0:782755700677541898>**Random**\nHola\n\n<:UwU:801886649469632562>**NSFW**\nTraps\n\n<:gabobb:787384850922995732>**Musica**\nTrabajando en eso\n\nRecuerda usar estos comandos despues del prefijo "uwu ". \nEspero haberte ayudado. <:like:783029416812609556>', color=0xFF5733)
    await ctx.send(embed=embed)

@client.command()
async def hola(ctx):
    await ctx.reply('Hola \*Sonido de Appa\*')

@client.command()
async def morir(ctx):
    await ctx.reply('Ciao')
    sys.exit("Appa has left the chat")

@client.command()
async def traps(ctx):
     embed=discord.Embed(title="Sike!", color=0xFF5733)
     embed.set_image(url="https://c.tenor.com/synaMy5G9VoAAAAC/appa-avatar.gif")
     await ctx.send(embed=embed)

@client.command()
async def play(ctx, url : str):
    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    vc.play(discord.FFmpegPCMAudio(source='song.mp3'))

    
    
client.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')
