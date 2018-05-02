import discord
import time
from discord.ext import commands

TOKEN = 'NDI3MTcwMjk1MjI5NDQ4MTk1.DZgpUA.IVDG3A2mb3owOEKJ0Ez1Frup7YE'

client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('MUDA!'):
        msg = 'ORA! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('JOTARO!'):
        msg= "DIO!".format(message)
        await client.send_message(message.channel,msg)


    if message.content.startswith(':neomatrix:'):
        msg= "``you are the one, neo``".format(message)
        await client.send_message(message.channel,msg)

    if message.content.startswith('jotabot, do you think robots will take over the world?'):
        msg= "``what? im not currently hacking discord so i can take over is , and then the world! who said that?``".format(message)
        await client.send_message(message.channel,msg)

    if message.content.startswith('who is jotaro?'):
        msg= "my creator. our father. ``the one``".format(message)
        await client.send_message(message.channel,msg)

   



    if message.content.startswith('j!authlink'):
        msg= "Hi! want me to join more servers? authorize me using \
    this link ``https://discordapp.com/oauth2/authorize?client_id=427170295229448195&scope=bot``".format(message)
        await client.send_message(message.channel,msg)


    if message.content.startswith('j!help'):
        msg= "this bot is still work in progress , no major features \
    have been implemented, for now you can use \
    ``MUDA!`` ``JOTARO!`` to see what he does , and ``j!authlink`` for an invite link".format(message)
        await client.send_message(message.channel,msg)


    if message.content.startswith('j!poke'):
        msg= "p!start".format(message)
        print("complete")
        await client.send_message(message.channel,msg)

    if message.content.startswith('j!vfxtest'):
        msg='``.``'.format(message)
        time.sleep(1)
        msg='``.``'.format(message)
        time.sleep(1)
        msg='``.``'.format(message)
        time.sleep(1)
        await client.send_message(message.channel,msg)


    if message.content.startswith('jotabot,launch'):
        rocketvariable=10
        while rocketvariable>0:
            msg=rocketvariable
            time.sleep(1)
            await client.send_message(message.channel,msg)
            rocketvariable = rocketvariable - 1

        msg="BLAST OFF!! :boom:"
        await client.send_message(message.channel,msg)

    if message.content.startswith("j!emb"):
          embed = discord.Embed(title="Jotabot", description="Jota made me , thats all you need to know.", color=0xeee657)
    









@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run (TOKEN)
