##### ON MESSAGE FUNCION HAS PROIRITY OVER COMMAND.
import discord
from discord.ext import commands
import math, re, urllib.parse
import json, requests, calendar
from random import randint
from googletrans import Translator, constants
from bs4 import BeautifulSoup as bs

TOKEN = 'NTYxNDU4ODcyOTYzODI1NjY3.XnSbUA.NoupjGFHCivfiwzgOg8qhOo_IY8'

client = commands.Bot(command_prefix='^')

############################ On Ready ############################
@client.event
async def on_ready():
    game = discord.Game('^helpme for help')
    await client.change_presence(status=discord.Status.online,activity=game, afk=True)
    print('Bot is ready!')

############################ Waste Dm. Uesless command ############################
@client.command()
async def dm(ctx):
    await ctx.author.send('**Ye DeviPrasad ka number nahi hai, phone rakh!**')

############################ Send Anonymous Dm's To Server Members ############################    
@client.command()
async def sendm(ctx, member:discord.Member, *, content):
    channel = await member.create_dm()
    await ctx.channel.purge(limit=1)
    await channel.send(content)
    
############################ Send Dm To Server Member With Your Tag ############################
@client.command()
async def send_DM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await ctx.channel.purge(limit=1)
    await channel.send(f"**{ctx.message.author} said:** {content}")
    
############################ Ping Pong ############################
@client.command()
async def ping(ctx):
    await ctx.send('**Pong! Bot is up and running!**')

############################ Display User's Avatar ############################
@client.command()
async def avatar(ctx, member: discord.Member=None):  
    #await ctx.send("{}".format(member.avatar_url))
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed()
    #show_avatar.setfooter(text='Here\'s {}\'s Avatar. Mmmm looks sexy!'.format(member))
    show_avatar.set_image(url="{}".format(member.avatar_url))
    show_avatar.set_footer(text=f"{member}")
    await ctx.send(embed=show_avatar)

############################ Echo Command (deletes autor's message) ############################
@client.command(pass_context=True)
async def echo(ctx,*args):
    '''This will make an echo'''
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.channel.purge(limit=1) # Delete author's message and then send authors message.
    await ctx.send(output)

############################ Clear The Chat ############################
@client.command(pass_context=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    
############################ Basic Math ############################
# Add
@client.command()
async def add(ctx, a: int, b : int):
    await ctx.send(f"```python\n {a} + {b} =  {str(a+b)}\n```")
# Subtract    
@client.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} - {b} =  {str(a-b)}\n```")
# Multiply
@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} x {b} =  {str(a*b)}\n```")
# Divide
@client.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} / {b} =  {str(a/b)}\n```")
 # Remainder   
@client.command()
async def modulus(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} % {b} =  {str(a%b)}\n```")

############################ Semd Ramdom Doggo Image ############################
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
@client.command()
async def doggo(ctx):
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    allowed_extension = ['jpg', 'jpeg', 'png', 'gif']
    file_extension = ''
    doggo_embed = discord.Embed(title='A doggo for you')

    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
        doggo_embed.set_image(url=url)
    print(file_extension)
    await ctx.send(embed=doggo_embed)
    
############################ Wallpapers (Unsplash) ############################
@client.command()
async def wall(ctx, content=None):
    url = ''
    n = randint(0, 1084)
    r = requests.get('https://source.unsplash.com/random')
    wall_embed = discord.Embed(title='New Wall For You')
    url = r.url
    if content == '1920':
        url = f"https://i.picsum.photos/id/{n}/1920/1080.jpg"
        wall_embed.title = 'Wallpaper (1920x180)'
        wall_embed.set_image(url=url)
        print(url)
        await ctx.send(embed=wall_embed)

    elif content == None:
        wall_embed.set_image(url=url)
        print(url)
        await ctx.send(embed=wall_embed)
    elif content == '720':
        r = requests.get('https://source.unsplash.com/collection/1065412/720x1280')
        url = r.url
        wall_embed.title = 'Wallpaper (720x1280)'
        wall_embed.set_image(url=url)
        print(url)
        await ctx.send(embed=wall_embed)
    elif content == 'iphone':
    # https://source.unsplash.com/collection/1065412/1600x900
        r = requests.get('https://source.unsplash.com/collection/1065412/')
        url = r.url
        wall_embed.title = 'Wallpaper (iphone)'
        wall_embed.set_image(url=url)
        print(url)
        await ctx.send(embed=wall_embed)    
    else:
        print('Some error occured')
        await ctx.send('**Watch what you type nigga!**')    

