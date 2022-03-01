import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from hentai import Hentai, Format
import requests
import urllib.parse
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='c!')
e = discord.Embed()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('halo cornifer'):
        if message.author.id == 231777334791897088:
            await message.channel.send('halo bos seperti biasa?')
        else:
            await message.channel.send('sapa lu anjing sok kenal')




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
async def sauce(ctx):
    attachment_url = ctx.message.attachments[0].url
    req = requests.get(
        "https://api.trace.moe/search?url={}"
        .format(urllib.parse.quote_plus(attachment_url))
        ).json()

    trace = req['result'][0]

    embed = discord.Embed(
        title = trace['filename'],
        colour = discord.Colour.purple()
    )

    embed.set_thumbnail(url=trace['image'])
    embed.add_field(name='video preview', value=trace['video'], inline=False)
    embed.add_field(name='episode', value=trace['episode'])
    embed.add_field(name='similarity', value="{:.2f}".format(trace['similarity']))
    await ctx.send(embed=embed)

client.run(TOKEN)