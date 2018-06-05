import pymysql


class Database(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "passw0rd", "mysql")

    def __del__(self):
        self.db.close()

    def get_one(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    def get_all(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
