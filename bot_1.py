# ON MESSAGE FUNCION HAS PROIRITY OVER COMMAND.

import discord
from discord.ext import commands
import asyncio
import datetime
import youtube_dl

TOKEN = 'NTYxNDU4ODcyOTYzODI1NjY3.XJ8h1g.85m9kbVEBJJBDGeChU5mgQIB7SY'
client = commands.Bot(command_prefix='!')

players = {}


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Testing myself....'))
    print('Bot is ready!')


'''@bot.event 
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))'''


# ping pong
@client.command()
async def ping():
    await client.say('Pong')

# chutiya
@client.command()
async def chutiya():
    await client.say('Tu chutiya!')

# Lets Ehco everything
@client.command()
async def echo(*args):
    '''This will make an echo'''
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
# Motivate me   
@client.command()
async def utha():
    sentence = '```Kaam kar bey, uthh!```'
    await client.say(sentence)

# Motivate me
@client.command()
async def uthalerebaba():
    sentence = '```Mairkuu nahi rey, innn dono ko!```'
    await client.say(sentence)



'''Date'''
# Lets print the date
@client.command()
async def date():
    #today = datetime.date.today()
    #sentence = 'Today is ' + today
    #await client.say(today)
    today = datetime.datetime.now()
    sentence = '```Today is {: %B %d, %Y}. Have a sexy day!```'.format(today)
    await client.say(sentence)




        
# Lets clear the clutter.
@client.command(pass_context=True)
async def clear(ctx, amount=2):
    # first get the channel 
    channel = ctx.message.channel
    # make a list of messages
    messages = []
    # iterate through messages in a channel
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Messages deleted.")




# lets Math.
'''add'''
@client.command()
async def add(a: int, b : int):
    await client.say(str(a + b))
'''subtract'''
@client.command()
async def subtract(a: int, b: int):
    await client.say(str(a - b))
'''multiply'''
@client.command()
async def multiply(a: int, b: int):
    await client.say(str(a * b))
'''divide'''
@client.command()
async def divide(a: int, b: int):
    await client.say(str(a / b))
'''modulous'''
@client.command()
async def modulous(a: int, b: int):
    await client.say(str(a % b))



'''Display Embed info'''

@client.command()
async def showinfo():
    # Creating embed
    embed = discord.Embed(
        title = 'Regix Bot',
        description = 'Made for learning purpose.',
        color = discord.Color.blue()
    )
    # modify embed
    embed.set_footer(text='The end')
    embed.set_image(url='https://media.discordapp.net/attachments/360451295699795968/570306966979870739/pepochair.gif')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/360451295699795968/570307322707050503/mona.gif?width=203&height=300')
    #embed.author(name='Arsen1c', icon_url='https://i.pinimg.com/originals/4d/0c/9d/4d0c9deece33de55ad09dc59d4994b23.jpg')
    embed.add_field(name='!ping', value='pong', inline=False)
    embed.add_field(name='!date', value='Month Day, Year', inline=True)
    embed.add_field(name='!chutiya', value='Tu chutiya!', inline=True)
    #embed.add_field(name='Server ID', value=id, inline=True)

    await client.say(embed=embed)


'''Lets play some music now'''
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command(pass_context=True)
async def dc(ctx):
    # access the voice client and disconnect the voice client.
    server = ctx.message.server
    # instance of bot being in a voice channel
    voice_client = client.voice_client_in(server)
    await voice_client.vc.disconnect() 
   

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    # creating the player
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()





client.run(TOKEN)  