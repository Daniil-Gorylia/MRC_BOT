import content
import database


def mailing_all():
    a = content.MRC_primen()[0]
    b = content.MRC_zayav()[0]
    resp = f"https://nalog.gov.by/{a}"
    database.set_primMRC(resp)
    resp2 = f"https://nalog.gov.by/{b}"
    database.set_zayavMRC(resp2)


mailing_all()
