from discord.ext import commands
from discord.utils import get
import discord


TOKEN = 'YOUR TOKEN HERE'

bot = commands.Bot(command_prefix="(", intents=discord.Intents.all())

@bot.event
async def on_ready():
	print("The bot has successfully started.")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(943602154428571708)
    await channel.send(f"{member.mention} ({member}) joined the server!\nhttps://tenor.com/view/snsdmongus-dog-sideye-gif-21272558")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(943602154428571708)
    await channel.send(f"{member.mention} ({member}) left the server!\nhttps://media.discordapp.net/attachments/1096276589743972386/1096665886779261068/attachment.gif")

@bot.command()
async def hello(ctx):
    await ctx.send("Hiiiii haiii haiiii :3")

@bot.command()
@commands.has_permissions(administrator=True)
async def HELP(ctx):
    await ctx.send("Prefix: '('\nUser commands:\nHELP\nhello\nAdmin commands:\npit (@user/ID)\nunpit (@user/ID)\nswagify (@user/ID)\nunswagify (@user/ID)")

@bot.command()
@commands.has_permissions(administrator=True)
async def pit(ctx, user: discord.Member):
    guild = ctx.guild
    admin_r = ctx.guild.get_role(938787942657327114)
    mod_r = ctx.guild.get_role(977248936148500550)
    owner_r = ctx.guild.get_role(938732039207809025)
    bot_r = ctx.guild.get_role(938795313815240734)
    bot2_r = ctx.guild.get_role(998594848582025269)
    user_roles = user.roles
    if any(role in user_roles for role in [admin_r, mod_r, owner_r, bot_r, bot2_r]):
        await ctx.send("User can not be pitted")
        pass
    else:
        role = ctx.guild.get_role(1057342828205846538)
        await user.edit(roles=[role])
        await ctx.send("Pitted.\nhttps://media.discordapp.net/attachments/1091036967199834112/1129035100915511376/attachment.gif")

    
@bot.command()
@commands.has_permissions(administrator=True)
async def unpit(ctx, user: discord.Member):
    guild = ctx.guild
    member_r = ctx.guild.get_role(938804320026099742)
    user_role = user.roles
    if any(role in user_role for role in [member_r]):
        await ctx.send("This user is not in the pit. Or maybe something went terribly wrong :smile: ")
        pass
    else:
        role = ctx.guild.get_role(938804320026099742)
        await user.edit(roles=[role])
        await ctx.send(f"{user}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif")

@bot.command()
@commands.has_permissions(administrator=True)
async def swagify(ctx, user: discord.Member):
    guild = ctx.guild
    role = ctx.guild.get_role(1003732468370776125)
    await user.add_roles(role)
    await ctx.send(f"{user} is now a swag baller!!!!!!!!!")

@bot.command()
@commands.has_permissions(administrator=True)
async def unswagify(ctx, user: discord.Member):
    guild = ctx.guild
    role = ctx.guild.get_role(1003732468370776125)
    await user.remove_roles(role)
    await ctx.send(f"{user} has gotten their swag priveleges revoked.")


bot.run(TOKEN)