############################ HELPME ############################
@client.command()
async def helpme(ctx):
    link = "https://www.w3schools.com/tags/ref_language_codes.asp"
    embed_help = discord.Embed(
        title = 'Help arrived!',
        description = 'These are the available Help commands:',
        color = discord.Color.blue()
    )
    embed_help.add_field(name=f'{"YouTube video details".upper()}', value='**Usage:** ``yt yt-video-link``',inline=False)
    embed_help.add_field(name=f'{"Translation".upper()}', value='``translate``\n``translate <langauge-code>``\n[Language codes link](%s)' % link,inline=True)
    embed_help.add_field(name=f'WALLPAPERS', value=f"``wall``\n``wall 1920``\n``wall 720``\n``wall iphone``", inline=True)
    embed_help.add_field(name='MISCS', value=f"``doggo``,``avatar``, ``clear``, ``echo``, ``add subtract divide multiply modulus``, \n``weather <city>``\n``sendm @member <message>``", inline=False) 
    await ctx.send(embed=embed_help)

############################ Server info ############################    
@client.command()
async def server(ctx):
    guild = ctx.guild
    date = guild.created_at
    # guild = ctx.guild
    # ser = client.get_guild(ctx.guild.id)
    # await ctx.send(str(ctx.guild.icon_url)) #### Returns Server's icon url
    online = 0
    idle = 0
    offline = 0

    for m in guild.members:
        if str(m.status) == "online":
            online += 1
        if str(m.status) == "offline":
            offline += 1
        else:
            idle += 1

    server_embed = discord.Embed(title=f'{guild.name}')
    # server_embed.add_field(name="**Server Name**", value=f"{guild.name}", inline=False)
    server_embed.add_field(name="**Owner's Name**", value=f"{guild.owner}", inline=False)
    server_embed.add_field(name="**Total Members**", value=f"{guild.member_count}", inline=False)
    server_embed.add_field(name='**Members Status**', value=f"🟢 ``Online: {online}.``\n⚪ ``Offline: {offline}.``\n🟡🔴``Idle/dnd: {idle}.\n``")
    server_embed.add_field(name="**Server Created On**", value=f"{date.day} {calendar.month_name[date.month]} {date.year} {date.hour}:{date.minute}", inline=False)
    server_embed.set_thumbnail(url=f"{str(guild.icon_url)}")
    server_embed.add_field(name="**Server's Description**", value=f"{guild.description}", inline=False)
    server_embed.add_field(name='**Server Region**', value=f"{guild.region}", inline=True)
    server_embed.add_field(name="**Premium Tier**", value=f"{guild.premium_tier}", inline=True)
    server_embed.add_field(name="**Number of Premium Members**", value=f"{guild.premium_subscription_count}", inline=True)
    server_embed.add_field(name='**Server\'s Icon Link**', value="**[Link](%s)**" % str(guild.icon_url),inline=False)
    await ctx.send(embed=server_embed)
    
############################ Google Maps ############################
@client.command()
async def whereis(ctx, *, content):
    cont = "https://www.google.com/maps/place/{}".format(content)
    icon = "https://colorlib.com/wp/wp-content/uploads/sites/2/google-maps-wordpress-plugins.png"
    try:
        await ctx.send(embed=discord.Embed(title="Google Maps",description="**[Yaha dekho bhai...](%s)**" % cont, color=discord.Color.darker_grey(), inline=True).set_thumbnail(url=icon))
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send("Usage: !whereis <some_location>")
  
