from flask import Flask, request, jsonify
from telegram import Bot
import asyncio

app = Flask(__name__)

TOKEN = "8178987489:AAF8xInlw8lkFECB7JJ-xn5uJODIkVUgNvY"
bot = Bot(token=TOKEN)

chat_id_grupo = -1002522015956  # Cambia por tu chat_id

# Registrar todas las solicitudes para depuración
@app.before_request
def log_request():
    print(f"Request: {request.method} {request.url}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.data.decode('utf-8')}")

@app.route('/create_invite', methods=['GET', 'POST'])
def create_invite():
    if request.method == 'GET':
        return jsonify({"message": "Usa POST para generar un enlace único."})

    # POST
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        invite_link = loop.run_until_complete(bot.create_chat_invite_link(
            chat_id=chat_id_grupo,
            name="Acceso Único",
            member_limit=1
        ))
        return jsonify({"invite_link": invite_link.invite_link})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
