from telethon import TelegramClient, events
import credentials

# Credenciales de tu API
api_id = credentials.api_id
api_hash = credentials.api_hash

# Crea el cliente usando una sesión de usuario
client = TelegramClient('user_session', api_id, api_hash)

# Canal a monitorear
# channel_to_monitor = -1002094282515
# channel_to_monitor = 771096498
channel_to_monitor = 616044209

# Tu chat_id personal
your_chat_id = 616044209

@client.on(events.NewMessage(chats=channel_to_monitor))
async def monitor(event):
    print(event.message.message)
    message = event.message.message  # Texto del mensaje recibido
    # Verificar palabras clave
    if 'sell entry' in message.lower() or 'buy entry' in message.lower():
        # Enviar notificación a tu chat personal
        await client.send_message(your_chat_id, f"Se detectó un mensaje: {message}")

# Iniciar el cliente (te pedirá el teléfono y código la primera vez)
client.start()

print("El cliente de usuario está ejecutándose...")
client.run_until_disconnected()