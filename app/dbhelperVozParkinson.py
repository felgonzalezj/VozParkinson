import sqlite3


class DBHelper:
    def __init__(self, dbname=r"C:\Users\felgo\Desktop\VozParkinson\VozParkinson\VozParkinson.sqlite3"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)


    def update_estado(self, condicion):
        stmt = "UPDATE app_publicacion SET estado = 1 WHERE fecha_publicacion = (?)"
        args = (condicion, )
        self.conn.execute(stmt, args)
        self.conn.commit()