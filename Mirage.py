import discord
from discord.ext import commands
TOKEN = 'NTEyMzI0MzYxMjQ0NTA4MTkx.Ds9cTw.QvzI7P9ebd-WTZe3AYAKokFAXCQ'


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Helping people'))
    print('Bot is ready!')




@client.command(pass_context=True)
async def giveck2(ctx, user: discord.User):
    listofid = ["205809651722354699" ,"316618976027213826" , "199127982177124352" , "420322265738117121" , "264389082811990017" , "304707344024076288" , "98150872361480192" , "194112829203152897" , "319560391267188746" , "263255468464406530" , "306440562112856065" , "117006211605331977" , "217751360253329409" , "409384065439891467" , "170603149378322432" , "224623696382394368" , "463262208470548492" , "158613353734864897" , "341302214041665536" , "242722714215907340" , "303140981845524480" , "390969866682761225" , "182974048370688000" , "390917182747443200" , "339044626147180545" , "267623243408474113" , "258621730833039360"]
    if ctx.message.author.id in listofid:
        await client.say("Check direct messages :tada:")
        embed = discord.Embed(title="**CK2 - Holy fury**",description="[CK2 Full game](https://scenegames.goodolddownloads.com/game/crusader-kings-ii) \n[Steamfix+CreamAPI](https://mega.nz/#!4wo2EKhL!g7qm-JJK8TZa177bwGv_OxxXno9p9tHOfVK_jEezyjU) \n[DLC only](https://mega.nz/#!PP5jlQTC!Uq8STfnGKK_6k5fujPwCecGcDu36kYzzjvR1WoDwBnY)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="https://i.redd.it/qf8jbw261i111.png")
        embed.set_image(url="https://i.imgur.com/F7giIci.jpg")
        embed.set_footer(text="© Mirage 2018",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        await client.send_message(user, embed=embed)
    else:
        await client.say("You don't have permission! :cry:")



@client.command(pass_context=True)
async def givehoi4(ctx, user: discord.User):
    listofid = ["205809651722354699" ,"316618976027213826" , "199127982177124352" , "420322265738117121" , "264389082811990017" , "304707344024076288" , "98150872361480192" , "194112829203152897" , "319560391267188746" , "263255468464406530" , "306440562112856065" , "117006211605331977" , "217751360253329409" , "409384065439891467" , "170603149378322432" , "224623696382394368" , "463262208470548492" , "158613353734864897" , "341302214041665536" , "242722714215907340" , "303140981845524480" , "390969866682761225" , "182974048370688000" , "390917182747443200" , "339044626147180545" , "267623243408474113" , "258621730833039360"]
    if ctx.message.author.id in listofid:
        await client.say("Check direct messages :tada:")
        embed = discord.Embed(title="**HOI4- Waking The Tiger**",description="[HOI4 Full game](https://scenegames.goodolddownloads.com/game/hearts-of-iron-iv) \n[Steamfix+CreamAPI](https://mega.nz/#!pgB2xKZC!UCYeNPY5mkC0nEzTU0YPRj0gns9lPf-i9F8gP3upd9Y) \n[DLC only part 1](https://www105.zippyshare.com/v/B8zdeyCD/file.html) \n[DLC only part 2](https://www53.zippyshare.com/v/jowAjd2G/file.html)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="https://i.redd.it/o9srxpsm8rm01.png")
        embed.set_image(url="https://forumcontent.paradoxplaza.com/public/330618/Paradox%20Pressrelease%20banner.png")
        embed.set_footer(text="© Mirage 2018",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        await client.send_message(user, embed=embed)
    else:
        await client.say("You don't have permission! :cry:")



@client.command(pass_context=True)
async def givestellaris(ctx, user: discord.User):
    listofid = ["205809651722354699" , "316618976027213826" , "199127982177124352" , "420322265738117121" , "264389082811990017" , "304707344024076288" , "98150872361480192" , "194112829203152897" , "319560391267188746" , "263255468464406530" , "306440562112856065" , "117006211605331977" , "217751360253329409" , "409384065439891467" , "170603149378322432" , "224623696382394368" , "463262208470548492" , "158613353734864897" , "341302214041665536" , "242722714215907340" , "303140981845524480" , "390969866682761225" , "182974048370688000" , "390917182747443200" , "339044626147180545" , "267623243408474113" , "258621730833039360"]
    if ctx.message.author.id in listofid:
        await client.say("Check direct messages :tada:")
        embed = discord.Embed(title="*Stellaris- Distant Stars**",description="[Stellaris Full game](https://scenegames.goodolddownloads.com/game/stellaris) \n[Steamfix](https://mega.nz/#!w4AkDIbA!FFUa_hKDfBNCGrNE6iSJaJpE4rZZk4kfPJr785XuTkI) \n[CreamAPI](https://mega.nz/#!NlpyGQJR!QkXyXFSCbejPhLM9QNkEXe-gJJX1bZA10OMeqjCAG3A)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="https://orig00.deviantart.net/b0dc/f/2016/361/3/7/stellaris___icon_by_blagoicons-dat1p2n.png")
        embed.set_image(url="https://i1.wp.com/ragequit.gr/wp-content/uploads/2018/05/Stellaris_Distant_Stars_DLC-780x353-780x405.jpg")
        embed.set_footer(text="© Mirage 2018",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        await client.send_message(user, embed=embed)
    else:
        await client.say("You don't have permission! :cry:")


@client.command(pass_context=True)
async def giveeu4(ctx, user: discord.User):
    listofid = ["205809651722354699" , "316618976027213826" , "199127982177124352" , "420322265738117121" , "264389082811990017" , "304707344024076288" , "98150872361480192" , "194112829203152897" , "319560391267188746" , "263255468464406530" , "306440562112856065" , "117006211605331977" , "217751360253329409" , "409384065439891467" , "170603149378322432" , "224623696382394368" , "463262208470548492" , "158613353734864897" , "341302214041665536" , "242722714215907340" , "303140981845524480" , "390969866682761225" , "182974048370688000" , "390917182747443200" , "339044626147180545" , "267623243408474113" , "258621730833039360"]
    if ctx.message.author.id in listofid:
        await client.say("Check direct messages :tada:")
        embed = discord.Embed(title="**EU4- Dharma**",description="[EU4 Full game](https://scenegames.goodolddownloads.com/game/europa-universalis-iv) \n[Steamfix](https://mega.nz/#!RpImTSpQ!OZMSItwcL3eq8wbuX21XZdYsOzQ5IVVtQ92VQH57fJI) \n[CreamAPI](http://www.mediafire.com/file/4s63rd20jpovj3v/CreamApi+1.27+eu4.zip) \n[DLC only](https://mega.nz/#!Y3IjDKLb!GxM24IA0gNtXryF0WX2XhALa_ZueMPs9t0X9g_19BbI)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="https://i.redd.it/dy08j5h0la111.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/470113585666850817/513715607674290176/eu4.png")
        embed.set_footer(text="© Mirage 2018",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        await client.send_message(user, embed=embed)
    else:
        await client.say("You don't have permission! :cry:")

@client.command(pass_context=True)
async def giveciv6(ctx, user: discord.User):
    listofid = ["205809651722354699" , "316618976027213826" , "199127982177124352" , "420322265738117121" , "264389082811990017" , "304707344024076288" , "98150872361480192" , "194112829203152897" , "319560391267188746" , "263255468464406530" , "306440562112856065" , "117006211605331977" , "217751360253329409" , "409384065439891467" , "170603149378322432" , "224623696382394368" , "463262208470548492" , "158613353734864897" , "341302214041665536" , "242722714215907340" , "303140981845524480" , "390969866682761225" , "182974048370688000" , "390917182747443200" , "339044626147180545" , "267623243408474113" , "258621730833039360"]
    if ctx.message.author.id in listofid:
        await client.say("Check direct messages :tada:")
        embed = discord.Embed(title="*Civilization VI**",description="[CIV6 Full game](https://scenegames.goodolddownloads.com/game/sid-meiers-civilization-vi) \n[Steamfix](https://cdn.discordapp.com/attachments/410597865329786880/446190282795384842/Sid.Meiers.Civlization.VI.Steamworks.Fix.V6-REVOLT.rar)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="https://orig00.deviantart.net/18e1/f/2017/016/b/1/civilization_vi___dock_icon_by_goldenarrow253-davmf3c.png")
        embed.set_image(url="http://steam.cryotank.net/wp-content/gallery/civilization6/Civilization-VI-10-HD.png")
        embed.set_footer(text="© Mirage 2018",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        await client.send_message(user, embed=embed)
    else:
        await client.say("You don't have permission! :cry:")

@client.command(pass_context=True)
async def givevic2(ctx, user: discord.User):
    listofid = ["205809651722354699" , "316618976027213826" , "199127982177124352" , "420322265738117121" , "264389082811990017" , "304707344024076288" , "98150872361480192" , "194112829203152897" , "319560391267188746" , "263255468464406530" , "306440562112856065" , "117006211605331977" , "217751360253329409" , "409384065439891467" , "170603149378322432" , "224623696382394368" , "463262208470548492" , "158613353734864897" , "341302214041665536" , "242722714215907340" , "303140981845524480" , "390969866682761225" , "182974048370688000" , "390917182747443200" , "339044626147180545" , "267623243408474113" , "258621730833039360"]
    if ctx.message.author.id in listofid:
        await client.say("Check direct messages :tada:")
        embed = discord.Embed(title="*Victoria 2- Hearts of Darkness**",description="[Vic2 Full game](https://thepiratebay3.org/?url=https://tpbship.org/torrent/17383304/Victoria_II_v3.04_Incl_ALL_DLC)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="https://orig00.deviantart.net/bbc1/f/2011/358/c/0/victoria_ii_icon_by_yurikenobi-d4k4f7h.png")
        embed.set_image(url="https://steamcdn-a.akamaihd.net/steam/apps/215001/header.jpg")
        embed.set_footer(text="© Mirage 2018",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        await client.send_message(user, embed=embed)
    else:
        await client.say("You don't have permission! :cry:")

@client.command(pass_context=True)
async def eu4season(ctx):
        await client.say("Check direct messages :tada:")
        await client.send_message(ctx.message.author, "Interested in playing mp Europa Universalis 4 with others , make sure to check out eu4 league weekend campaign , we play every weekend without fail")

@client.event
async def on_message(message):
    print(f"{message.channel}:  {message.author}: {message.author.name}: {message.content}")
    await client.process_commands(message)
client.run(TOKEN)
