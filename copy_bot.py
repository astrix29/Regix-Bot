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

############################ NSFW Porn ############################        
@client.command()
async def nsfw(ctx, *, content):
    x = randint(0, 311)
    y = randint(0, 228)
    z = randint(1, 216)
    bj = randint(1, 730)
    cow = randint(1, 716)
    em = discord.Embed()
    cont_split = content.split()
    # porngif.top/index.php?k=tits
    # kitty: http://porngif.top/gif/kundicky/0030.gif
    # hass: http://porngif.top/gif/zadky/0216.gif # upto 216
    # bj: http://porngif.top/gif/koureni/0001.gif # upto 730
    # cowgril: http://porngif.top/gif/na%20konicka/0000.gif # 716
    # url = f"http://porngif.top/gif/prsa/0{x:03}.gif"
    # print(url)
    # em.set_image(url=url)
    # if ctx.channel.is_nsfw():
    #     await ctx.send(embed=em)
    # else:
    #     await ctx.send(f"Try in a NSFW channel fam.", delete_after=3)

    if cont_split[0] == 'titty':
        url = f"http://porngif.top/gif/prsa/0{x:03}.gif"
        if ctx.channel.is_nsfw():
            em.set_image(url=url)
            await ctx.send(embed=em)
        else:
            await ctx.send("**Try in a NSFW channel fam.**", delete_after=5)
    
    elif cont_split[0] == 'kitty':
        url = f"http://porngif.top/gif/kundicky/0{y:03}.gif"
        if ctx.channel.is_nsfw():
            em.set_image(url=url)
            await ctx.send(embed=em)
        else:
            await ctx.send("**Try in a NSFW channel fam.**", delete_after=5)
    elif cont_split[0] == 'butty':
        url = f"http://porngif.top/gif/zadky/0{z:03}.gif"
        if ctx.channel.is_nsfw():
            em.set_image(url=url)
            await ctx.send(embed=em)
        else:
            await ctx.send("**Try in a NSFW channel fam.**", delete_after=5)
    elif cont_split[0] == 'bjob':
        url = f"http://porngif.top/gif/koureni/0{bj:03}.gif"
        if ctx.channel.is_nsfw():
            em.set_image(url=url)
            await ctx.send(embed=em)
        else:
            await ctx.send("**Try in a NSFW channel fam.**", delete_after=5)
    elif cont_split[0] == 'cow':
        url = f"http://porngif.top/gif/na%20konicka/0{cow:03}.gif"
        if ctx.channel.is_nsfw():
            em.set_image(url=url)
            await ctx.send(embed=em)
        else:
            await ctx.send("**Try in a NSFW channel fam.**", delete_after=5) 
    else:
        em.add_field(name="Nsfw Commands", value="```- titty\n- kitty\n- butty\n- bjob\n- cow```")
        em.set_footer(text="This message will be deleted in 10 seconds.")
        await ctx.send(embed=em, delete_after=10)       
############################ HELPME ############################
@client.command()
async def help(ctx):
    link = "https://www.w3schools.com/tags/ref_language_codes.asp"
    embed_help = discord.Embed(
        title = 'Help arrived!',
        description = 'These are the available Help commands:',
        color = discord.Color.blue()
    )
    embed_help.add_field(name=f'{"Translation".upper()}', value='```- t \n- t <langauge-code>\n```[Language codes link](%s)' % link,inline=True)
    embed_help.add_field(name=f'WALLPAPERS', value=f"```- wall\n- wall 1920\n- wall 720\n- wall iphone```", inline=True)
    embed_help.add_field(name='MISCS', value=f"```- doggo, avatar, clear, echo, server\n- weather <city>\n- sendm @member <message>\n- ytube yt-video-link\n- covid <country>\n- virus <URL>```", inline=False) 
    embed_help.add_field(name="NSFW (Beta) ( ͡° ͜ʖ ͡°)", value=f"``- nsfwhelp``", inline=True)
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

