# fortnite discord bot 2018 Jeff Durbin | rage688i
import discord
import asyncio
import random

TOKEN = 'YOURTOKENHERE'

client = discord.Client()

# map locations
drop = ['Anarchy Acres', 'Dusty Divot', 'Fatal Fields', 'Flush Factory', 'Greasy Grove', 'Haunted Hills', 'Junk Junction', 'Lazy Links', 'Lonely Lodge', 'Leaky Lake', 'Lucky Landing', 'Paradise Palms', 'Pleasant Park', 'Retail Row', 'Risky Reels', 'Salty Springs', 'Shifty Shafts', 'Snobby Shores', 'Tilted Towers', 'Tomato Temple', 'Wailing Woods']

# weekly challenges season 4 (depreciated)
#week1 = 'https://i.redd.it/o56opse8v8v01.jpg'
#week2 = 'https://i.redd.it/m3huulqtlnw01.jpg'
#week3 = 'https://i.redd.it/az5bi82hzzx01.jpg'
#week4 = 'https://i.redd.it/6t97smvccdz01.jpg'
#week5 = 'https://i.redd.it/icygqd05g6111.jpg'
#week6 = 'https://i.redd.it/w9u46ctfij211.jpg'
#week7 = 'https://i.redd.it/kmzsks3uix311.jpg'
#week8 = 'https://i.redd.it/ijpye4dq1c511.jpg'
#week9 = 'https://i.imgur.com/B06mKzG.jpg'
#weekX = 'https://i.imgur.com/3iR0bGF.jpg'

# weekly challenges season 5 (depreciated)
#week1 = 'https://i.redd.it/7nauejtfui911.jpg'
#week2 = 'https://i.redd.it/f3wocu0tpwa11.jpg'
#week3 = 'https://i.redd.it/xihzmw4brac11.jpg'
#week4 = 'https://i.redd.it/h6oj6uuaood11.jpg'
#week5 = 'https://i.redd.it/uzoqem8om2f11.jpg'
#week6 = 'https://i.redd.it/fahipbn3zgg11.jpg'
#week7 = 'https://i.redd.it/73w8ni2rl1i11.jpg'
#week8 = 'https://i.redd.it/yhbim1z3d8j11.jpg'
#week9 = 'https://i.redd.it/bh9jeh74ltk11.jpg'
#weekX = 'https://i.redd.it/8kru4hjud0m11.jpg'

# weekly challenges season 6
week1 = 'https://i.redd.it/ocqvrzkraso11.jpg'
week2 = 'https://i.redd.it/nhquyo2aa6q11.jpg'
week3 = 'https://i.redd.it/23lj1ypejkr11.jpg'
week4 = 'https://i.redd.it/a5utgt5h7ys11.jpg'
week5 = 'https://i.redd.it/44rm8cgyhcu11.jpg'
week6 = 'https://i.redd.it/8n8z4e7mw5u11.jpg' #haloween event (Fortnitemares)
week7 = 'https://i.redd.it/vr11ih7ne4x11.jpg'
week8 = 'https://i.redd.it/o1t7tr619iy11.jpg'
week9 = ''
weekX = ''

# chest locations
lonelylodge = 'https://i.redd.it/fyqxh1ihyzx01.jpg'
greasygrove = 'https://i.redd.it/02dd95qklnw01.jpg'
hauntedhills = 'https://i.redd.it/al5x9f1ht8v01.jpg'
wailingwoods = 'https://i.redd.it/f83lco3lcdz01.jpg'
dustydivot = 'https://i.redd.it/h5bwrvx9e6111.jpg'
riskyreels = 'https://i.redd.it/jy4s3b9cax311.jpg'
saltysprings = 'https://i.redd.it/q8nspjdh0c511.jpg'
#moistymire = 'https://i.redd.it/rg26c3isgp611.jpg'
junkjunction = 'https://i.imgur.com/Iezlvzz.jpg'

# shopping cart locations
shoppingcart = 'https://i.redd.it/z91qjl9rf2111.jpg'

# rift locations
rifts = 'https://i.redd.it/xtt9n85n16a11.jpg'

