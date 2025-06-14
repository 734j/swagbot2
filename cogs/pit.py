import discord
import os
import sqlite3
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from discord import app_commands, Embed, ui
from datetime import datetime
from discord.app_commands import Group, command
from discord.ext.commands import GroupCog

server_id = 938728183203758080 # as much as id like to use env files i dont want to make meme alt to download more libraries
role_pitted = 1057342828205846538 
channel_pit = 1057343199888285786
channel_pplofthepit = 1243174332293976095

class Pit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def generic_pit(
        self, user, reason, roles, moderator, interaction
    ):
        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()
        parsedRoles = str(roles)
        
        c.execute("""CREATE TABLE IF NOT EXISTS pitties(
                     target_user_id BIGINT NOT NULL UNIQUE, -- pitted persons id
                     target_user_roles TEXT NOT NULL, -- pitted persons roles upon pitting
                     reason TEXT, 
                     moderator BIGINT NOT NULL --moderator that carried out the pitting
                     )""")

        c.execute("""INSERT INTO pitties(target_user_id, target_user_roles, reason, moderator)
                                    VALUES (?, ?, ?, ?);
                                 """, (user, reason, roles, moderator)) # don't ask me why, it just works

    
        pit_role = discord.Object(id=role_pitted)  # pit role
        await interaction.guild.get_member(user).edit(roles=[pit_role])
        conn.commit()
        conn.close()
    
    async def generic_unpit(
        self, user, reason, interaction
    ):
        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()       
        
        c.execute(f"SELECT * FROM pitties WHERE target_user_id = {user}")
        row = c.fetchone()
        if row:
            user_id = row[0]
            roles = row[1]
            reason = row[2]
            moderator = row[3]

            listRoles = eval(roles)
            member = interaction.guild.get_member(user_id)
            
            parsedRoles = [interaction.guild.get_role(role) for role in listRoles]

            await member.edit(roles=parsedRoles)
            c.execute(f"DELETE FROM pitties WHERE target_user_id = {user}")
            conn.commit()
            conn.close()
            print("done succesfully")
        else:
            await interaction.response.send_message("User not pitted!")
        

    @command(
        name="pit",
        description="Pit someone"
    )
    @app_commands.describe(reason="Reason will be posted in the public logging channel.")
    async def pit(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
        if user.guild_permissions.manage_roles:
            await interaction.response.send_message(
                "https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.",
                ephemeral=True,
            )
            return
        bot_member = interaction.guild.get_member(self.bot.user.id)
        bot_top_role = bot_member.top_role
        user_top_role = user.top_role
        pitted_gif = "https://cdn.discordapp.com/attachments/938739040667201536/1340065789033709730/copy_7C870B9C-E3BA-4575-8CCF-9FB778977AED.gif?ex=67b10105&is=67afaf85&hm=173643969836e2ebffaf200e37640501f6926bda04acde0f6ca7b0d2b4489b76&"
    
        if bot_top_role <= user_top_role:
            await interaction.response.send_message(
                "I do not have permission to modify roles for this user.", ephemeral=True
            )
            return
    
        try:
            pit = interaction.client.get_channel(channel_pit)
            if reason != None:
                role_ids = [role.id for role in user.roles if role.id != interaction.guild.id]
                await self.generic_pit(user.id, str(role_ids), reason, interaction.user.id, interaction)
                await interaction.response.send_message(
                    f"{user.mention} has been pitted.\n{pitted_gif}"
                )
                channel = interaction.client.get_channel(channel_pplofthepit)
                await user.send(
                    f"You have been pitted in 69SwagBalls420 cord for reason: {reason}."
                )
                await channel.send(
                    f"{user.mention} ({user}) was pitted by {interaction.user.mention} for reason: {reason}."
                )
                await pit.send(
                    f"A loud thud shakes the depths of the Pit as {user.mention} ({user}) falls to the ground... Welcome your new friend."
                )
            elif reason == None:
                await generic_pit(interaction, user)
                channel = interaction.client.get_channel(channel_pplofthepit)
                await interaction.response.send_message(
                    f"{user.mention} has been pitted.\n{pitted_gif}"
                )
                await user.send(
                    f"You have been pitted in 69SwagBalls420 cord for undisclosed reasons."
                )
                await channel.send(
                    f"{user.mention} ({user}) was pitted by {interaction.user.mention} for unknown reasons! :DEVIL:"
                )
                await pit.send(
                    f"A loud thud shakes the depths of the Pit as {user.mention} ({user}) falls to the ground... Welcome your new friend."
                )
            else:
                role_ids = [role.id for role in user.roles if role.id != interaction.guild.id]
                await self.generic_pit(user.id, str(role_ids), None, interaction.user.id, interaction)
                await interaction.response.send_message(
                    "https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.",
                    ephemeral=True,
                )
        except discord.Forbidden:
            await interaction.response.send_message(
                "403. I need to be higher in the role hiearchy.", ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"An unexpected error occurred: {str(e)}", ephemeral=True
            )


    @command(
        name="unpit", description="unpits someone"
    )
    @app_commands.describe(reason="Reason will be posted in the public logging channel.")
    async def unpit(
        self, interaction: discord.Interaction, user: discord.Member, reason: str = None
    ):
        if user.guild_permissions.manage_roles:
            await interaction.response.send_message(
                "https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.",
                ephemeral=True,
            )
            return
        bot_member = interaction.guild.get_member(self.bot.user.id)
        bot_top_role = bot_member.top_role
        user_top_role = user.top_role
    
        if bot_top_role <= user_top_role:
            await interaction.response.send_message(
                "I do not have permission to modify roles for this user.", ephemeral=True
            )
            return
    
        try:
            if reason != None: 
                await self.generic_unpit(user.id, reason, interaction)
                await interaction.response.send_message(
                    f"{user.mention}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif"
                )
                channel = interaction.client.get_channel(channel_pplofthepit)
                await channel.send(
                    f"{user.mention} ({user}) was unpitted by {interaction.user.mention} for reason: {reason}"
                )
    
            elif reason == None:

                await self.generic_unpit(user.id, None, interaction)
                await interaction.response.send_message(
                    f"{user.mention}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif"
                )
                channel = interaction.client.get_channel(channel_pplofthepit)
                await channel.send(
                    f"{user.mention} ({user}) was unpitted by {interaction.user.mention} for unknown reasons!"
                )
            else:
                await interaction.response.send_message(
                    "https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.",
                    ephemeral=True,
                )
        except discord.Forbidden:
            await interaction.response.send_message(
                "403. I need to be higher in the role hiearchy.", ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"An unexpected error occurred: {str(e)}", ephemeral=True
            )

async def setup(bot: commands.Bot):
    await bot.add_cog(Pit(bot), guild=discord.Object(id=server_id))
