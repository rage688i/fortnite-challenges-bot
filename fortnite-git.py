# fortnite discord bot 2018 Jeff Durbin | rage688i
import discord
import asyncio
import random

TOKEN = 'yourTokenHere'

client = discord.Client()

drop = ['Anarchy Acres', 'Dusty Divot', 'Fatal Fields', 'Flush Factory', 'Greasy Grove', 'Haunted Hills', 'Junk Junction', 'Lazy Links', 'Lonely Lodge', 'Loot Lake', 'Lucky Landing', 'Paradise Palms', 'Pleasant Park', 'Retail Row', 'Risky Reels', 'Salty Springs', 'Shifty Shafts', 'Snobby Shores', 'Tilted Towers', 'Tomato Town', 'Wailing Woods']

#weekly challenges season 4
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

# weekly challenges season 5
week1 = 'https://i.redd.it/7nauejtfui911.jpg'
week2 = 'https://i.redd.it/f3wocu0tpwa11.jpg'
week3 = 'Not available yet'
week4 = 'Not available yet'
week5 = 'Not available yet'
week6 = 'Not available yet'
week7 = 'Not available yet'
week8 = 'Not available yet'
week9 = 'Not available yet'
weekX = 'Not available yet'

# blockbuster challenges (secret battle pass star) season 4
#blockbuster1 = 'https://i.redd.it/vnqpm5ii6iv01.jpg'
#blockbuster2 = 'https://i.redd.it/oz1anpa7nnw01.jpg'
#blockbuster3 = 'https://i.redd.it/ju4ixjcy79y01.jpg'
#blockbuster4 = 'https://i.redd.it/papf24v0wdz01.jpg'
#blockbuster5 = 'https://i.redd.it/w8ec66o4h6111.jpg'
#blockbuster6 = 'https://i.redd.it/07h10o1itj211.jpg'
#blockbuster7 = 'https://i.redd.it/upa3fp5ijx311.jpg'
#blockbuster8 = 'has no battle pass star'
#blockbuster9 = 'has no battle pass star'
#blockbusterX = 'has no battle pass star'
#blockbusterall = 'https://i.redd.it/5x8udejll0611.jpg'

# road trip challenges (secret battle pass star) season 5
roadtrip1 = 'Not available yet'
roadtrip2 = 'Not available yet'
roadtrip3 = 'Not available yet'
roadtrip4 = 'Not available yet'
roadtrip5 = 'Not available yet'
roadtrip6 = 'Not available yet'
roadtrip7 = 'Not available yet'
roadtrip8 = 'Not available yet'
roadtrip9 = 'Not available yet'
roadtripX = 'Not available yet'

