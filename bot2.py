import discord  # discord.py module
from discord.ext import commands
import asyncio
from discord.ext import tasks
import time

bot = commands.Bot(command_prefix='.')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):  # When a message is sent
        if (message.author.bot == False):  # If the message is not from a bot
            
            channel = message.channel.name
            restricted_channels = ["general"] # List of restricted channels

            prefix = "!"  # Replace with your prefix
            # If the message starts with the prefix
            if message.content.startswith(prefix):
                if channel in restricted_channels: # If the message was sent in a restricted channel
                    command = message.content[len(prefix):]  # Get the command
                    # Check if the user is an admin
                    isAdmin = [role.name ==
                            "Admin" for role in message.author.roles][0]
                    # Check for commands
                    if command == "hello" and isAdmin:
                        # Send a message
                        await message.channel.send("Hello Admin!")
                    if command == "bo3":
                        await message.channel.send("is useless")
                    if command == "help":
                        await message.channel.send("```\n"
                                                "Commands:\n"
                                                "help - This is the help §erver stats\n"
                                                "```")
                    if command == "log stop":
                        myLoop.stop()
                    if command == "log":

                        @tasks.loop(seconds = 10) # repeat after every 10 seconds
                        async def myLoop():
                            await message.channel.send('working')
                            await message.channel.send(file=discord.File('output.jpg'))
                            
                        myLoop.start()
                    
                        
                    else:
                        # If the command is not found
                        await message.channel.send("This command doesn't exist")
                else:
                    await message.delete()
                    await message.author.send(f"You can't use commands in #{channel}")
                    # await message.channel.send("You can't use commands in this channel")\
                

client = MyClient()
# Replace with your token
client.run('MTA4ODMxNzAwMjc5NzU0NzYwMQ.G7rb6T.tPL0WDLgSGp8kPl459BnkryJXqIqKG-BYSSBwQ')
