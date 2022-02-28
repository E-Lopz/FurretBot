## This bot needs a previous installation of FFMPEG.
import discord
import sys
from discord.ext import commands
import yt_dlp
import os
import random

beenCalled = False
noStreetName = ""

client = commands.Bot(command_prefix='uwu ',help_command=None) # Creates our bot

# When  the bot is ready, it warns us in the terminal
@client.event
async def on_ready():
    print("Appa is now at your service")

# Handles each message sent in the server
@client.event
async def on_message(ctx):
    global beenCalled
    global noStreetName
    name = ctx.author.name # String with the name of the message remitent
    # Gives a random probability to respond to the message sent
    if name != "Appa": # The bot cannot respond to himself
        randomInt = random.randrange(1,20,1)
        if randomInt == 2: # Random response with a probability of 1/20
            str = "Callate a la verga "+name
            await ctx.reply(str)
        # This response is composed in two parts, Appa saves the name of the person, he responded to the first time 
        if (randomInt == 5) or (name == noStreetName): # Random response with a probability of 1/20
            if  beenCalled and name == noStreetName: # If its the second time and its the same person
                await ctx.reply("te pregunto, te falta calle hermano")
                beenCalled = False # Reinitializes the variable
                noStreetName = " " # Reinitializes the variable
            else: # Its the first time
                await ctx.reply("Quien?")
                beenCalled = True 
                noStreetName = name # Saves the name
    await client.process_commands(ctx) # if the message is a command, processes it 


## Text related commands
    
# Sends an embed with all the commands and a little extra information
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Lista de Comandos", description='<:Pablo0:782755700677541898>**Random**\nHola\n\n<:UwU:801886649469632562>**NSFW**\nTraps\n\n<:gabobb:787384850922995732>**Musica**\n\Play "la rola"\n\nRecuerda usar estos comandos despues del prefijo "uwu ". \nEspero haberte ayudado. <:like:783029416812609556>', color=0xFF5733)
    await ctx.send(embed=embed)

# Appa says hello!
@client.command()
async def hola(ctx):
    await ctx.reply('Hola \*Sonido de Appa\*')

# This command kills Appa, it ends the execution Appa
@client.command()
async def morir(ctx):
    await ctx.reply('Ciao') # Appa says bye before leaving
    sys.exit("Appa has left the chat")

# This command sends an embed with a gif attached
@client.command()
async def traps(ctx):
    # Builds the embed
    embed=discord.Embed(title="Sike!", color=0xFF5733)
    embed.set_image(url="https://c.tenor.com/synaMy5G9VoAAAAC/appa-avatar.gif")
    await ctx.send(embed=embed)


## Music related commands

# Appa joins a voice channel and plays the audio of the url given
@client.command()
async def play(ctx, *,url : str):
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
    ydl_options = {'format': 'bestaudio/best','postprocessors' : [{'key': 'FFmpegExtractAudio', 'preferredcodec' : 'mp3','preferredquality':'192'}], 'noplaylist': True,
    'default_search': 'auto',}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith('.mp3'):
            print("ya llegue")
            os.rename(file,"song.mp3")
            print("ya llegue")      
    vc.play(discord.FFmpegPCMAudio(source='song.mp3'))

# Appa leaves the voice channel if he's in one
@client.command()
async def leave(ctx):
    vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if vc != None:
        await vc.disconnect()

@client.command()
async def pause(ctx):
    vc = vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    try:
        vc.pause()
    except:
        print("Appa no puede pausar")
      
@client.command()
async def resume(ctx):
    vc = vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    try:
        vc.resume()
    except:
        print("Appa no puede continuar")

@client.command()
async def stop(ctx):
    vc = vc = discord.utils.get(client.voice_clients,guild = ctx.guild)
    try:
        vc.stop()
    except:
        print("Appa no puede parar")
  
    
client.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')
