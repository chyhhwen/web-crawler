import pymysql
import datetime
def select():
    db_settings = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "",
        "db": "stonk",
        "charset": "utf8"
    }
    try:
        conn = pymysql.connect(**db_settings)
        with conn.cursor() as cursor:
            quary = "SELECT * FROM data"
            cursor.execute(quary)
            data = cursor.fetchall()
            print(data)
    except Exception as ex:
        print(ex)

def insert(sid,name,price):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='stonk', charset='utf8')
    cursor = db.cursor()
    quary = "INSERT into `data`(`sid`,`name`,`price`,`time`) VALUES " \
            "('" + sid + "'," + "'" + name + "'," + "'" + price + "'," + "'" + time + "')"
    print(quary)
    try:
        cursor.execute(quary)
        db.commit()
        print('success')
    except Exception as ex:
        db.rollback()
        print(ex)
    db.close()


if __name__ == '__main__':
    insert("12","12","12")
