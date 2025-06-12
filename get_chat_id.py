import asyncio
from telegram import Bot

TOKEN = "8178987489:AAF8xInlw8lkFECB7JJ-xn5uJODIkVUgNvY"
bot = Bot(token=TOKEN)

async def main():
    updates = await bot.get_updates()
    for update in updates:
        if update.message:
            print(f"Chat ID: {update.message.chat.id} - Chat type: {update.message.chat.type}")

asyncio.run(main())
