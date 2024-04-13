cid = input("Channel ID: ")
token = input("Token: ")

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="nvm", intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f"Trying to send message as {client.user}")
    try:
        c = await client.fetch_channel(cid)
        m = await c.send("_ _")
        print(f"Message ID: {m.id}\nNow you can close this program")
    except Exception as e:
        print(f"I can't :/\nError: {e}")

client.run(token)