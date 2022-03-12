import discord
from discord.ext import commands

# # TODO: implementar al bot


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if len(message.attachments) > 0:
            attachment = message.attachments[0]
        else:
            return
        if attachment.filename.endswith(".jpg") or attachment.filename.endswith(".jpeg") or attachment.filename.endswith(".png") or attachment.filename.endswith(".webp") or attachment.filename.endswith(".gif"):
            self.image = attachment.url
        elif "https://images-ext-1.discordapp.net" in message.content or "https://tenor.com/view/" in message.content:
            self.image = message.content

    @commands.command(name="t")
    async def other_function(self, ctx):
        e = discord.Embed()
        e.set_image(url=self.image)
        await ctx.send(embed=e)
