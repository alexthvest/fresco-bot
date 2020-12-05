from flask import Flask, request
from bot import FrescoBot


app = Flask(__name__)
bot = FrescoBot("YOUR_TOKEN_HERE", "YOUR_CONFIRMATION_CODE_HERE")


@app.route("/", methods=["POST"])
def index():
    data = request.get_json(force=True, silent=True)

    if not data or 'type' not in data:
        return 'fail'

    return bot.handle_callback(data)


if __name__ == "__main__":
    app.run()
