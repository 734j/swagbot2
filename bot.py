from discord import app_commands
from discord.utils import get # New import
from discord.ext import commands
import discord

intents = discord.Intents.all()
intents.members = True
TOKEN = 'YOUR TOKEN HERE'
bot = commands.Bot(command_prefix="(", intents=intents)
tree = bot.tree

#Guild ID
server_id = 938728183203758080

#Channels
channel_joinleave = 943602154428571708 # join and leave channel
channel_pplofthepit = 1243174332293976095

#Roles
role_admin = 938787942657327114
role_mod = 977248936148500550
role_owner = 938732039207809025
role_bot_smileyface = 938795313815240734
role_bot2 = 998594848582025269
role_pitted = 1057342828205846538
role_member = 938804320026099742
role_swagballer = 1003732468370776125

@bot.event
async def on_ready():
	await tree.sync(guild=discord.Object(id=server_id))
	print("The bot has successfully started.")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channel_joinleave)
    await channel.send(f"{member.mention} ({member}) joined the server!\nhttps://tenor.com/view/snsdmongus-dog-sideye-gif-21272558")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(channel_joinleave)
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
async def swagify(ctx, user: discord.Member):
    guild = ctx.guild
    role = ctx.guild.get_role(role_swagballer)
    await user.add_roles(role)
    await ctx.send(f"{user} is now a swag baller!!!!!!!!!")

@bot.command()
@commands.has_permissions(administrator=True)
async def unswagify(ctx, user: discord.Member):
    guild = ctx.guild
    role = ctx.guild.get_role(role_swagballer)
    await user.remove_roles(role)
    await ctx.send(f"{user} has gotten their swag priveleges revoked.")

@bot.command()
async def c2k(ctx, celsius: float):
    kelvin = celsius + 273
    await ctx.send(f"{celsius}°C is equal to {kelvin:.2f}°K.")

@bot.command()
async def k2c(ctx, kelvin: float):
    celsius = kelvin - 273
    await ctx.send(f"{kelvin}°K is equal to {celsius:.2f}°C.")
    
@tree.command(name="length", description="Convert cm to feet and vica versa", guild=discord.Object(id=server_id))	
@app_commands.describe(value="Value of length", system="The measurement system used for the value parameter. Options: cm, in, m, ft (Case sensitive)")
async def calculate(interaction: discord.Interaction, value: str, system: str):
    try:
        number = float(value)
        if system == 'cm':
            await interaction.response.send_message(f"{number:.3f}cm equals; \n- {number / 100:.3f} meters\n- {number / 2.54:.3f} inches\n- {number /30.48:.3f} feet")
        elif system == 'in':
            await interaction.response.send_message(f"{number:.3f}in equals; \n- {number * 0.0254:.3f} meters\n- {number * 2.54:.3f} centimeters\n- {number / 12:.3f} feet")
        elif system == 'm':
            await interaction.response.send_message(f"{number:.3f}m equals; \n- {number * 100:.3f} centimeters\n- {number / 0.0254:.3f} inches\n- {number * 3.280839895:.3f} feet")
        elif system == 'ft':
            await interaction.response.send_message(f"{number:.3f}ft equals; \n- {number * 30.48:.3f} centimeters\n- {number * 12:.3f} inches\n- {number * 0.3048:.3f} meters") 
        # https://preview.redd.it/zh4z7cem9kg51.png?auto=webp&s=90ff37f3925e3d8dfe41a88aafcf8f35a414d5b7
    except ValueError:
        await interaction.response.send_message("Invalid input! Please provide a valid number.")

@tree.command(
    name="temperature",
    description="Convert kelvin, fahrenheit and celsius.",
    guild=discord.Object(id=server_id)
)
@app_commands.describe(value="Value", system="The system that you inputted the value in. Options: k, c, f. (Case sensitive)")
async def calc(interaction: discord.Interaction, value: str, system: str):
    try:
        number = float(value)
        embed = discord.Embed(title="Calculation Result", color=discord.Color.yellow())

        if system == "k":
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Celsius", value=round(number - 273.15, 2), inline=True)
            embed.add_field(name="Fahrenheit", value=round(1.8 * (number - 273.15) + 32, 2))
        elif system == "c":
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Kelvin", value=round(number + 273.15, 2), inline=True)
            embed.add_field(name="Fahrenheit", value=round(number * 1.8 + 32, 2))
        elif system == "f":
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Kelvin", value=round(number + 459.67 * 5/9, 2), inline=True)
            embed.add_field(name="Celsius", value=round(number - 32 / 1.8, 2))
            
        await interaction.response.send_message(embed=embed)
    except ValueError:
        await interaction.response.send_message("Invalid input")
        