########################## COVID-19 Report ##########################                          
@client.command()
async def covid(ctx, *, content):
    try:
        argument = content.replace(" ", "-")
        url = f"https://www.worldometers.info/coronavirus/country/{argument}/"
        r = requests.get(url) # we donloaded the page
        soup = bs(r.content, 'html.parser')
        data = []
        
        for tags in soup.find_all(class_='maincounter-number'):
            data.append(tags.text.strip())
        
        flag = soup.find_all('img')
        # print(f"Flag Link: {flag[1]['src']}")
        flag_url = f"https://www.worldometers.info{flag[1]['src']}"
        value = randint(0, 0xffffff)
        cont = soup.find('div', class_='content-inner')
        roguh = []
        for x in cont:
            roguh.append(x)
        foot = roguh[7].text.strip()

        # Updates
        new = soup.find_all('div', class_='news_body')
        updates = []
        for li in new:
            updates.append(li.text)
        # print(updates[0])
        res = updates[0].split()
        # print(res[0], res[4])
        # try:
        covid_embed = discord.Embed(title='Covid-19  🦠', color=discord.Color(value=value))
        covid_embed.description = f"Covid-19 report for: **{argument.title()}**"
        covid_embed.add_field(name='**Coronavirus Cases**', value=f"**{data[0]}**", inline=True)
        covid_embed.add_field(name='**Deaths**', value=f"**{data[1]}**", inline=True)
        covid_embed.add_field(name='**Recovered**', value=f"**{data[2]}**", inline=False)
        covid_embed.add_field(name="**Updates**", value=f"**+{res[0]} cases\n+{res[4]} deaths**", inline=True)
        covid_embed.set_thumbnail(url=flag_url)
        covid_embed.set_footer(text=foot)
        await ctx.send(embed=covid_embed)
    except Exception:
        error_embed = discord.Embed(description="Invalid Country", color=discord.Color(value=0xf70c0c))
        await ctx.send(embed=error_embed, delete_after=3) 
                          
########################## TRANSLATION ############################                        
@client.command()
async def t(ctx, *, content):
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

########################## Check for Malicious Links ##########################                          
@client.command()
async def virus(ctx, *, content):
    # GET DOMAIN from URL: https://stackoverflow.com/questions/55862019/extract-domain-name-from-url-using-pythons-re-regex
    print("URL:", content )
    try:

        # api- d1bbf8a2f78253458ec70c75701ddf550e388a3ed6bede3be8475f476acd3049
        url = "https://www.virustotal.com/vtapi/v2/url/report"
        params = {'apikey': 'd1bbf8a2f78253458ec70c75701ddf550e388a3ed6bede3be8475f476acd3049', 'resource': content}
        response = requests.get(url, params=params).json()
        # full_url = url+'?apikey=d1bbf8a2f78253458ec70c75701ddf550e388a3ed6bede3be8475f476acd3049'
        print(params)
        virus_em = discord.Embed(title='😎 No issues found', color=discord.Color.green(), description='✅ This site looks safe!')
        if response['positives'] > 0:
            virus_em.title = f'👹 {response["positives"]} threat(s) found.'
            virus_em.color = discord.Color.red()
            virus_em.description = f'⛔ Staap Kid. This site looks sketchy!'
        # virus_em.add_field(name='')
        virus_em.add_field(name='Requests URL', value=f"{response['resource']}\n\n[Full Report](%s)" % response['permalink'])
        # virus_em.add_field(namer='Serving IP', value=f"{IP}")
        virus_em.set_footer(text=f"Requested by: {ctx.author}\n|| Scan Date: {response['scan_date']}")

        await ctx.send(embed=virus_em)
    
    except Exception:
        virus_em_err = discord.Embed(title='Invalid URL')
        virus_em_err.description = 'N/A'
        await ctx.send(embed=virus_em_err)                          
##### Calling function which takes the TOKEN and then run the bot                          
client.run(TOKEN)  