# fortnite bday
bday = 'https://i.redd.it/d09zspssrvb11.jpg'

@client.event
@asyncio.coroutine
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # chest locations by area
    # set keyword for lonely lodge chests
    if message.content.startswith('!lonelylodge'):
        msg = 'Lonely Lodge Chests' + ' ' +  lonelylodge.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for greasy grove chests
    if message.content.startswith('!greasygrove'):
        msg = 'Greasy Grove Chests' + ' ' + greasygrove.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for haunted hills chests
    if message.content.startswith('!hauntedhills'):
        msg = 'Haunted Hills Chests' + ' ' + hauntedhills.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for wailing woods chests
    if message.content.startswith('!wailingwoods'):
        msg = 'Wailing Woods Chests' + ' ' + wailingwoods.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for dusty divot chests
    if message.content.startswith('!dustydivot'):
        msg = 'Dusty Divot Chests' + ' ' + dustydivot.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for risky reels chests
    if message.content.startswith('!riskyreels'):
        msg = 'Risky Reels Chests' + ' ' + riskyreels.format(message)
        await client.send_message(message.channel, msg)
     # set keyword for salty springs chests
    if message.content.startswith('!saltysprings'):
        msg = 'Salty Springs Chests' + ' ' + saltysprings.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for junk junction chests
    if message.content.startswith('!junkjunction'):
        msg = 'Junk Junction Chests' + ' ' + junkjunction.format(message)
        await client.send_message(message.channel, msg)

    # set keyword for week 1
    if message.content.startswith('!week1'):
        msg = 'Week 1 Challenges' + ' ' + week1.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 2
    if message.content.startswith('!week2'):
        msg = 'Week 2 Challenges' + ' ' + week2.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 3
    if message.content.startswith('!week3'):
        msg = 'Week 3 Challenges' + ' ' + week3.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 4
    if message.content.startswith('!week4'):
        msg = 'Week 4 Challenges' + ' ' + week4.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 5
    if message.content.startswith('!week5'):
        msg = 'Week 5 Challenges' + ' ' + week5.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 6
    if message.content.startswith('!week6'):
        msg = 'Week 6 Challenges' + ' ' + week6.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 7
    if message.content.startswith('!week7'):
        msg = 'Week 7 Challenges' + ' ' + week7.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 8
    if message.content.startswith('!week8'):
        msg = 'Week 8 Challenges' + ' ' + week8.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 9
    if message.content.startswith('!week9'):
        msg = 'Week 9 Challenges' + ' ' + week9.format(message)
        await client.send_message(message.channel, msg)
    # set keyword for week 10
    if message.content.startswith('!weekX'):
        msg = 'Week 10 Challenges' + ' ' + weekX.format(message)
        await client.send_message(message.channel, msg)

    # set keyword for drop locations
    if message.content.startswith('!drop'):
        location = random.choice(drop)
        msg = 'Drop @ ' + location + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    # set keyword for help
    if message.content.startswith('!fortnite'):
        msg = 'How to use: !drop for random drop location. !week1-X to get weekly challenge. !location (!hauntedhills, !greasygrove, etc) to get chest locations for each area'.format(message)
        await client.send_message(message.channel, msg)

    # set keyword for all shopping cart locations
    if message.content.startswith('!shoppingcart'):
        msg = shoppingcart.format(message)
        await client.send_message(message.channel, msg)

    # set keyword for all rift locations
    if message.content.startswith('!rifts'):
        msg = rifts.format(message)
        await client.send_message(message.channel, msg)
    
    # set keyword for fortnite bday content
    if message.content.startswith('!bday'):
        msg = 'Fortnite Year 1 Celebration Challenges' + ' ' + bday.format(message)
        await client.send_message(message.channel, msg)

@client.event
@asyncio.coroutine
async def on_ready():
    print('Logged in as')
    print('Username: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('Status: Active')
    print('Fortnite Season 6 Week 8')
    print('Use !fortnite in Discord to view commands')
    print('------')
    await client.change_presence(game=discord.Game(name='!fortnite | S6:8'))

client.run(TOKEN)
