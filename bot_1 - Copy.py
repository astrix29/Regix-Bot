# ON MESSAGE FUNCION HAS PROIRITY OVER COMMAND.

import discord
from discord.ext import commands
import asyncio
import datetime
import time
import youtube_dl


TOKEN = 'XXXXXXXXXXXXXXXXXXXx'
client = commands.Bot(command_prefix='!')



@client.event
async def on_ready():
    game = discord.Game('looking for raju')
    await client.change_presence(status=discord.Status.idle,activity=game, afk=True)
    print('Bot is ready!')

'''@client.event
async def on_message(message):
    author = message.author
    if message.content.startswith('!dm'):
        await message.author.send('I love you!')'''

'''@bot.event 
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))'''

@client.command()
async def dm(ctx):
    await ctx.author.send('``I love you!``')


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send('``Pong``')

# chutiya
@client.command()
async def chutiya(ctx): 
    await ctx.send('``Tu chutiya!``')

@client.command()
async def hey(ctx):
    await ctx.send('``Hey, sexy!``')


'''Users Avatar'''

'''@client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await ctx.send("{}".format(member.avatar_url))'''

@client.command()
async def avatar(ctx, member: discord.Member):  
    #await ctx.send("{}".format(member.avatar_url))
    show_avatar = discord.Embed(

        title = 'Ye le tera Avatar!',
        color = discord.Color.dark_grey()
    )
    show_avatar.setfooter(text='Here\'s {}\'s Avatar. Mmmm looks sexy!'.format(member))
    show_avatar.set_image(url="{}".format(member.avatar_url))
    
    await ctx.send(embed=show_avatar)

@client.command()
async def stop(ctx):
    await ctx.send('``Aaj mairku rokna nahi re baba``')



# Lets Ehco everything
@client.command()
async def echo(ctx,*args):
    '''This will make an echo'''
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)
# Motivate me   
@client.command()
async def utha(ctx):
    sentence = '``Kaam kar bey, uthh!``'
    await ctx.send(sentence)

# Motivate me
@client.command()
async def uthalerebaba(ctx):
    sentence = '``Mairkuu nahi rey, innn dono ko!``'
    await ctx.send(sentence)



'''Date'''
# Lets print the date
@client.command()
async def datetime(ctx):
    #today = datetime.date.today()
    #sentence = 'Today is ' + today
    #await ctx.send(today)
    today = time.ctime()
    sentence = '```It\'s {}. Have a sexy day!```'.format(today)
    await ctx.send(sentence)

@client.command()
async def date(ctx):
    #today = datetime.date.today()
    #sentence = 'Today is ' + today
    #await client.say(today)
    today = datetime.datetime.now()
    sentence = '```Today is {: %B %d, %Y}. Have a sexy day!```'.format(today)
    await ctx.send(sentence)






        
# Lets clear the clutter.
@client.command(pass_context=True)
async def clear(ctx, amount=2):
    # first get the channel 
    channel = ctx.message.channel
    # make a list of messages
    messages = []
    # iterate through messages in a channel
    async for message in ctx.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await ctx.delete_messages(messages)
    await ctx.send("Messages deleted.")




# lets Math.
'''add'''
@client.command()
async def add(ctx, a: int, b : int):
    await ctx.send('``Ans. ``' + str(a + b))
'''subtract'''      
@client.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a - b))
'''multiply'''
@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a * b))
'''divide'''
@client.command()
async def divide(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a / b))
'''modulus'''
@client.command()
async def modulus(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a % b))



'''Display Embed info'''

@client.command()
async def showinfo(ctx):
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

    await ctx.send(embed=embed)

'''Help Command'''
@client.command()
async def helpme(ctx):
    embed_help = discord.Embed(
        title = 'Help arrived!',
        description = '**These are the available Help commands**:',
        color = discord.Color.blue()
    )
    embed_help.set_footer(text='Bas itna he.')
    embed_help.set_image(url='https://media.discordapp.net/attachments/530002554688503808/571677365755838474/15_avatar_middle.jpg')
    embed_help.set_thumbnail(url='https://media.discordapp.net/attachments/530002554688503808/571676560873226240/442350001805590538.gif')
    embed_help.add_field(name='!helpme', value='Show\'s available commands.', inline=False)
    embed_help.add_field(name='!datetime or !date', value='Shows date and time',inline=False)
    embed_help.add_field(name='!chutiya', value=' Chutiya you back.',inline=False)
    embed_help.add_field(name='!uthalerebaba', value='Complete\'s Baburao\'s statement.' ,inline=False)
    embed_help.add_field(name='!utha', value='Wakes you up.',inline=False)
    embed_help.add_field(name='!zapinsta', value='Zapper\'s instagram ',inline=False)
    embed_help.add_field(name='!nicinsta', value='Arsenic\'s instagram ',inline=False)
    #embed_help.add_field(name='!dm', value='Send\'s you a lovely DM',inline=False)
    embed_help.add_field(name='!add <first_number> <second_number>', value='Does Addition.',inline=False)
    embed_help.add_field(name='!subtract <first_number> <second_number>', value='Does Subtraction.',inline=False)
    embed_help.add_field(name='!divide <first_number> <second_number>', value='Does Division.',inline=False)
    embed_help.add_field(name='!multiply <first_number> <second_number>', value='Does Multplication.',inline=False)
    embed_help.add_field(name='!modulus <first_number> <second_number>', value='Gives the remainder.',inline=False)
    embed_help.add_field(name='!echo <your text here>', value='Repeats what you said(Including emoji\'s)',inline=False)

    await ctx.send(embed=embed_help)


'''Test'''
@client.command()
async def nicinsta(ctx):
    '''open_browser = webbrowser.open('https://www.instagram.com/_.cyph3r_/')
    await ctx.author.send(open_browser)'''
    nic = discord.Embed(
        #title = 'Instagram',
        #description = 'This is Arsenic\'s discord',
        color = discord.Color.purple()
    )
    nic.add_field(name='Arsenic\'s Instagram:', value='https://www.instagram.com/_.cyph3r_/')

    await ctx.send(embed=nic)
    
@client.command()
async def zapinsta(ctx):
    '''open_browser = webbrowser.open('https://www.instagram.com/ashishjustgotreal/')
    await ctx.author.send(open_browser)'''
    zap = discord.Embed(
        #title = 'Instagram',
        #description = 'This is Zapper\'s Instagram',
        color = discord.Color.purple()
    )
    zap.add_field(name='Zapper\'s Instagram:', value='https://www.instagram.com/ashishjustgotreal/')
    
    await ctx.send(embed=zap)



'''lets get the cats'''


'''Lets play some music now'''

client.run(TOKEN)  
