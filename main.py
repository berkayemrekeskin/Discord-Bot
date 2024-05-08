import os
import json
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from discord.ext import commands

# Load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot setup
intents : Intents = Intents.default()
intents.message_content = True
command_prefix = '!'
client : commands = commands.Bot(command_prefix=command_prefix, intents=intents)
with open('data.json', 'r') as file:
    data = json.load(file)


# Message
async def send_message(message: Message, user_message: str) -> None:
    
    if not user_message:
        print('Messsage was empty')
        return
    
    elif is_private := user_message[0] == '?':
        user_message = user_message[1:]
        
    elif is_command := user_message[0] == '!':
        user_message = user_message[1:]
    
    msg_list = user_message.split(" ")
    
    try:
        response: str = get_response(msg_list, data)
        if is_private:
            await message.author.send(response)
        elif is_command:
            await message.channel.send(response)
    except Exception as e:
        print(e)

# Handling startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} started running!')
    
# Handling income messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
