# ON MESSAGE FUNCION HAS PROIRITY OVER COMMAND.
import discord
from discord.ext import commands
import math, re, urllib.parse, os
import json, requests, calendar
from random import randint
from googletrans import Translator, constants
from bs4 import BeautifulSoup as bs

TOKEN = os.environ.get('DISCORD_TOKEN')


client = commands.Bot(command_prefix='^')
client.remove_command("help")

@client.event
async def on_ready():
    game = discord.Game(f'^help || Serving {client.get_guild(383421855056527372)}')
    await client.change_presence(status=discord.Status.idle ,activity=game)
    print('Bot is ready!\n\nServer\'s info\n')
    print(f"serving in {len(client.guilds)} servers")
    # print(f"Serving: {client.get_guild(*************)}")
    for server in client.guilds:
        print(f"Server name: {server.name}; Members: {server.member_count}; ID: {server.id}")


############################### DM ###############################
@client.command()
async def dm(ctx):
    await ctx.author.send('**Ye DeviPrasad ka number nahi hai, phone rakh!**')

@client.command()
async def send_DM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await ctx.channel.purge(limit=1)
    await channel.send(f"**{ctx.message.author} said:** {content}")

@client.command()
async def sendm(ctx, member:discord.Member, *, content):
    channel = await member.create_dm()
    await ctx.author.send(f"```Message sent to {member}: \n{content}```")
    await ctx.channel.purge(limit=1)
    await channel.send(content)

############################### AVATAR ###############################

@client.command(aliases=['av'])
async def avatar(ctx, member: discord.Member=None):  
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed(description="[Avatar URL](%s)" % member.avatar_url)
    show_avatar.set_image(url="{}".format(member.avatar_url))
    show_avatar.set_footer(text=f'{member}')
    await ctx.send(embed=show_avatar)

############################### ECHO ###############################

@client.command(pass_context=True)
async def echo(ctx,*, content):
	await ctx.message.delete()
	await ctx.send(content)

############################### DM ###############################

@client.command(pass_context=True)
async def clear(ctx, amount=2):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("```You can't do that sar```", delete_after=3)

############################### MatheMaticS ###############################

@client.command()
async def add(ctx, a: int, b : int):
    await ctx.send(f"```python\n {a} + {b} =  {str(a+b)}\n```")  

# Subtract
@client.command()
async def sub(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} - {b} =  {str(a-b)}\n```")

# Multiply
@client.command()
async def mult(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} x {b} =  {str(a*b)}\n```")

