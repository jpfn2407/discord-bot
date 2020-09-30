import discord, time, ffmpeg
from random import choice
from keys import *
from discord.ext import commands

bot = commands.Bot(command_prefix = '>')

@bot.event
async def on_ready():
    print('Bot is online.')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')   

@bot.command()
async def ya(ctx):
    await ctx.send(f'foda-se')

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    
    try:
        vc.play(discord.FFmpegPCMAudio('./audio/bye.mp3'), after=lambda e: print('Played the sound:', e))
    except:
        await ctx.send(f'yah mpt, não deu') 

    time.sleep(3)

    try:
        await member.move_to(channel=None)
    except:
        pass    

    server = ctx.message.guild.voice_client
    await server.disconnect()
    
@bot.command()
async def cut(ctx, member : discord.Member, *, reason=None):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    
    try:
        vc.play(discord.FFmpegPCMAudio('./audio/like_yo_cut_g.mp3'), after=lambda e: print('Played the sound:', e))
    except:
        await ctx.send(f'yah mpt, não deu') 

    time.sleep(2)
    
    try:
        await member.move_to(channel=None)
    except:
        pass    

    server = ctx.message.guild.voice_client
    await server.disconnect()

@bot.command()
async def kick_random(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    #try:      
    vc.play(discord.FFmpegPCMAudio('./audio/russianroulette.mp3'), after=lambda e: print('Played the sound:', e))
    #except:
        #await ctx.send(f'yah mpt, não deu')

    user = choice(ctx.message.author.voice.channel.members)

    time.sleep(7) 
    
    await user.move_to(channel=None)
    await ctx.send(f'BYE BYE %s'%user.mention)

    server = ctx.message.guild.voice_client
    await server.disconnect()

    
bot.run(BOT_TOKEN)    
