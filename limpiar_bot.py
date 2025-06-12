import asyncio
from telegram import Bot

TOKEN = "8178987489:AAF8xInlw8lkFECB7JJ-xn5uJODIkVUgNvY"

async def clear_webhook():
    bot = Bot(token=TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook eliminado y actualizaciones borradas.")

asyncio.run(clear_webhook())

