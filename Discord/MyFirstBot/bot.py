from discord.ext import commands
import discord


client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is ready")

@client.event
async def on_member_join(member):
	print(f"{member} servere katildi mk.")

@client.event
async def on_member_remove(member):
	print(f"{member} serverden ayrildi sg.")

@client.command()
async def hakansmommy(ctx):
	await ctx.send("Hakansmommy is gooden boy")

@client.command()
async def gokay(ctx):
	await ctx.send("Gokay is the only and real gay on this discord!")

@client.command()
async def utku(ctx):
	await ctx.send("Sikerim Seni")

@client.command()
async def memed(ctx):
	await ctx.send("Memed the cainess")

@client.command()
async def batu(ctx):
	await ctx.send("Batu's dick is big !")

@client.command()
async def sen(ctx):
	await ctx.send("bak")
	await ctx.send("kab")
	await ctx.send("bak")
	await ctx.send("SEn")
	await ctx.send("bAna")
	await ctx.send("Böle")
	await ctx.send("bak")
	await ctx.send("YapamaSIN")
	await ctx.sen("bak")

@client.command()
async def bak(ctx):
	await ctx.send("bak")
	await ctx.send("kab")
	await ctx.send("bak")
	await ctx.send("bak")
		
@client.command()
async def klaud(ctx):
	await ctx.send("Klaud caz yapma sikerim belanı bak beni delirtme")

@client.command()
async def emre(ctx):
    await ctx.send("Keops")

@client.command()
async def botvs(ctx):
	await ctx.send("")


client.run("my bot token :)")
