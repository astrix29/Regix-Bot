##### ON MESSAGE FUNCION HAS PROIRITY OVER COMMAND.
import discord
from discord.ext import commands
import asyncio
import datetime
import time
import json
import requests
from googletrans import Translator, constants
from bs4 import BeautifulSoup as bs
#import youtube_dl

#from googlesearch import search

TOKEN = 'NTYxNDU4ODcyOTYzODI1NjY3.XnSbUA.NoupjGFHCivfiwzgOg8qhOo_IY8'

client = commands.Bot(command_prefix='^')

#### On Ready
@client.event
async def on_ready():
    game = discord.Game('^helpme for help')
    await client.change_presence(status=discord.Status.online,activity=game, afk=True)
    print('Bot is ready!')

#### Dm user
@client.command()
async def dm(ctx):
    await ctx.author.send('**Ye DeviPrasad ka number nahi hai, phone rakh!**')

#### ping pong
@client.command()
async def ping(ctx):
    await ctx.send('**Pong! Bot is up and running!**')

'''
#### Simple Avatar Display
@client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await ctx.send("{}".format(member.avatar_url))
'''

#### Show me your Avatar
@client.command()
async def avatar(ctx, member: discord.Member=None):  
    #await ctx.send("{}".format(member.avatar_url))
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed(
        title = 'Ye le tera Avatar!',
        color = discord.Color.dark_grey()
    )
    #show_avatar.setfooter(text='Here\'s {}\'s Avatar. Mmmm looks sexy!'.format(member))
    show_avatar.set_image(url="{}".format(member.avatar_url))
    await ctx.send(embed=show_avatar)

#### ECHO command
@client.command(pass_context=True)
async def echo(ctx,*args):
    '''This will make an echo'''
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.channel.purge(limit=1)
    await ctx.send(output)

#### Clear command
@client.command(pass_context=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


#### Add
@client.command()
async def add(ctx, a: int, b : int):
    await ctx.send('``Ans. ``' + str(a + b))

#### Subtract
@client.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a - b))

#### Multiply
@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a * b))

#### Divide
@client.command()
async def divide(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a / b))

#### Modulus
@client.command()
async def modulus(ctx, a: int, b: int):
    await ctx.send('``Ans. ``' + str(a % b))

#### TimePass ShowInfo
@client.command()
async def showinfo(ctx):
    # Creating embed
    info_embed = discord.Embed(
        title = 'Regix Bot',
        description = 'Made for learning purpose.',
        color = discord.Color.blue()
    )
    # modify embed
    info_embed.set_footer(text='The end')
    info_embed.set_image(url='https://media.discordapp.net/attachments/360451295699795968/570306966979870739/pepochair.gif')
    info_embed.set_thumbnail(url='https://media.discordapp.net/attachments/360451295699795968/570307322707050503/mona.gif?width=203&height=300')
    #embed.author(name='Arsen1c', icon_url='https://i.pinimg.com/originals/4d/0c/9d/4d0c9deece33de55ad09dc59d4994b23.jpg')
    info_embed.add_field(name='!ping', value='pong', inline=False)
    info_embed.add_field(name='!date', value='Month Day, Year', inline=True)
    #embed.add_field(name='Server ID', value=id, inline=True)
    await ctx.send(embed=info_embed)

