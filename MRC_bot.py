import content
import telebot
import database
from telebot import types
token = "5180389254:AAEty1vOHrbLAfSFnqFiJZqqXQQj5PsIVC0"
bot = telebot.TeleBot(token)

def main():
    @bot.message_handler(commands=["start"])
    def start_func(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("Запросить применяемые мрц")
        btn3 = types.KeyboardButton("Запросить заявленные мрц")
        markup.add(btn1, btn2, btn3)
        user_id = message.from_user.id
        bot.send_message(user_id, 'Привет, это бот который отправляет информация об максимальных розничных ценах в '
                                ' республике Беларусь'.format(message.from_user), reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def func(message):
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        database.set_user(user_id, username, first_name, last_name)

        if message.text == "👋 Поздороваться":
            bot.send_message(user_id, 'Привет, для того чтобы использовать бота, используйте соответствующие кнопки'
                                    '\n Данный бот показывает как заявленные МРЦ, так и применяемые МРЦ')
        elif message.text == "Запросить применяемые мрц":
            resp = f"https://nalog.gov.by/{content.MRC_primen()[0]}"
            database.set_primMRC(resp)
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton("Последнее применяемое мрц", url=resp)
            markup.add(btn)
            bot.send_message(user_id, "Для скачивания последнего применяемого мрц, нажмите кнопку", reply_markup=markup)
        elif message.text == "Запросить заявленные мрц":
            resp = f"https://nalog.gov.by/{content.MRC_zayav()[0]}"
            database.set_zayavMRC(resp)
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton("Последнее заявленное мрц", url=resp)
            markup.add(btn)
            bot.send_message(user_id, "Для скачивания последнего заявленного мрц, нажмите кнопку", reply_markup=markup)

