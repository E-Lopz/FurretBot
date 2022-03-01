## This bot needs a previous installation of FFMPEG.
import discord
from discord.ext import commands
import yt_dlp
import os
import random 
import time

beenCalled = False
noStreetName = ""
musicQueue = []

client = commands.Bot(command_prefix='uwu ',help_command=None) # Creates our bot

# When  the bot is ready, it warns us in the terminal
@client.event
async def on_ready():
    print("Furret is now at your service")

# Handles each message sent in the server
@client.event
async def on_message(ctx):
    if not ctx.content.startswith('uwu'):# if the message is a command, processes it 
        global beenCalled
        global noStreetName
        # String with the name of the message remitent
        name = ctx.author.name 
        # Gives a random probability to respond to the message sent
        upperBound = 25;
        # Self response less likely.
        if name == "Furret":
          upperBound += 100
          
        randomInt = random.randrange(1,upperBound,1)
        if randomInt <= 4: # Random response with a probability of 1/20
            str = "Me caes muy bien "+name+" :)"
            await ctx.reply(str)
        # This response is composed in two parts, Furret saves the name of the person, he responded to the first time 
        if (randomInt == 5) or (name == noStreetName): # Random response with a probability of 1/20
            if  beenCalled and name == noStreetName: # If its the second time and its the same person
                await ctx.reply("te pregunto, te falta calle hermano.")
                beenCalled = False # Reinitializes the variable
                noStreetName = " " # Reinitializes the variable
            else: # Its the first time
                await ctx.reply("Quien?")
                beenCalled = True 
                noStreetName = name # Saves the name
    else:
        await client.process_commands(ctx) 


## Text related commands
    
# Sends an embed with all the commands and a little extra information
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Lista de Comandos", description='<:Pablo0:782755700677541898>**Random**\nHola\n\n<:UwU:801886649469632562>**NSFW**\nTraps\n\n<:gabobb:787384850922995732>**Musica**\nPlay "la rola"\nLeave\nPause\nResume\n\nRecuerda usar estos comandos despues del prefijo "uwu ". \nEspero haberte ayudado. <:like:783029416812609556>', color=0xFF5733)
    await ctx.send(embed=embed)

# Furret says hello!
@client.command()
async def hola(ctx):
    await ctx.reply('Hola \*Sonido de Furret\*')

# This command sends an embed with a gif attached
@client.command()
async def traps(ctx):
    # Builds the embed
    embed=discord.Embed(title="Sike!", color=0xFF5733)
    embed.set_image(url="https://i.imgur.com/hj6zXD1.gif")
    await ctx.send(embed=embed)


## Music related commands

# Furret joins a voice channel and plays the audio of the url given
@client.command()
async def play(ctx, *,url : str):
    # Removes previous Song if present
    isSong = os.path.isfile("song.mp3")
    try:
        if isSong:
            os.remove("song.mp3")
    except PermissionError:
        return
    try:
        if discord.utils.get(client.voice_clients,guild = ctx.guild).is_playing():
          musicQueue.append(url)
          return
    except:
        print("puedes poner rolas")
    # Gets the voice channel of the author
    voiceChannel = ctx.author.voice.channel 
    # Is the bot already connected
    if discord.utils.get(client.voice_clients,guild = ctx.guild)==None:
        await voiceChannel.connect() 
        discord.utils.get(client.voice_clients,guild = ctx.guild).play(discord.FFmpegPCMAudio(source='caminar.mp3'),)
  
    vCl = discord.utils.get(client.voice_clients,guild = ctx.guild) 
    # YDLP parameters
    ydl_options = {'format': 'bestaudio/best',
                   'postprocessors' : [
                     {'key': 'FFmpegExtractAudio',
                      'preferredcodec' : 'mp3',
                      'preferredquality':'192'}
                   ], 
                   'noplaylist': True, 
                   'default_search': 'auto'}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
        # Extracts information, returns a dictionary
        info = ydl.extract_info(url,download=False) 
        title = info.get("title",None)
        # Sends an embed with important information
        embed = discord.Embed(title="Ahora estas escuchando:", description=title,color=0xFF5733)
    # Finds the requested mp3 file and renames it
    for file in os.listdir("./"):
        if file.endswith('.mp3') and file!=("caminar.mp3"):
            os.rename(file,"song.mp3")

    # Wait for critical bot announcement.
    time.sleep(8)
    await ctx.send(embed=embed)
    vCl.play(discord.FFmpegPCMAudio(source='song.mp3'),after=lambda e: playQueue(ctx, vCl)) # Plays the mp3

# Furret leaves the voice channel if he's in one
@client.command()
async def leave(ctx):
    vCl = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if vCl != None:
        await vCl.disconnect()

# Furret pauses the current song
@client.command()
async def pause(ctx):
    vCl = discord.utils.get(client.voice_clients,guild = ctx.guild)
    try:
        vCl.pause()
    except:
        print("Furret no puede pausar")

# Furret resumes the current song 
@client.command()
async def resume(ctx):
    vCl = discord.utils.get(client.voice_clients,guild = ctx.guild)
    try:
        vCl.resume()
    except:
        print("Furret no puede continuar")

# Furret stops playing the song and clears the queue
@client.command()
async def stop(ctx):
    vCl = discord.utils.get(client.voice_clients,guild = ctx.guild)
    try:
        vCl.stop()
    except:
        print("Furret no puede parar")

def playQueue(ctx,vCl):
  global musicQueue
  print(musicQueue)
  if musicQueue != []:
    #Removes previous Song if present
    isSong = os.path.isfile("song.mp3")
    try:
        if isSong:
            os.remove("song.mp3")
    except PermissionError:
        return
    url=musicQueue.pop(0)
     # YDLP parameters
    ydl_options = {'format': 'bestaudio/best',
                   'postprocessors' : [
                     {'key': 'FFmpegExtractAudio',
                      'preferredcodec' : 'mp3',
                      'preferredquality':'192'}
                   ], 
                   'noplaylist': True, 
                   'default_search': 'auto'}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
      ydl.download([url])
      # Extracts information, returns a dictionary
      #info = ydl.extract_info(url,download=False) 
      #title = info.get("title",None)
      # Sends an embed with important information
      #embed = discord.Embed(title="Ahora estas escuchando:", description=title,color=0xFF5733)
    # Finds the requested mp3 file and renames it
    for file in os.listdir("./"):
      if file.endswith('.mp3') and file!=("caminar.mp3"):
        os.rename(file,"song.mp3")
    #await ctx.send(embed=embed)
    vCl.play(discord.FFmpegPCMAudio(source='song.mp3'),after=lambda e: playQueue(ctx, vCl)) # Plays the mp3 

    def songdl(ctx,url)
  
    
client.run('OTQ2NDc4ODYyNjE3OTUyMjk3.YhfTIQ.mrJqA1O2084PQInBAUYixUj1NHc')