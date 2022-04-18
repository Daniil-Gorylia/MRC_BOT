import content
import database


def mailing_all():
    resp = f"https://nalog.gov.by/{content.MRC_primen()[0]}"
    database.set_primMRC(resp)
    resp2 = f"https://nalog.gov.by/{content.MRC_zayav()[0]}"
    database.set_zayavMRC(resp2)
