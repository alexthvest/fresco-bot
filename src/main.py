from bot import FrescoBot
from config import TOKEN, CONFIRMATION_CODE, SECRET_KEY
from flask import Flask, request


app = Flask(__name__)
bot = FrescoBot(TOKEN, CONFIRMATION_CODE)


@app.route("/", methods=["GET"])
def index():
    return "Жак Фреско Бот"


@app.route("/bot", methods=["POST"])
def bot_callback():
    data = request.get_json(force=True, silent=True)

    if not data or "type" not in data:
        return "fail"

    if "secret" not in data or data["secret"] != SECRET_KEY:
        return "fail"

    return bot.handle_callback(data)


if __name__ == "__main__":
    app.run()
