import discord
import os
import random
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from discord import app_commands, Embed, ui
from random import randint
from discord.app_commands import Group, command
from discord.ext.commands import GroupCog

server_id = 938728183203758080 # as much as id like to use env files i dont want to make meme alt to download more libraries

class Nep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    neps = [
            "<:the:1362753377661878312>",
            "<:theaero:1329588697301254146>",
            "<:thebhel:1298671218869932133>",
            "<:theborg:1325126908035469382>",
            "<:thecold:1329993501634728026>",
            "<:thecount:1325123075381002301>",
            "<:thecop:1362848930366357664>",
            "<:thecthep:1336096513671299204>",
            "<:thecult:1343251423005114368>",
            "<:thedad:1370855744722829372>",
            "<:thedanger:1329858685241135174>",
            "<:thedeep:1325157787793100810>",
            "<:thedev:1287807400358707281>",
            "<:thediv:1301340982645624884>",
            "<:theexe:1335056775660961832>",
            "<:theflame:1360256388785246238>",
            "<:thefool:1336076723292213348>",
            "<:thefungus:1338309354138636383>",
            "<:thefunk:1345804296343650437>",
            "<:thegem:1341385710975848509>",
            "<:theghoul:1334912579625025687>",
            "<:thegnep:1249460660937555988>",
            "<:thegod:1335693180276051983>",
            "<:thegrug:1339283531595255830>",
            "<:thehap:1328066153729233060>",
            "<:thehemp:1325611671003205642>",
            "<:thehotep:1339284557354111089>",
            "<:theice:1335653196571480084>",
            "<:theinfinep:1324804511620927600>",
            "<:thejinn:1325155782492291144>",
            "<:thejoy:1329590818566311996>",
            "<:theknep:1335653219816312934>",
            "<:themeh:1337485931158048953>",
            "<:themob:1324822716905160725>",
            "<:themonk:1324802296072376391>",
            "<:themusicofthespheres:1324229870708068403>",
            "<:thenap:1325134800960622632>",
            "<:thenec:1325130769475043369>",
            "<:theneo:1345748691469996062>",

            "<:thenep:1247985898017128540>",

            "<:thenepbeard:1329985955461070939>",
            "<:thenepertiti:1334258318222426233>",
            "<:thenepestroika:1334274530486652938>",
            "<:theneplings:1335730157075300473>",
            "<:thenepoleon:1325120690327916655>",
            "<:theneportal1:1340392586954805268>",
            "<:theneportal2:1340392613286514832>",
            "<:thenepotism:1304878220784566342>",
            "<:theneprole:1305216257275990066>",
            "<:theneptune:1334195846543315048>",
            "<:thenepula:1324804380272103444>",
            "<:thenop:1328438217070088323>",
            "<:theocracy:1336069621035438122>",
            "<:thenord:1352790494005952613>",
            "<:thepenpen:1331575733042155520>",
            "<:thepetal:1331022738596565032>",
            "<:theplanep:1335035983959294003>",
            "<:thepolynepus:1350836223144362014>",
            "<:thepride:1335448454394150974>",
            "<:theprime:1335060174808809553>",
            "<:thepunk:1345804531602296965>",
            "<:therage:1329506816643563570>",
            "<:therah:1343251602189975672>",
            "<:thergb:1330664578266304644>",
            "<:therip:1329996095887118366>",
            "<:theroot:1305705004488986726>",
            "<:therot:1279356490955624509>",
            "<:thesad:1330674346192011374>",
            #god this is painstaking
            "<:thescnep:1253011439694643320>",
            "<:thesky:1334957927642955796>",
            "<:theslen:1325161237729906688>",
            "<:thesnep:1305726730530717736>",
            "<:thesoy:1328469674257809439>",
            "<:thetang:1324641842356293684>",
            "<:thetrue:1328463491027439647>",
            "<:thewar:1325123916934545458>",
            "<:thewest:1325143534101200906>",
            "<:thewind:1324462663987892245>",
            "<:thewiz:1324233457177464884>",
            "<:theyakuza:1335693421284954152>",
            "<:theyar:1335636787162386492>",
            "<:theyep:1328089549452214332>",
    ]

    @command(
        name="nep",
        description="nep generator 2000"
    )
    async def nep(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.choice(self.neps))

    @command(
        name="nep-flip",
        description="flip a nep coin"
    )
    async def nep(self, interaction: discord.Interaction):
        choice = random.randint(1,2)
        if choice == 1:
            await interaction.response.send_message("<:theyep:1328089549452214332>")
        else:
            await interaction.response.send_message("<:thenop:1328438217070088323>")

async def setup(bot: commands.Bot):
    await bot.add_cog(Nep(bot), guild=discord.Object(id=server_id))
