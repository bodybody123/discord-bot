import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from hentai import Hentai, Format

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='c!')
e = discord.Embed()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

@client.command()
async def nhentai(ctx, arg):

    if arg.isnumeric():
        doujin = Hentai(int(arg))
        if Hentai.exists(doujin.id):
            await ctx.send(f'''
                > Title: [{doujin.title(Format.Pretty)}](https://nhentai.net/g/{int(arg)}) 
                > Artist: {doujin.artist[0].name} 
                > {[tag.name for tag in doujin.tag]} 
                > {doujin.image_urls[0]} \
                ''')

    else:
        return
client.run(TOKEN)
