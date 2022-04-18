import content
import database
import MRC_bot

def mailing_all():
    resp = f"https://nalog.gov.by/{content.MRC_primen()[0]}"
    database.set_primMRC(resp)
    resp2 = f"https://nalog.gov.by/{content.MRC_zayav()[0]}"
    database.set_zayavMRC(resp2)
    MRC_bot.bot.send_message(database.sub_check()[0], "Вышло новое обновление заявленных мрц, проверьте ссылку")


mailing_all()
