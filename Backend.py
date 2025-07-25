import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS store(ID INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Year INTEGER,ISBN INTEGER)")
        self.conn.commit()

    def insert_data(self,Title,Author,Year,ISBN):
        self.cur.execute("INSERT INTO store VALUES(NULL,?,?,?,?)",(Title,Author,Year,ISBN))
        self.conn.commit()

    def view(self):
        self.cur.execute('SELECT * FROM store')
        data= self.cur.fetchall()
        return data

    def Search(self,Title="",Author="",Year="",ISBN=""):
        self.cur.execute("SELECT * FROM store WHERE Title=? OR Author=? OR year=? OR ISBN=?",(Title,Author,Year,ISBN))
        data=self.cur.fetchall()
        self.conn.commit()
        return data

    def delete(self,ID):
        self.cur.execute("DELETE FROM store WHERE ID=?",(ID,))
        self.conn.commit()

    def update(self,ID,Title,Author,Year,ISBN):
        self.cur.execute('UPDATE store SET Title=?,Author=?, Year=?, ISBN=? WHERE ID=?',(Title,Author,Year,ISBN,ID))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()