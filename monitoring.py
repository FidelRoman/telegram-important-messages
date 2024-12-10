from telethon import TelegramClient, events
import credentials 

# Assign credentials
api_id = credentials.api_id
api_hash = credentials.api_hash
bot_token = credentials.bot_token

# Configure the bot client
bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# ID or @username of the channel to monitor
channel_to_monitor = '@lookerstudioespanol'

@bot.on(events.NewMessage(chats=channel_to_monitor))
async def monitor(event):
    message = event.message.message  # Text of the received message
    # Check for the keywords "SELL ENTRY" or "BUY ENTRY"
    if 'sell entry' in message.lower() or 'buy entry' in message.lower():
        # Send the detected message to your chat ID
        your_chat_id = event.message.sender_id  # Change this if you need a fixed ID
        await bot.send_message(your_chat_id, f"Detected message: {message}")

# Start the bot
print("Bot is running...")
bot.run_until_disconnected()