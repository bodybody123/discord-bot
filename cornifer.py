import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from hentai import Hentai, Format

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='c!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

@client.command()
async def nhentai(ctx, arg):

    if arg.isnumeric():
        doujin = Hentai(arg)
        if Hentai.exists(doujin.id):
            await ctx.send(f'Title: {doujin.title} Artist: {doujin.artist} Tags: {[tag.name for tag in doujin.tag]} {doujin.image_urls}')
    else:
        return
client.run(TOKEN)
