import discord
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import commands

import pokebase as pb

import os
from dotenv import load_dotenv

#-----------------------------MAIN------------------------------#
bot = commands.Bot(command_prefix=",p ", intents=discord.Intents.default())

@bot.command(pass_context=True,aliases=["v"])
async def view(ctx, pname):
	p = pb.pokemon(pname.lower())
	
	types = "`"
	for i in range(len(p.types)):
		types += p.types[i].type.name+"/"
	types = types[:-1]
	types += "`"
	
	abilities = ""
	for i in range(len(p.abilities)):
		abilities += str(i+1)+" - `"+p.abilities[i].ability.name+"`\n"
	
	embed = discord.Embed(title=f"{p.id} - {p.name}", color=0xfcfc14)
	embed.set_thumbnail(url=p.sprites.front_default)
	embed.add_field(name="General Info", value=f"Type: `{types}`\nHeight: `{p.height}`\tWeight: `{p.weight}`", inline=False)
	embed.add_field(name="Stats", value=f"HP: `{p.stats[0].base_stat}`\nATK/DEF: `{p.stats[1].base_stat}/{p.stats[2].base_stat}`\nSP ATK/SP DEF: `{p.stats[3].base_stat}/{p.stats[4].base_stat}`\nSpeed: `{p.stats[5].base_stat}`", inline=False)
	embed.add_field(name="Abilities", value=f"{abilities}", inline=False)
	await ctx.message.channel.send(embed=embed)


#-------------------------TOKEN---------------------------------#
load_dotenv()
bot.run(os.getenv("TOKEN"))
