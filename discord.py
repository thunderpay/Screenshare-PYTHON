import pyautogui
import discord
import asyncio

# Discord bot setup
client = discord.Client()
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
channel_id = 'YOUR_DISCORD_CHANNEL_ID'

# Function to take Minecraft screenshots
async def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('minecraft_screenshot.png')
    return 'minecraft_screenshot.png'

# Function to send screenshot to Discord
async def send_screenshot():
    channel = client.get_channel(channel_id)
    screenshot_file = await take_screenshot()
    await channel.send(file=discord.File(screenshot_file))

# Event: Bot connected to Discord
@client.event
async def on_ready():
    print('Bot connected to Discord!')
    while True:
        await send_screenshot()
        await asyncio.sleep(60)  # Send screenshot every 60 seconds

# Run the bot
client.run(TOKEN)
