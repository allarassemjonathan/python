import youtube_dl
import discord
import os
from discord.ext import commands



Client =  commands.Bot(command_prefix='$')

@Client.command()
async def repeat(ctx, args):
	await ctx.send(args)

@Client.command()
async def hello(ctx):
	await ctx.send('Hello')

@Client.command()
async def server(ctx):
	name = str(ctx.guild.name)
	description = str(ctx.guild.description)
	owner = str(ctx.guild.owner)
	region = str(ctx.guild.region)
	memberCount = str(ctx.guild.member_count)
	id =str(ctx.guild.id)
	icon = str(ctx.guild.icon_url)
	embed = discord.Embed(
		title=name + " Server Information",
		description=description,
		color=discord.Color.blue()
	)
	embed.set_thumbnail(url=icon)
	embed.add_field(name='owner', value=owner, inline=True)
	embed.add_field(name='Server ID', value=id, inline=True)
	embed.add_field(name='Region', value=region, inline=True)
	embed.add_field(name='Member Count', value=memberCount, inline=True)
	await ctx.send(embed=embed)

@Client.command()
async def play(ctx, url_:str):
	song_there = os.path.isfile('song.mp3')
	try:
		if song_there:
			os.remove('song.mp3')
	except PermissionError:
		await ctx.send('Wait for the song to finish')
		return

	voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
	await voiceChannel.connect()
	voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)

	ydl_ops = {
		'format':'bestaudio/best',
		'postprocessors':[{
			'key':'FFmpegExtractAudio',
			'preferredcodec':'mp3',
			'preferredquality': '192',
		}],
	}

	with youtube_dl.YoutubeDL(ydl_ops) as ydl:
		ydl.download([url_])
	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			os.rename(file, 'song.mp3')
	voice.play(discord.FFmpegPCMAudio('song.mp3'))

@Client.command()
async def leave(ctx):
	 voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
	 if voice.is_connected():
	    await voice.disconnect()
	 else:
	    await ctx.send('the voice is already off')

@Client.command()
async def pause(ctx):
	voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
	if voice.is_playing():
		voice.pause()
	else:
		ctx.send('the voice is already paused')

@Client.command()
async def resume(ctx):
	voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
	if voice.is_paused():
		voice.resume()
	else:
		await ctx.send('The audio is already playing')

@Client.command()
async def stop(ctx):
	voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
	voice.stop()

Client.run('NzkwODk0OTk2MDE0MzY2Nzcx.X-HQXQ.OwCwQrrWMDYwYS45BAJ34fJqRPc')
