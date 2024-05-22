'''
depending on how python 3.10 installed pip either pip install discord.py or apt-get install python3-discord
'''
import discord
from discord.ext import commands
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True  # make sure it can read chat in channels (this will have to get changed since it will read any channel it can see currently so it will probably read #announcments and reply there to lmao
bot = commands.Bot(command_prefix='!', intents=intents)

keyword_responses = {
    "wipe": "No. The wipe has now been pushed back. ",
        # other words can be added here if we want it to trigger on anything else
}

# date counter, starts at the current date
date_counters = {
    "wipe": datetime.now(),
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # bot wont reply to its self since that is silly
        # Check if any keyword is in the message content
    for keyword in keyword_responses:
        if keyword in message.content.lower():
            # increment the date by one day
            date_counters[keyword] += timedelta(days=1)
            # replies to the message
            response = f"{keyword_responses[keyword]} The new date for wipe is {date_counters[keyword].strftime('%Y-%m-%d')}."
            await message.reply(response)
            break  # Stop checking if it finds wipe in a message and post a response

    await bot.process_commands(message)
# bot token
bot.run('bot token here')