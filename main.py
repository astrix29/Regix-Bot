
import discord
from discord.ext import commands
import asyncio
import datetime
import time

# This is prefix of my bot
client = commands.Bot(command_prefix='!')


@client.event       
async def on_ready():
    game = '<playing>'
    #url= 'https://www.twitch.tv/cohhcarnage'
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=game))
    #Twitching
    #await client.change_presence(status=discord.Status.idle,activity=discord.Streaming(name='Twitching', url=url))#, afk=False)
    print('Marathi mansa jaga hooo!')
    #await message.channel(f'``Marathi mansaa jagaa hooo!!``')


@client.event
async def on_message(message):
    server = client.get_guild(<add_guild_number_here>)
    # Lets count the number of memebers.
    if '!members' == message.content.lower():
        await message.channel.send(f'```py\nThis server has {server.member_count} members```')
    
    # Lets grab the server/guid's icon.
    elif '!server_icon' == message.content.lower():
        show_icon = discord.Embed(
            color = discord.Color.dark_grey()
        )
        show_icon.set_image(url='{}'.format(server.icon_url))
        #show_icon.set_footer(text=':disappointed:')
        await message.channel.send(embed=show_icon)
        #await message.channel.send(server.icon_url)    

    # Server Report
    elif "!members_report" == message.content.lower():
        online = 0
        idle = 0
        offline = 0
        dnd = 0

        for m in server.members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            if str(m.status) == "idle":
                idle += 1
            if str(m.status) == "dnd":
                dnd += 1

        await message.channel.send(f"```py\nOnline: {online}\nIdle/busy/dnd: {idle}\nDnd: {dnd}\nOffline: {offline}```")

        # Lets log out.
    elif "!logout" == message.content.lower():
        await client.close()
    
    #  Server region
    elif "!server_region" == message.content.lower():
        await message.channel.send(f'```{server.region}```')

    await client.process_commands(message)
    
    
# send DM
@client.command()
async def dm(ctx):
    await ctx.author.send('<DM_MESSAGE>')


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send('``Pong``')

# chutiya
@client.command()
async def chutiya(ctx): 
    await ctx.send('``Tu chutiya!``')
# waste command
@client.command()
async def hey(ctx):
    await ctx.send('``Hey, sexy!``')

# waste command
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
# wasted command . Motivate me   
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

# getting users avatar
@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar  = discord.Embed(

        color = discord.Color.dark_blue() # select any color
    )
    show_avatar.set_footer(text='Here\'s {}\'s avatar. Mmmm looks sexy!'.format(member))
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

'''# theres also an alternative to this command or a simplified version
@client.command()
async def avatar(ctx, member: discord.Member):
    await ctx.send('{}'.format(member.avatar_url))

    # save and run it.'''

# Lets get server icon
@client.command()
async def servericon(ctx):
    await ctx.send(discord.Guild.icon_url)



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




@client.command(pass_context=True, aliases=['google'])
async def query(ctx, *args):
    """
    Just a simple lmgtfy command embeding the link into the message.*
    *Links are still visible because discord asks you if this link is safe :/
    """
    if args:
        url = "http://lmgtfy.com/?q=" + "+".join(args)
        await ctx.send(embed=discord.Embed(description="**[Try this solution...](%s)**" % url, color=discord.Color.darker_grey()))
    #await client.delete_message(ctx.message)


TOKEN = 'YOUR_TOKEN_HERE'
client.run(TOKEN)
