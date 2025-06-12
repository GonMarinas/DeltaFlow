from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Token del bot
TOKEN = "8178987489:AAF8xInlw8lkFECB7JJ-xn5uJODIkVUgNvY"

# Función para manejar el comando /getlink
async def get_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id  # ID del grupo donde está el bot

    try:
        # Crear un enlace único
        bot = context.bot
        invite_link = await bot.create_chat_invite_link(
            chat_id=chat_id,
            name="Acceso Único",
            expire_date=None,  # Puede configurarse una fecha de expiración
            member_limit=1  # Limitar a un solo uso
        )
        await update.message.reply_text(f"Aquí tienes tu enlace único: {invite_link.invite_link}")
    except Exception as e:
        await update.message.reply_text(f"Error al generar el enlace: {e}")

# Función para obtener el ID del chat
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"El ID de este chat es: {chat_id}")

# Configurar el bot
def main():
    # Crear la aplicación
    application = Application.builder().token(TOKEN).build()

    # Asociar comandos y manejadores
    application.add_handler(CommandHandler("getlink", get_link))  # Handler para /getlink
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_chat_id))  # Handler para mensajes de texto

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
