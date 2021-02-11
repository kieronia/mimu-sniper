from discord.ext import commands
import discord
prefix = "!"
token = "token here"
#token here - go in inspect element -> local storage -> filter items -> type token -> control r to reload -> see it and copy it (QUICKLY)
#tokens give access to your account - avoid anyone asking for your token or files that seem to send your token over a webhook
#changing your password should reset your token.
client = commands.Bot(prefix, self_bot=True)
@client.event
async def on_message(message):
    if message.author.id == 493716749342998541:
        embeds = message.embeds 
        for embed in embeds:
            info = embed.to_dict()
            try:
                description = info["description"].split("`")
                print(f"Sniping mimu drop with message \"{description[1]}\" ")
                await message.channel.send(description[1])
                print("Sniped successfully")

            except Exception as e:
                #print(e)
                pass
client.run(token, bot=False)