# Divide
@client.command()
async def div(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} / {b} =  {str(a/b)}\n```")

 # Remainder   
@client.command()
async def mod(ctx, a: int, b: int):
    await ctx.send(f"```python\n {a} % {b} =  {str(a%b)}\n```")

############################### DOGGO ###############################

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
    doggo_embed = discord.Embed()

    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
        doggo_embed.set_image(url=url)
    print(file_extension)
    await ctx.send(embed=doggo_embed)    

############################### CATTO ###############################

@client.command()
async def catto(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    catto_em = discord.Embed()
    catto_em.set_image(url=f'{r[0]["url"]}')
    await ctx.send(embed=catto_em)

############################### RIP ###############################

@client.command()
async def rip(ctx):
    em = discord.Embed()
    url = 'https://i.imgur.com/w3duR07.png'
    em.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=em)

############################### WALLPAPERS ###############################

@client.command(aliases=['WALLP', 'Wallp'])
async def wallp(ctx):
    url = ''
    r = requests.get('https://source.unsplash.com/collection/1065412/720x1280')
    url = r.url
    wall_embed = discord.Embed()
    wall_embed.set_image(url=url)
    print(f'{ctx.author} asked for wallp')
    await ctx.send(embed=wall_embed)

@client.command()
async def wallip(ctx):
    url = ''
    r = requests.get('https://source.unsplash.com/collection/1065412/')
    url = r.url
    wall_embed = discord.Embed()
    wall_embed.set_image(url=url)
    print(f'{ctx.author} asked for wallip')
    await ctx.send(embed=wall_embed)
       
############################### NSWF STUFF ###############################

@client.command(aliases=['n'])
async def nsfw(ctx, *, content):
    x = randint(0, 311)
    y = randint(0, 228)
    z = randint(1, 216)
    bj = randint(1, 730)
    cow = randint(1, 716)
    em = discord.Embed()
    cont_split = content.split()
    print(f'{ctx.author} asked for {content}')

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
    elif cont_split[0] == 'butt':
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
        await ctx.message.delete()

############################### NSWF HELP ###############################

@client.command(aliases=['nh'])
async def nsfwhelp(ctx):
    value = randint(0, 0xffffff)
    nsfw_help = discord.Embed(color = discord.Color(value=value))
    if ctx.channel.is_nsfw():
        nsfw_help.title = "( ͡° ͜ʖ ͡°)"
        nsfw_help.description = '^nsfw <option>'
        nsfw_help.add_field(name="NSFW Commands", value=f"```- titty\n- kitty\n- butt\n- bjob\n- cow```", inline=True)
        await ctx.send(embed=nsfw_help)
    else:
        nsfw_help.title = f"This is not an NSFW channel sir."
        await ctx.send(embed=nsfw_help, delete_after=5)
        await ctx.message.delete()

############################### SERVER INFO ###############################

@client.command()
async def server(ctx):
    guild = ctx.guild
    date = guild.created_at
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
    server_embed.add_field(name="**Owner's Name**", value=f"{guild.owner}", inline=False)
    server_embed.add_field(name="**Total Members**", value=f"{guild.member_count}", inline=True)
    server_embed.add_field(name="**Server Created On**", value=f"{date.day} {calendar.month_name[date.month]} {date.year} {date.hour}:{date.minute}", inline=True)
    server_embed.set_thumbnail(url=f"{str(guild.icon_url)}")
    server_embed.add_field(name='**Server Region**', value=f"{guild.region}", inline=False)
    server_embed.add_field(name='**Server\'s Icon Link**', value="**[Link](%s)**" % str(guild.icon_url),inline=False)
    await ctx.send(embed=server_embed)

############################### BOT HELP COMMAND ###############################

@client.command()
async def help(ctx):
    embed_help = discord.Embed(
        title = 'Help arrived!',
        description = 'These are the available Help commands:',
        color = discord.Color.blue()
    )
    embed_help.add_field(name=f'{"⫸  **UTILITY**".upper()}', value='»» **``avatar``** • **``clear ``** • **``weather``** • **``covid``** • **``translate``**\n»»  **``iplookup``**',inline=False)
    embed_help.add_field(name=f'⫸  **WALLPAPERS**', value=f"»» **``wall``** • **``walld``** • **``wallp``** • **``wallip``**", inline=False)
    embed_help.add_field(name='⫸  **MISCS**', value=f"»» **``doggo``** • **``catto``** • **``echo``** • **``server``** • **``ytvid``** • **``url``**\n»»  **``sendm @mention message``**", inline=False) 
    embed_help.add_field(name="⫸  **NSFW (Beta)** ( ͡° ͜ʖ ͡°)", value=f"»» **``nsfwhelp``**", inline=False)
    await ctx.send(embed=embed_help)

############################### LATENCY (INCOMPLETE) ###############################

@client.command()
async def ping(ctx):
    value = randint(0, 0xffffff)
    lat_em = discord.Embed(title='Pong!', color=discord.Color(value=value))
    lat_em.add_field(name='**``• Discord WebSocket Latency``**', value=f'**``⇢ {client.latency:.3f} ms``**')
    lat_em.set_footer(text='• Latency b/w Baburao and the discord servers.')
    await ctx.send(embed=lat_em)

############################### ASTRONAUTS ###############################

@client.command()
async def astroiss(ctx):
    response = requests.get("http://api.open-notify.org/astros.json")
    json.dumps(response.json(), sort_keys=True, indent=4)
    astronauts = response.json()["people"]
    astro_names = []
    for x in astronauts:
        names = x["name"]
        astro_names.append(names)
    astroiss_embed = discord.Embed(
        title = 'Names of Astronauts on the ISS',
        description = f'There are ``{len(astro_names)} astronaut[s]`` in space atm ',
        color = discord.Color.blue()
    )
    astroiss_embed.set_thumbnail(url="https://economictimes.indiatimes.com/thumb/msid-68707249,width-1200,height-900,resizemode-4,imgsize-762936/iss.jpg?from=mdr")
    for idx, item in enumerate(astro_names, 1):
        astroiss_embed.add_field(name="‎‎‎‎‎ ‎", value=f"**{idx}**. ``{item}``",inline=False)
    await ctx.send(embed=astroiss_embed)

############################### YOUTUBE VIDEO DETAILS ###############################

def get_video_info(url):
    request = requests.get(url)
    soup = bs(request.content, 'html.parser')
    result = {}
    result['title'] = soup.find('span', class_='watch-title').text.strip()
    result['views'] = soup.find('div', attrs={'class': 'watch-view-count'}).text[:-6]
    result['description'] = soup.find('p', attrs={'id': 'eow-description'}).text
    result['date_published'] = soup.find('strong', attrs={'class': 'watch-time-text'}).text
    result['likes'] = int(soup.find('button', attrs={'title': 'I like this'}).text.replace(',', ''))
    result['dislikes'] = int(soup.find('button', attrs={'title': 'I dislike this'}).text.replace(',', ''))
    channel_tag = soup.find('div',  attrs={"class": "yt-user-info"}).find("a")
    channel_name = channel_tag.text
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    channel_subscribers = soup.find('span', attrs={'class': 'yt-subscriber-count'}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url,'subscribers': channel_subscribers}
    return result
  
@client.command()
async def ytvid(ctx, *, content):
    data = get_video_info(content)
    video_embed = discord.Embed(
        title = 'Youtube Video Details.',
        color = discord.Color.red()
        )
    code = content.split('=')
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

############################### TRANSLATION ###############################

@client.command(aliases=['tr'])
async def translate(ctx, *, content):
    translator = Translator()
    translation = translator.translate(content)
    detection = translator.detect(content)
    spli = content.split(' ')
    link = "https://www.w3schools.com/tags/ref_language_codes.asp"

    if(spli[0] in constants.LANGUAGES):
        lang_embed = discord.Embed(
            title = f"Langauge detected: **{constants.LANGUAGES[detection.lang].title()}**",
            color = discord.Color.dark_grey(),
            )        
        translation = translator.translate(content[3:], dest=spli[0])
        detect = translator.detect(translation.text)
        lang_embed.add_field(name=f"❖ **Original ({constants.LANGUAGES[detection.lang].title()})**", value=f"» **{content[3:]}**", inline=False)
        lang_embed.add_field(name=f"❖ **Translation ({constants.LANGUAGES[detect.lang].title()})**", value=f"» **{translation.text}**", inline=False)
        lang_embed.add_field(name=f"**\n\nLanguage codes**", value="[Open codes link](%s)" % link, inline=False)
        print(f'{ctx.author} translate {content} to {spli[0]}')
        await ctx.send(embed=lang_embed)

    elif(spli[0] not in constants.LANGUAGES):
        langauge_embed = discord.Embed(
            title = f"Langauge detected: {constants.LANGUAGES[detection.lang].title()}",
            color = discord.Color.dark_grey(),
            description = '∅ Language Not Specified. Translated to **English**'
            )
        langauge_embed.add_field(name=f"❖ **Original ({constants.LANGUAGES[detection.lang].title()})**", value=f"» **{content}**", inline=False)
        langauge_embed.add_field(name=f"❖ **Translation (English)**", value=f"» **{translation.text}**", inline=False)
        langauge_embed.add_field(name=f"**\n\nLangauge codes**", value="**[Open codes list](%s)**" % link, inline=False)
        print(f'{ctx.author} translate {content} to English')
        await ctx.send(embed=langauge_embed)

############################### WEATHER ###############################

@client.command(aliases=['wt'])
async def weather(ctx, *, content):
    api_key = os.environ.get('WEATHER_API')
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = urllib.parse.quote(content)
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    x = response.json()


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

        weather_embed = discord.Embed(title=f"{weather_description.title()}",
            color = discord.Color(value=0x42f5ef))
        weather_embed.add_field(name=f"🌡️ Temperature", value=f"{temp_cel} ℃", inline=True)
        weather_embed.add_field(name="💧 Humidity", value=f"{current_humidity}%", inline=True)
        weather_embed.add_field(name='🌬️ Pressure', value=f"{current_pressure} hPa", inline=False)
        weather_embed.set_thumbnail(url=icon_url)
        weather_embed.set_footer(text=f"Weather Report for {content.upper()} ({country_code})")
        print(f'{ctx.author} asked for weather of {city_name}')
        await ctx.send(embed=weather_embed)
    else:
        await ctx.send("**City Not Found**")

############################### COVID-19 ###############################

@client.command()
async def covid(ctx, *, content):
    try:
        argument = content.replace(" ", "-")
        url = f"https://www.worldometers.info/coronavirus/country/{argument}/"
        r = requests.get(url) # we download the page
        soup = bs(r.content, 'html.parser')
        data = []
        
        for tags in soup.find_all(class_='maincounter-number'):
            data.append(tags.text.strip())
        
        flag = soup.find_all('img')
        flag_url = f"https://www.worldometers.info{flag[1]['src']}"
        value = randint(0, 0xffffff)
        # Updates
        new = soup.find_all('div', class_='news_body')
        updates = []
        for li in new:
            updates.append(li.text)
        # print(updates[0])
        res = updates[0].split()
        if "deaths" in res or "death" in res:
            res[4] = res[4]
        else:
            res[4] = 0
        # print(res[0], res[4])
        covid_embed = discord.Embed(title='Covid-19  🦠', color=discord.Color(value=value))
        covid_embed.description = f"Covid-19 report for: {argument.title()}"
        covid_embed.add_field(name='Total Cases', value=f"**``{data[0]}``**", inline=True)
        covid_embed.add_field(name='Total Deaths', value=f"**``{data[1]}``**", inline=True)
        covid_embed.add_field(name='Recovered', value=f"**``{data[2]}``**", inline=False)
        covid_embed.add_field(name=f"Updates", value=f"**``+{res[0]} new cases\n+{res[4]} new deaths``**", inline=True)
        covid_embed.set_thumbnail(url=flag_url)
        covid_embed.set_footer(text=f"Last updated: {soup.find('div', class_='news_date').text.strip()}")
        await ctx.send(embed=covid_embed)
    except Exception:
        error_embed = discord.Embed(description="Invalid Country", color=discord.Color(value=0xf70c0c))
        await ctx.send(embed=error_embed)

############################### VIRUSTOTAL ###############################

@client.command()
async def url(ctx, *, content):
    print("URL:", content )
    try:
        url = "https://www.virustotal.com/vtapi/v2/url/report"
        params = {'apikey': f'{os.environ.get("VT_API")}', 'resource': content}
        response = requests.get(url, params=params).json()
        print(params)
        virus_em = discord.Embed(title='(>‿◠)✌ No issues found', color=discord.Color.green(), description='✅ This site looks safe!')
        if response['positives'] > 0:
            virus_em.title = f'👹 {response["positives"]} threat(s) found.'
            virus_em.color = discord.Color.red()
            virus_em.description = f'⛔  Staap Kid. This site looks sketchy!'
        virus_em.add_field(name=f'**``Requests URL``**', value=f"{response['resource']}\n\n[Full Report](%s)" % response['permalink'])
        virus_em.set_footer(text=f"Requested by: {ctx.author}\n")
        await ctx.send(embed=virus_em)
    
    except Exception:
        virus_em_err = discord.Embed(title='Invalid URL')
        virus_em_err.description = 'N/A'
        await ctx.send(embed=virus_em_err)
# GET DOMAIN from URL: https://stackoverflow.com/questions/55862019/extract-domain-name-from-url-using-pythons-re-regex

############################### IP-LOOKUP ##############################

@client.command(aliases=['ip'])
async def iplookup(ctx, *, content):
    ip_api_key = os.environ.get('IP_API')
    url = 'http://api.ipapi.com/' + str(content)
    payload = {'access_key': ip_api_key, 'format': 1}
    response = requests.get(url, params=payload).json()
    value = randint(0, 0xffffff)
    print(url)
    ip_embed = discord.Embed(title=f'{content}', description=f"Continent: **``{response['continent_name']} ({response['continent_code']})``**", color=discord.Color(value=value))
    ip_embed.add_field(name='**Country**', value=f"{response['location']['country_flag_emoji']} • **``{response['country_name']} ({response['country_code']})``**", inline=False)
    ip_embed.add_field(name='**Region**', value=f"**``{response['region_name']}``**", inline=True)
    ip_embed.add_field(name='**City**', value=f"**``{response['city']}``**", inline=False)
    ip_embed.add_field(name='**Address Type**', value=f"**``{response['type']}``**")
    print(f'{ctx.author} searched for ip {content}')
    await ctx.send(embed=ip_embed)

############################### HANDLING ERRORS ###############################

@covid.error
async def covid_error(ctx, error):
    await ctx.send("**``Include Country Name Plox.``**")

@translate.error
async def translate_error(ctx, error):
    link = "https://www.w3schools.com/tags/ref_language_codes.asp"
    tr_er = discord.Embed(description='Alias: **tr**')
    tr_er.add_field(name='Usage', value=f'translate ``code`` ``query``\n\n|| [Language Code Link](%s)' % link)
    tr_er.set_footer(text="NOTE: Code is optional")
    await ctx.send(embed=tr_er)

@catto.error
async def catto_error(ctx, error):
    await ctx.send(str(error))

@weather.error
async def weather_error(ctx, error):
    await ctx.send("**``Include City Name Plox.``**")

@ytvid.error
async def ytvid_error(ctx, error):
    await ctx.send(str(error))

############################### RUN CLIENT ###############################

client.run(TOKEN)  


