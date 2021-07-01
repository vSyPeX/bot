import random
from discord.ext.commands import Bot
import discord
import asyncio


TOKEN = "ODIyNDYwMzM4MTA4MTA0NzA2.YFSl4Q.NMSICxpXwmOSCZujfdDc4JgR5ZM"  # DISCORD TOKEN
client = Bot('')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.send('Private message')


def Tru(m):
    return True


tkm = ['t', 'k', 'm']


@client.event
async def on_message(message):
    if message.author == client.user:
        return 0
    elif message.content == '!tkm':
        await asyncio.sleep(3)
        d = random.choice(tkm)
        u = message.channel.last_message
        await message.channel.send('{} {}'.format(d, u.content))
        s = (d+" "+u.content)
        print(s)
        if s in ['t k', 'm t', 'k m']:
            await message.channel.send('WI')

        elif s in ['k t', 't m', 'm k']:
            await message.channel.send('LO')

        elif s in ['k k', 't t', 'm m']:
            await message.channel.send('DR')

    elif message.content == '!temizle':
        # print(message.channel.last_message.content,"silindi")
        # await message.channel.last_message.delete()
        # await client.delete_messages(message.channel.last_message)

        deleted = await message.channel.purge(limit=100, check=Tru)
        await message.channel.send('Deleted {} message(s)'.format(len(deleted)))


client.run(TOKEN)
