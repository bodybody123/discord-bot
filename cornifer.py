from http.client import responses
import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from hentai import Hentai, Format
import requests
import urllib.parse
import json
import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ["1.1.1.1", "1.0.0.1", "2606:4700:4700::1111", "2606:4700:4700::1001"]

load_dotenv()
TOKEN = os.getenv('TOKEN')
environtment = os.getenv('ENVIRONTMENT')

intents = discord.Intents.all()

client = commands.Bot(command_prefix='c!', intents=intents)
e = discord.Embed()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

@client.command()
async def nhentai(ctx, arg):

    try:
        if arg.isnumeric():
            response: dict = None
            doujin = await Hentai(int(arg), json=response)
            if Hentai.exists(doujin.id):
                embed = discord.Embed(
                    title = doujin.title(Format.Pretty),
                    colour = discord.Colour.blue()
                ) 

                embed.set_thumbnail(url=doujin.image_urls[0])
                embed.set_image(url=doujin.image_urls[0])
                embed.add_field(name='Artist', value=doujin.image_urls[0], inline=False)
                embed.add_field(name='Tags', value=[tag.name for tag in doujin.tag], inline=False)
                embed.add_field(name='Sauce', value=f"https://nhentai.net/g/{int(arg)}", inline=False)

                await ctx.send(embed=embed)

        else:
            await ctx.send('Bro your nuke code is stupid')
    except requests.exceptions.RequestException as e:
        ctx.send('Shits dead just give up horny asshole')

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

@client.command()
async def bomb(ctx, tag='loli'):
    try:
        url = f'https://yande.re/post.json?tags={tag}&limit=100'

        response = requests.get(url, resolver)

        # data = convertJson(response.json())
        data = response.json()

        samples = random.sample(data, 5)

        for bob in samples :
            await ctx.send(bob['jpeg_url']);
    except requests.exceptions.RequestException as e:
        if environtment == 'production':
            await ctx.send('It seems I unable to satisfy your needs you horny fucker')
        else:
            await ctx.send(e)

def convertJson(jsonData):
    return jsonData[random.randrange(0,100)]['jpeg_url']

client.run(TOKEN)
