import os
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

# Message
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Messsage was empty')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
        
    if is_command := user_message[0] == '!':
        try:
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(e)
        
# Handling startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} calismaya basladi')
    
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
    
    
# main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