#### HELPME
@client.command()
async def helpme(ctx):
    embed_help = discord.Embed(
        title = 'Help arrived!',
        description = 'These are the available Help commands:',
        color = discord.Color.blue()
    )
    embed_help.set_footer(text='Bas itna hi.')
    embed_help.set_image(url='https://media.discordapp.net/attachments/530002554688503808/571677365755838474/15_avatar_middle.jpg')
    # embed_help.set_thumbnail(url='https://media.discordapp.net/attachments/530002554688503808/571676560873226240/442350001805590538.gif')
    # embed_help.add_field(name='``!helpme``', value=' ‎', inline=True)
    #embed_help.add_field(name='!dm', value='Send\'s you a DM',inline=False)
    embed_help.add_field(name='**add x y**', value='**Adds 2 numbers**',inline=True)
    embed_help.add_field(name='**subtract x y**', value='**Subtracts 2 numbers**',inline=True)
    embed_help.add_field(name='**divide x y**', value='**Divides 2 numbers**',inline=True)
    embed_help.add_field(name='**multiply x y**', value='**Multiple 2 numbers**',inline=True)
    embed_help.add_field(name='**modulus x y**', value='**Reminder of 2 numbers**',inline=True)
    embed_help.add_field(name='**echo**', value='**Repeats what you said**',inline=False)
    embed_help.add_field(name='**whereis <city>**', value='**Sends link of google maps**',inline=False)
    embed_help.add_field(name='**astroiss**', value='**Returns name[s] of Astronauts on ISS atm**',inline=False)
    embed_help.add_field(name='**yt video_link**', value='**Returns detailed info of a YouTube Video**',inline=False)
    embed_help.add_field(name='**avatar @member**', value='**Returns avatar of mentioned member**',inline=True)
    embed_help.add_field(name='**clear <amount>**', value='**Clears messages in a channel.**',inline=True)
    embed_help.add_field(name='**dm**', value='**Still not decided**',inline=True)
    await ctx.send(embed=embed_help)

#### Show on Google Maps
@client.command()
async def whereis(ctx, *, content):
    cont = "https://www.google.com/maps/place/{}".format(content)
    icon = "https://colorlib.com/wp/wp-content/uploads/sites/2/google-maps-wordpress-plugins.png"
    try:
        await ctx.send(embed=discord.Embed(title="Google Maps",description="**[Yaha dekho bhai...](%s)**" % cont, color=discord.Color.darker_grey(), inline=True).set_thumbnail(url=icon))
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send("Usage: !whereis <some_location>")
  
#### ASTROISS
@client.command()
async def astroiss(ctx):
    response = requests.get("http://api.open-notify.org/astros.json")
    # print(response) #working
    # def jprint(obj):
    json.dumps(response.json(), sort_keys=True, indent=4)
        # print(text)
    # gets the json request in proper manner
    # jprint(response.json())
    # Lets grab astronauts names
    astronauts = response.json()["people"]
    # jprint(astronauts)  # prints the PEOPE object
    astro_names = []
    for x in astronauts:
        names = x["name"]
        astro_names.append(names)
        # print(names)
    astroiss_embed = discord.Embed(
        title = 'Names of Astronauts on the ISS',
        description = f'There are ``{len(astro_names)} astronaut[s]`` in space atm ',
        color = discord.Color.blue()
    )
    astroiss_embed.set_thumbnail(url="https://economictimes.indiatimes.com/thumb/msid-68707249,width-1200,height-900,resizemode-4,imgsize-762936/iss.jpg?from=mdr")
    for idx, item in enumerate(astro_names, 1):
        astroiss_embed.add_field(name="‎‎‎‎‎ ‎", value=f"**{idx}**. ``{item}``",inline=False)
    await ctx.send(embed=astroiss_embed)

def get_video_info(url):
    # download html code
    request = requests.get(url)
    # create beautiful soup object to parse HTML
    soup = bs(request.content, 'html.parser')
    # initialize the result
    result = {}
    # video title
    result['title'] = soup.find('span', class_='watch-title').text.strip()
    # video views (converted to integer)
    result['views'] = soup.find('div', attrs={'class': 'watch-view-count'}).text[:-6]
    # Get the video description
    result['description'] = soup.find('p', attrs={'id': 'eow-description'}).text
    # the date when the video was published
    result['date_published'] = soup.find('strong', attrs={'class': 'watch-time-text'}).text
    # number of likes and dislikes as integers
    result['likes'] = int(soup.find('button', attrs={'title': 'I like this'}).text.replace(',', ''))
    # number of dislikes as interger
    result['dislikes'] = int(soup.find('button', attrs={'title': 'I dislike this'}).text.replace(',', ''))
    # channel details
    channel_tag = soup.find('div',  attrs={"class": "yt-user-info"}).find("a")
    # channel name
    channel_name = channel_tag.text
    # channel URL
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subs as str
    channel_subscribers = soup.find('span', attrs={'class': 'yt-subscriber-count'}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url,'subscribers': channel_subscribers}
    # return the result
    return result

