import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = os.getenv('YOUTUBE_API_TOKEN')


bot = commands.Bot(command_prefix='!')  # prefijo del Bot


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command(name="hi")
async def ping(ctx: commands.Context):
    await ctx.send(f"hola baby!!!!")


@bot.command(name='subs')
async def subscriptores(ctx, username):
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + KEY).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + \
        "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)


# funcion de suma
@bot.command(name='s')  # suma
async def sumar(ctx, num1, num2):
    response = int(num1) + int(num2)
    await ctx.send(response)


@bot.command(name='m')  # multiplicar
async def multiplicar(ctx, num1, num2):
    response = int(num1) * int(num2)
    await ctx.send(response)

bot.run(TOKEN)
