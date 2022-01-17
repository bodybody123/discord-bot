import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from hentai import Hentai, Format
import requests
import urllib.parse

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


@client.command()
async def sauce(ctx, arg):
    # await ctx.send(
    #     requests
    #     .get("https://api.trace.moe/search?url={}"
    #     .format(urllib.parse.quote_plus(arg))).json())
    await ctx.send(requests.get("https://api.trace.moe/search?url={}".format(urllib.parse.quote_plus("https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"))).json())

client.run(TOKEN)