# chest locations
lonelylodge = 'https://i.redd.it/fyqxh1ihyzx01.jpg'
greasygrove = 'https://i.redd.it/02dd95qklnw01.jpg'
hauntedhills = 'https://i.redd.it/al5x9f1ht8v01.jpg'
wailingwoods = 'https://i.redd.it/f83lco3lcdz01.jpg'
dustydivot = 'https://i.redd.it/h5bwrvx9e6111.jpg'
lootlake = 'https://i.redd.it/5i61xfzxvj211.jpg'
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

    #chest locations by area
    #set keyword for lonely lodge chests
    if message.content.startswith('!lonelylodge'):
        msg = 'Lonely Lodge Chests' + ' ' +  lonelylodge.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for greasy grove chests
    if message.content.startswith('!greasygrove'):
        msg = 'Greasy Grove Chests' + ' ' + greasygrove.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for haunted hills chests
    if message.content.startswith('!hauntedhills'):
        msg = 'Haunted Hills Chests' + ' ' + hauntedhills.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for wailing woods chests
    if message.content.startswith('!wailingwoods'):
        msg = 'Wailing Woods Chests' + ' ' + wailingwoods.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for dusty divot chests
    if message.content.startswith('!dustydivot'):
        msg = 'Dusty Divot Chests' + ' ' + dustydivot.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for loot lake chests
    if message.content.startswith('!lootlake'):
        msg = 'Loot Lake Chests' + ' ' + lootlake.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for risky reels chests
    if message.content.startswith('!riskyreels'):
        msg = 'Risky Reels Chests' + ' ' + riskyreels.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for salty springs chests
    if message.content.startswith('!saltysprings'):
        msg = 'Salty Springs Chests' + ' ' + saltysprings.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for junk junction chests
    if message.content.startswith('!junkjunction'):
        msg = 'Junk Junction Chests' + ' ' + junkjunction.format(message)
        await client.send_message(message.channel, msg)

    #set keyword for week 1
    if message.content.startswith('!week1'):
        msg = 'Week 1 Challenges' + ' ' + week1.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 2
    if message.content.startswith('!week2'):
        msg = 'Week 2 Challenges' + ' ' + week2.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 3
    if message.content.startswith('!week3'):
        msg = 'Week 3 Challenges' + ' ' + week3.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 4
    if message.content.startswith('!week4'):
        msg = 'Week 4 Challenges' + ' ' + week4.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 5
    if message.content.startswith('!week5'):
        msg = 'Week 5 Challenges' + ' ' + week5.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for week 6
    if message.content.startswith('!week6'):
        msg = 'Week 6 Challenges' + ' ' + week6.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 7
    if message.content.startswith('!week7'):
        msg = 'Week 7 Challenges' + ' ' + week7.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 8
    if message.content.startswith('!week8'):
        msg = 'Week 8 Challenges' + ' ' + week8.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 9
    if message.content.startswith('!week9'):
        msg = 'Week 9 Challenges' + ' ' + week9.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for week 10
    if message.content.startswith('!weekX'):
        msg = 'Week 10 Challenges' + ' ' + weekX.format(message)
        await client.send_message(message.channel, msg)

    #set keyword for blockbuster 1
    if message.content.startswith('!blockbuster1'):
        msg = 'Blockbuster Week 1 Challenge' + ' ' + blockbuster1.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for blockbuster 2
    if message.content.startswith('!blockbuster2'):
        msg = 'Blockbuster Week 2 Challenge' + ' ' + blockbuster2.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for blockbuster 3
    if message.content.startswith('!blockbuster3'):
        msg = 'Blockbuster Week 3 Challenge' + ' ' + blockbuster3.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for blockbuster 4
    if message.content.startswith('!blockbuster4'):
        msg = 'Blockbuster Week 4 Challenge' + ' ' + blockbuster4.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for blockbuster 5
    if message.content.startswith('!blockbuster5'):
        msg = 'Blockbuster Week 5 Challenge' + ' ' + blockbuster5.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for blockbuster 6
    if message.content.startswith('!blockbuster6'):
        msg = 'Blockbuster Week 6 Challenge' + ' ' + blockbuster6.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for blockbuster 7
    if message.content.startswith('!blockbuster7'):
        msg = 'Blockbuster Week 7 Challenge' + ' ' + blockbuster7.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for blockbuster 8
    if message.content.startswith('!blockbuster8'):
        msg = 'Blockbuster Week 8 Challenge' + ' ' + blockbuster8.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for blockbuster 9
    if message.content.startswith('!blockbuster9'):
        msg = 'Blockbuster Week 9 Challenge' + ' ' + blockbuster9.format(message)
        await client.send_message(message.channel, msg)
     #set keyword for blockbuster 10
    if message.content.startswith('!blockbusterX'):
        msg = 'Blockbuster Week 10 Challenge' + ' ' + blockbusterX.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for blockbuster all
    if message.content.startswith('!blockbusterall'):
        msg = 'All Blockbuster Star Locations' + ' ' + blockbusterall.format(message)
        await client.send_message(message.channel, msg)

    #set keyword for roadtrip week 1
    if message.content.startswith('!roadtrip1'):
        msg = 'Roadtrip 1 Star Location' + ' ' + roadtrip1.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 2
    if message.content.startswith('!roadtrip2'):
        msg = 'Roadtrip 2 Star Location' + ' ' + roadtrip2.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 3
    if message.content.startswith('!roadtrip3'):
        msg = 'Roadtrip 3 Star Location' + ' ' + roadtrip3.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 4
    if message.content.startswith('!roadtrip4'):
        msg = 'Roadtrip 4 Star Location' + ' ' + roadtrip4.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 5
    if message.content.startswith('!roadtrip5'):
        msg = 'Roadtrip 5 Star Location' + ' ' + roadtrip5.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 6
    if message.content.startswith('!roadtrip6'):
        msg = 'Roadtrip 6 Star Location' + ' ' + roadtrip6.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 7
    if message.content.startswith('!roadtrip7'):
        msg = 'Roadtrip 7 Star Location' + ' ' + roadtrip7.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 8
    if message.content.startswith('!roadtrip8'):
        msg = 'Roadtrip 8 Star Location' + ' ' + roadtrip8.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 9
    if message.content.startswith('!roadtrip9'):
        msg = 'Roadtrip 9 Star Location' + ' ' + roadtrip9.format(message)
        await client.send_message(message.channel, msg)
    #set keyword for roadtrip week 10
    if message.content.startswith('!roadtripX'):
        msg = 'Roadtrip 10 Star Location' + ' ' + roadtripX.format(message)
        await client.send_message(message.channel, msg)
        
    # set keyword for drop locations
    if message.content.startswith('!drop'):
        location = random.choice(drop)
        msg = 'Drop @ ' + location + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    # set keyword for help
    if message.content.startswith('!fortnite'):
        msg = 'Instructions: !drop for random drop location. !week1-X to get weekly challenge. !roadtrip1-7 to get the hidden challenge for each week. !location (!hauntedhills, !greasygrove, !wailingwoods, etc) to get chest locations for each area'.format(message)
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
    print('Use !fortnite in Discord to view commands')
    print('------')
    await client.change_presence(game=discord.Game(name='!fortnite | S5:2-Anniversary'))

client.run(TOKEN)