#### Send YT video details
@client.command()
async def yt(ctx, *, content):
    data = get_video_info(content)
    keys = ['Title', 'Views', 'Description', 'Date Published', 'Likes', 'Dislikes',
    'Channel Name', 'Channel URL', 'Channel Subs']
    # await ctx.send(f"Title: {data['title']}")
    video_embed = discord.Embed(
        title = 'Youtube Video Details.',
        color = discord.Color.red()
        )
    code = content.split('=')
    video_embed.set_thumbnail(url=f"http://i3.ytimg.com/vi/{code[1]}/hqdefault.jpg")
    # video_embed.add_field(name='**Title:**', value=f'**{data["title"]}**', inline=False)
    video_embed.add_field(name=f"**Title**", value=f"**{data['title']}**", inline=False)
    video_embed.add_field(name=f"**Views**", value=f"**{data['views']}**", inline=True)
    video_embed.add_field(name=f"**Date Published**", value=f"**{data['date_published']}**", inline=False)
    video_embed.add_field(name=f"**Likes**", value=f"**{data['likes']}**", inline=True)
    video_embed.add_field(name=f"**Dislikes**", value=f"**{data['dislikes']}**", inline=True)
    video_embed.add_field(name=f"**Channel Name**", value=f"**{data['channel']['name']}**", inline=False)
    video_embed.add_field(name=f"**Channel Subs**", value=f"**{data['channel']['subscribers']}**", inline=True)
    video_embed.add_field(name=f"**Channel URL**", value="**[Channel Dikhao](%s)**" % data['channel']['url'], inline=False)
    await ctx.send(embed=video_embed)

#### TRANSLATION                        
@client.command()
async def translate(ctx, *, content):
    translator = Translator()
    translation = translator.translate(content)
    detection = translator.detect(content)
    spli = content.split(' ')
    link = "https://www.w3schools.com/tags/ref_language_codes.asp"

    # await ctx.send(f"Langauge: {spli[0]}")
    if(spli[0] in constants.LANGUAGES):
        lang_embed = discord.Embed(
            title = f"Langauge detected: {constants.LANGUAGES[detection.lang].upper()}",
            color = discord.Color.dark_grey(),
            )        
        translation = translator.translate(content[3:], dest=spli[0])
        detect = translator.detect(translation.text)
        lang_embed.add_field(name=f"**Original ({constants.LANGUAGES[detection.lang].title()})**", value=f"**{content[3:]}**", inline=False)
        lang_embed.add_field(name=f"**Translation ({constants.LANGUAGES[detect.lang].title()})**", value=f"**{translation.text}**", inline=False)
        lang_embed.add_field(name=f"**\n\nCountry List**", value="**[Open Country List Link](%s)**" % link, inline=False)

        await ctx.send(embed=lang_embed)

        # await ctx.send(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        # await ctx.send(f"Langauge not found mitrr.")

    elif(spli[0] not in constants.LANGUAGES):
        langauge_embed = discord.Embed(
            title = f"Langauge detected: {constants.LANGUAGES[detection.lang].upper()}",
            color = discord.Color.dark_grey(),
            description = 'Language Not Specified. Translated to **English**'
            )
        langauge_embed.add_field(name=f"**Original ({constants.LANGUAGES[detection.lang]})**", value=f"**{content}**", inline=False)
        langauge_embed.add_field(name=f"**Translation (English)**", value=f"**{translation.text}**", inline=False)
        langauge_embed.add_field(name=f"**\n\nLangauge codes**", value="**[Open codes list](%s)**" % link, inline=False)
        # langauge_embed.set_footer(text="**[Open Country List Link](%s)**" % link)
        await ctx.send(embed=langauge_embed)                    
                          
client.run(TOKEN)  


