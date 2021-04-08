#Import Libraries
from mcstatus import MinecraftServer
from socket import gaierror
import discord

#Server to look up
server = MinecraftServer.lookup("hermitsmelt.tk")

#Discord Configuration
TOKEN = "ODI5Njk0NTY5ODUwOTk0Njk4.YG73SA.KvPn4qon6J1OoMR5PqZZiF7-5Ks"
GUILD ="HermitSmelt"

#Initiate the Discord client
client = discord.Client()

#print to console that it is ready to start
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content == '?map':
      status = "Map link : http://hermitsmelt.tk:25570"

    if message.content == '?up':
      try:
        serverout = server.status()
        status = "The server has "+str(serverout.players.online)+" players and replied in "+str(serverout.latency)+" ms"
        
      except gaierror:
        status = "Server is unreachable"
      
      except ConnectionRefusedError:
        status = "Server is Down"

    await message.channel.send(status)

client.run(TOKEN)