############################ Astonaut's Names ############################
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

############################ YouTube Video Details ############################
# This function will return YT video's details in a Dictionary.
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
    video_embed = discord.Embed(
        title = 'Youtube Video Details.',
        color = discord.Color.red()
        )
    code = content.split('=')
    # Add values from the response into the embed.
    video_embed.set_thumbnail(url=f"http://i3.ytimg.com/vi/{code[1]}/hqdefault.jpg")
    video_embed.add_field(name=f"**Title**", value=f"**{data['title']}**", inline=False)
    video_embed.add_field(name=f"**Views**", value=f"**{data['views']}**", inline=True)
    video_embed.add_field(name=f"**Date Published**", value=f"**{data['date_published']}**", inline=False)
    video_embed.add_field(name=f"**Likes**", value=f"**{data['likes']}**", inline=True)
    video_embed.add_field(name=f"**Dislikes**", value=f"**{data['dislikes']}**", inline=True)
    video_embed.add_field(name=f"**Channel Name**", value=f"**{data['channel']['name']}**", inline=False)
    video_embed.add_field(name=f"**Channel Subs**", value=f"**{data['channel']['subscribers']}**", inline=True)
    video_embed.add_field(name=f"**Channel URL**", value="**[Channel Dikhao](%s)**" % data['channel']['url'], inline=False)
    await ctx.send(embed=video_embed)

############################ WEATHER BY OPEN WEATHER. MAKE SURE YOU GET AN "API" KEY. ############################
async def weather(ctx, *, content):
    # openweather's api key
    api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = urllib.parse.quote(content)
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    x = response.json()
    # Parse only the important information from the response.
    if x['cod'] != '404':
        y = x["main"]
        icon = x['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        country_code = x['sys']['country']
        current_temp = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x['weather']
        weather_description = z[0]['description']
        temp_cel = math.ceil((current_temp-273.15))
    # Creating the embed.
        weather_embed = discord.Embed(title=f"{weather_description.title()}",
            color = discord.Color(value=0x42f5ef))
        weather_embed.add_field(name=f"🌡️ Temperature", value=f"{temp_cel} ℃", inline=True)
        weather_embed.add_field(name="💧 Humidity", value=f"{current_humidity}%", inline=True)
        weather_embed.add_field(name='🌬️ Pressure', value=f"{current_pressure} hPa", inline=False)
        # weather_embed.add_field(name="Description", value=f"{icon_url} {weather_description.title()} ", inline=False)
        weather_embed.set_thumbnail(url=icon_url)
        weather_embed.set_footer(text=f"Weather Report for {content.upper()} ({country_code})")
        await ctx.send(embed=weather_embed)
    else:
        await ctx.send("**City Not Found**")                          
                          
########################## TRANSLATION ############################                        
@client.command()
async def translate(ctx, *, content):
    translator = Translator()
    translation = translator.translate(content)
    detection = translator.detect(content)
    spli = content.split(' ')
    link = "https://www.w3schools.com/tags/ref_language_codes.asp"
    
    # Check if language code is valid and respond accordingly.
    if(spli[0] in constants.LANGUAGES):
        lang_embed = discord.Embed(
            title = f"Langauge detected: **{constants.LANGUAGES[detection.lang].title()}**",
            color = discord.Color.dark_grey(),
            )        
        translation = translator.translate(content[3:], dest=spli[0])
        detect = translator.detect(translation.text)
        lang_embed.add_field(name=f"**Original ({constants.LANGUAGES[detection.lang].title()})**", value=f"**{content[3:]}**", inline=False)
        lang_embed.add_field(name=f"**Translation ({constants.LANGUAGES[detect.lang].title()})**", value=f"**{translation.text}**", inline=False)
        lang_embed.add_field(name=f"**\n\nCountry List**", value="[Language codes link](%s)" % link, inline=False)
        await ctx.send(embed=lang_embed)
                          
    # If no language code if provided then simply translate to english.
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

##### Calling function which takes the TOKEN and then run the bot                          
client.run(TOKEN)  


