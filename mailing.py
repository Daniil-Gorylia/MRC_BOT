import content
import database
import MRC_bot

def mailing_all():
    MRC_bot.bot.send_message(database.sub_check()[0], "Вышло новое обновление заявленных мрц, проверьте ссылку")


mailing_all()
