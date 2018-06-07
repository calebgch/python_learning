import pymysql


class Database(object):
    db = None

    def __init__(self):
        if Database.db is None:
            Database.db = pymysql.connect("localhost", "root", "passw0rd", "python")

    def get_one(self, sql):
        cursor = Database.db.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    def get_all(self, sql):
        cursor = Database.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def execute(self, sql):
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
