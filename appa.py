## This bot needs a previous installation of FFMPEG.
import discord
import sys
from discord.ext import commands
import youtube_dl
import os
import random
import math

client = commands.Bot(command_prefix='uwu ',help_command=None)

@client.event
async def on_ready():
    print("Appa is now at your service")

@client.event
async def on_message(ctx):
    randomInt = random.randrange(1,10,1)
    if randomInt==2:
        name = ctx.author.name
        str = "Callate a la verga "+name
        await ctx.reply(str)
    
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Lista de Comandos", description='<:Pablo0:782755700677541898>**Random**\nHola\n\n<:UwU:801886649469632562>**NSFW**\nTraps\n\n<:gabobb:787384850922995732>**Musica**\Play "la rola"\n\nRecuerda usar estos comandos despues del prefijo "uwu ". \nEspero haberte ayudado. <:like:783029416812609556>', color=0xFF5733)
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
    isSong = os.path.isfile("song.mp3")
    try:
        if isSong:
            os.remove("song.mp3")
    except PermissionError:
        ctx.send("espera a que acabe la cancion")
    voiceChannel = ctx.author.voice.channel
    if discord.utils.get(client.voice_clients,guild = ctx.guild)==None:
        await voiceChannel.connect()    
    vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    ydl_options = {'format': 'bestaudio/best','postprocessors' : [{'key': 'FFmpegExtractAudio', 'preferredcodec' : 'mp3','preferredquality':'192'}],}
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith('.mp3'):
            print("ya llegue")
            os.rename(file,"song.mp3")
            print("ya llegue")
    vc.play(discord.FFmpegPCMAudio(source='song.mp3'))

@client.command()
async def leave(ctx):
    vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if vc!=None:
        await vc.disconnect()
    
    
client.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')
