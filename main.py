import discord
from discord.ext import commands
from discord.ext.commands import Bot


#music
bot = commands.Bot(command_prefix='.')
bot.lavalink_nodes = [{"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},]
bot.spotify_credentials = {
	'client_id': '63e6026be7a34a21b7fe283d764062ce',
	'client_secret': 'b4088d258e7448d58e6a87235be514be'
}
#send_message
#853408121695633419

#client = discord.Client()

#async def sender(text):
    #channel = client.get_channel(id=853408121695633419)
    #await channel.send(text)

#@client.event
#async def on_ready():
    #print('Bot ready')
    #await sender('Hello NIGGERS')
    #await sender("commands: \n.connect (підключити бот до себе) \n.nowplayng (Зараз відтворюється інформація про пісню) \n.pause \n.play \n.queue (Черга гравців) \n.resume (Відновити програвач) \n.seek (Шукайте гравця назад або вперед) \n.skip \n.stop \n.volume ")
#start
bot.load_extension('dismusic')
#client = MyClient()
#client.run('OTU5MTA4NTM4OTE4MTQyMDEz.YkXFbw.tm_M9LIsn7f2ceYIPdGvhAV8Tw0')
bot.run('OTU5MTA4NTM4OTE4MTQyMDEz.YkXFbw.tm_M9LIsn7f2ceYIPdGvhAV8Tw0')

















#class MyClient(discord.Client):
	#async def in_ready(self):
		#print('Logged on as {0}!'.format(self.user))

	#async def on_message(self, message):
		#print('Message from {0.author}: {0.content}'.format(message))