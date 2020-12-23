import discord
import os
import requests
import json

from discord.ext import commands



def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return quote



Client = discord.Client()


@Client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(Client))


@Client.event
async def on_message(message):
	if message.author == Client.user:
		return
	msg = message.content
	
	if msg.startswith('$hello'):
		await message.channel.send('Hello!')
	'''
	if msg.startswith('$repeat'):
		string = msg.split("$repeat",1)[1]
		await message.channel.send(string)
	'''
	if msg.startswith('$inspire'):
		quote = get_quote()
		await message.channel.send(quote)
Client.run('NzkwODk0OTk2MDE0MzY2Nzcx.X-HQXQ.OwCwQrrWMDYwYS45BAJ34fJqRPc')
