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
    game = discord.Game('give_your_satus_name')
    await client.change_presence(status=discord.Status.idle,activity=game, afk=True)
    print('Bot is ready!')



@client.command()
async def dm(ctx):
    await ctx.author.send('``message_you_want_to_send_in_DM``')


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send('``Pong``')


'''Users Avatar. Simple version'''

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

# Lets Ehco everything. There's a simpler version available, google it.
@client.command()
async def echo(ctx,*args):
    '''This will make an echo'''
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)

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




# Simple math.
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
    embed_help.add_field(name='!zapinsta', value='Zapper\'s instagram ',inline=False)
    embed_help.add_field(name='!nicinsta', value='Arsenic\'s instagram ',inline=False)
    #embed_help.add_field(name='!dm', value='Send\'s you a DM',inline=False)
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
    '''open_browser = webbrowser.open('https://www.instagram.com/')
    await ctx.author.send(open_browser)'''
    nic = discord.Embed(
        #title = 'Instagram',
        #description = 'This is Arsenic\'s discord',
        color = discord.Color.purple()
    )
    nic.add_field(name='Arsenic\'s Instagram:', value='https://www.instagram.com/')

    await ctx.send(embed=nic)
    
@client.command()
async def zapinsta(ctx):
    '''open_browser = webbrowser.open('https://www.instagram.com/')
    await ctx.author.send(open_browser)'''
    url = "https://www.instagram.com/_.tapper._/"
    zap = discord.Embed(
        title = 'Instagram',
        description = "**[Zapper's insta](%s)**" % url,
        color = discord.Color.purple()
    )
    #zap.description("dnfkfn e")
    #zap.add_field(name='Zapper\'s Instagram:', value='https://www.instagram.com/ashishjustgotreal/')
    zap.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/599px-Instagram_icon.png')
    zap.set_footer(text="Updated")
    await ctx.send(embed=zap)
    
# Little bit of webscraping(Use it at your own risk)
@client.command()
async def getgeek(ctx):
    URL='https://geeksforgeeks.org'
    response = requests.get(URL)

    parsed_data = bs4.BeautifulSoup(response.text)
    all_links = parsed_data.select('a')

    for l in all_links:
        await ctx.send('``{}``'.format(l.get('href')))
   
# Getting location on google maps
@client.command()
async def whereis(ctx, *, content):
    cont = "https://www.google.com/maps/place/{}".format(content)
    icon = "https://colorlib.com/wp/wp-content/uploads/sites/2/google-maps-wordpress-plugins.png"
#     location = discord.Embed(
#         #title = 'Instagram',
#         #description = 'This is Zapper\'s Instagram',
#     color = discord.Color.purple()
#     )
#     # location.add_field(name='Here is what I found on google maps:', value=cont, inline=True)
#     location.add_field(description="**[Try this solution...](%s)**" % cont,value=" ",inline=True)

#     location.set_thumbnail(url='https://colorlib.com/wp/wp-content/uploads/sites/2/google-maps-wordpress-plugins.png')
    
#    # await ctx.send(embed=location)
#     if(len(content) < 1):
#         await ctx.send('``Error: Please give me a location to search!``')
#     else:
#         await ctx.send(embed=location)
    await ctx.send(embed=discord.Embed(title="Google Maps",description="**[Yaha dekho bhai...](%s)**" % cont, color=discord.Color.darker_grey(), inline=True).set_thumbnail(url=icon))


client.run(TOKEN)  
