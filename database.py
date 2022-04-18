import psycopg2
import inform
import MRC_bot
import content


conn = psycopg2.connect(host=inform.host, dbname=inform.database,
                        user=inform.user, password=inform.password)

#id
#user_id
#username
#first_name
#last_name

cur = conn.cursor()


def set_user(user_id, username, first_name, last_name):
    cur.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    data = cur.fetchone()
    if data is None:
        cur.execute(f"INSERT INTO users (user_id, username, first_name, last_name) "
                    f"VALUES ('{user_id}', '{username}', '{first_name}', '{last_name}');")
        conn.commit()


def set_primMRC(download_link):
    cur.execute(f"SELECT download_link FROM prim_MRC WHERE download_link = '{download_link}'")
    data = cur.fetchone()
    if data is None:
        cur.execute(f"INSERT INTO prim_MRC (download_link) VALUES ('{download_link}')")
        conn.commit()



def set_zayavMRC(download_link):
    cur.execute(f"SELECT download_link FROM zayav_MRC WHERE download_link = '{download_link}'")
    data = cur.fetchone()
    if data is None:
        cur.execute(f"INSERT INTO zayav_MRC (download_link) VALUES ('{download_link}')")
        conn.commit()



def sub(user_id):
    cur.execute(f"UPDATE users SET subscription = TRUE WHERE user_id = '{user_id}';")
    conn.commit()


def unsub(user_id):
    cur.execute(f"UPDATE users SET subscription = FALSE WHERE user_id = '{user_id}';")
    conn.commit()
