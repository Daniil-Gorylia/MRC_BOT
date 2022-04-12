import telebot
from flask import Flask, request
import MRC_bot
import os

server = Flask(__name__)

bot = MRC_bot.bot

MRC_bot.main()


@server.route('/' + bot.token, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://mrcs-bot.herokuapp.com/' + bot.token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