# PITTING SYSTEM
@tree.command(
    name="pit",
    description="pits someone",
    guild=discord.Object(id=server_id)
)
@app_commands.describe(reason="Reason will be posted in the public logging channel.")
async def pit(interaction: discord.Interaction, user: discord.Member, reason: str = ""):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return

    if user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return
    bot_member = interaction.guild.get_member(bot.user.id)
    bot_top_role = bot_member.top_role
    user_top_role = user.top_role

    if bot_top_role <= user_top_role:
        await interaction.response.send_message("I do not have permission to modify roles for this user.", ephemeral=True)
        return

    try:
        #
        if interaction.user.guild_permissions.manage_roles and reason != "":
            pit_role = discord.Object(id=role_pitted)  # pit role
            await user.edit(roles=[pit_role])
            await interaction.response.send_message(f"{user.mention} has been pitted.\nhttps://media.discordapp.net/attachments/1091036967199834112/1129035100915511376/attachment.gif")
            channel = client.get_channel(channel_pplofthepit) 
            await channel.send(f"{user.mention} ({user}) was pitted by {interaction.user.mention} for {reason}")
            await user.send(f'You have been pitted in 69SwagBalls420 cord for undisclosed reasons.')
        elif interaction.user.guild_permissions.manage_roles and reason == "":
            pit_role = discord.Object(id=role_pitted)  # pit role
            await user.edit(roles=[pit_role])
            channel = bot.get_channel(channel_pplofthepit)
            await interaction.response.send_message(f"{user.mention} has been pitted.\nhttps://media.discordapp.net/attachments/1091036967199834112/1129035100915511376/attachment.gif")
            await user.send(f'You have been pitted in 69SwagBalls420 cord for undisclosed reasons.')
            await channel.send(f"{user.mention} ({user}) was pitted by {interaction.user.mention} for unknown reasons! :DEVIL:")
        else:
            await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
    except discord.Forbidden:
            await interaction.response.send_message("403. I need to be higher in the role hiearchy.", ephemeral=True)
    except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)

@tree.command(
    name="unpit",
    description="unpits someone",
    guild=discord.Object(id=server_id)
)

@app_commands.describe(reason="Reason will be posted in the public logging channel.")
async def unpit(interaction: discord.Interaction, user: discord.Member, reason: str = ""):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return

    if user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return
    bot_member = interaction.guild.get_member(bot.user.id)
    bot_top_role = bot_member.top_role
    user_top_role = user.top_role

    if bot_top_role <= user_top_role:
        await interaction.response.send_message("I do not have permission to modify roles for this user.", ephemeral=True)
        return

    try:
        # 
        if interaction.user.guild_permissions.manage_roles and reason != "":
            greenrole = discord.Object(id=role_member)
            await user.edit(roles=[greenrole])
            await interaction.response.send_message(f"{user.mention}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif")
            channel = bot.get_channel(channel_pplofthepit) 
            await channel.send(f"{user.mention} ({user}) was unpitted by {interaction.user.mention} for reason: {reason}")
        elif interaction.user.guild_permissions.manage_roles and reason == "":
            greenrole = discord.Object(id=role_member)
            await user.edit(roles=[greenrole])
            channel = bot.get_channel(channel_pplofthepit)
            await interaction.response.send_message(f"{user.mention}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif")
            await channel.send(f"{user.mention} ({user}) was unpitted by {interaction.user.mention} for unknown reasons! :evil:")
        else:
            await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
    except discord.Forbidden:
            await interaction.response.send_message("403. I need to be higher in the role hiearchy.", ephemeral=True)
    except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)
        

bot.run(TOKEN)
